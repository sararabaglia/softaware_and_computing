import ROOT
import re
import os
import math
import logging
import re
import glob
from pprint import pprint

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class EmptyTreeException(Exception):
    pass

class cutFlow:
    def __init__(self,
                 processes=None,
                 treeprocesses=None,
                 rootfiles=None,
                 weights=None,
                 cutFlows=None,
                 lumifactor=None,
                 format="txt",
                 outputdir="csv",
                 replacements=None,
                 extracolumns=None,
                 rescale_by=None,
                 save_merged_cutflows=False,
                 xsec_dir=None,
                 filter=None,
                 pdgRounding=False,
                 names=None):

        self.processes = processes
        self.treeprocesses = treeprocesses
        self.rootfiles = rootfiles
        self.weights = weights
        self.cutFlows = cutFlows
        self.lumifactor = lumifactor
        self.format = format
        self.outputdir = outputdir
        self.extracolumns = extracolumns
        self.replacements = replacements
        self.rescale_by = rescale_by
        self.save_merged_cutflows = save_merged_cutflows
        self.xsec_dir = xsec_dir
        self.filter = filter
        self.pdgRounding = pdgRounding
        self.names = names

        self.sumws = {}

    def createCutflows(self):
        table = self.makeTable()
        self.formatCutFlow(table)

    def yieldRootFiles(self, txtfile):
        if self.rootfiles:
            for rf in self.rootfiles:
                yield rf
        else:
            with open(txtfile) as f:
                for s in f:
                    if s.isspace() or "#" in s:
                        continue
                    yield s.strip()

    @staticmethod
    def getValueFromTree(rf, value):
        tree = rf.Get("tree_NoSys")
        if tree == None:
            raise KeyError("Can't get  {} "
                           "(tree_NoSys wasn't found in {})".
                           format(value, rf.GetName()))
        if tree.GetEntries() == 0:
            raise EmptyTreeException
        tree.Draw(value, "1", "goff", 1)
        return float(tree.GetV1()[0])

    @staticmethod
    def getXsec(rf):
        return cutFlow.getValueFromTree(rf, "xsec")

    @staticmethod
    def getXsecDSID(dsid, xsecPath):
        logger.debug("Trying to get xsec from path {}".format(os.path.expandvars(xsecPath)))
        searchString = "{:.0f}".format(dsid)
        for txtfile in glob.glob(os.path.join(os.path.expandvars(xsecPath), "*")):
            logger.debug("Searching xsec in file {}".format(txtfile))
            with open(txtfile) as f:
                for l in f:
                    if l.startswith(searchString):
                        return float(l.split()[2])
        raise KeyError("Couldn't find xsec for {}".format(dsid))

    @staticmethod
    def getDSID(rf):
        try:
            return cutFlow.getValueFromTree(rf, "DatasetNumber")
        except EmptyTreeException:
            logger.warning("Empty tree for {} - trying to parse from filename".format(rf.GetName()))
            foundDSIDS = re.findall("\.([0-9]{6,6}|[0-9]{8,8})\.", rf.GetName())
            if len(foundDSIDS) < 1:
                logger.error("Couldn't find dsid")
                raise
            logger.warning("Found dsid {}".format(foundDSIDS[0]))
            return int(foundDSIDS[0])

    @staticmethod
    def pdgRound(value,error):
        """
        Given a value and an error, round and format them according to PDG rounding rules.
        """
        def threeDigits(err):
            """Extract the three most significant digits and return as int"""
            return int(("%.2e"%float(err)).split('e')[0].replace('.','').replace('+','').replace('-',''))
        def nSignificantDigits(threeDigits):
            if threeDigits==0: return 0
            assert threeDigits<1000,"three digits (%d) cannot be larger than 10^3"%threeDigits
            assert threeDigits>=100,"three digits (%d) cannot be smaller than 10^2"%threeDigits
            if threeDigits<355 : return 2
            elif threeDigits<950 : return 1
            else : return 2
        def frexp10(value) :
            "convert to mantissa+exp representation (same as frex, but in base 10)"
            valueStr = ("%e"%float(value)).split('e')
            return float(valueStr[0]), int(valueStr[1])
        def nDigitsValue(expVal, expErr, nDigitsErr) :
            "compute the number of digits we want for the value, assuming we keep nDigitsErr for the error"
            return expVal-expErr+nDigitsErr
        def formatValue(value, exponent, nDigits, extraRound=0) :
            "Format the value; extraRound is meant for the special case of threeDigits>950"
            roundAt = nDigits-1-exponent - extraRound
            nDec = roundAt if exponent<nDigits else 0
            nDec = max([nDec, 0])
            return ('%.'+str(nDec)+'f')%round(value,roundAt)
        if value == 0.0 and error == 0.0:
            return (0.0,0.0)
        tD = threeDigits(error)
        nD = nSignificantDigits(tD)
        expVal, expErr = frexp10(value)[1], frexp10(error)[1]
        extraRound = 1 if tD>=950 else 0
        return (formatValue(value, expVal, nDigitsValue(expVal, expErr, nD), extraRound),
                formatValue(error,expErr, nD, extraRound))

    def getSumwFromHist(self,txtfile, dsid):
        mergeList = ROOT.TList()
        hists = []
        for rfName in self.yieldRootFiles(txtfile):
            rf = ROOT.TFile.Open(rfName, "READ")
            hist = rf.Get("weighted__AOD")
            if hist == None:
                raise KeyError("hist weighted__AOD not found in file!".format(txtfile))
            hist.SetDirectory(0)
            rf.Close()
            hists.append(hist)
            mergeList.Add(hist)
        mergedHist = hists[0].Clone()
        mergedHist.Reset()
        mergedHist.Merge(mergeList)
        logger.debug("Merged hist: {}".format(mergedHist))
        logger.debug("Entries: {}".format(mergedHist.GetEntries()))
        binNumber = mergedHist.GetXaxis().FindFixBin("{:.0f}".format(dsid))
        logger.debug("Bin number for {}: {}".format(dsid, binNumber))
        logger.debug("Content: {}".format(mergedHist.GetBinContent(binNumber)))
        if binNumber < 0:
            raise KeyError("No sumw found in weighted__AOD for dsid {}".format(dsid))
        return float(mergedHist.GetBinContent(binNumber))

    def getSumwFromTree(self, txtfile, dsid):
        chain = ROOT.TChain()
        for rfName in self.yieldRootFiles(txtfile):
            found = chain.AddFile(rfName, -1, "CutBookkeepers")
            if not found:
                raise KeyError("Couldn't find CutBookkeeper tree in file {}".format(rfName))
        tmpHist = ROOT.TH1F("sumw", "", 1, 0.5, 1.5)
        found = chain.Draw("1>>sumw", "AllExecutedEvents_sumOfEventWeights*(DatasetNumber=={})".format(dsid), "goff")
        sumw = float(tmpHist.GetBinContent(1))
        del tmpHist
        return sumw

    def getSumw(self, txtfile, dsid):
        if (txtfile, dsid) in self.sumws:
            return self.sumws[(txtfile, dsid)]
        try:
            sumw = self.getSumwFromTree(txtfile, dsid)
        except KeyError:
            logger.debug("Couldn't find cutbookkeeper tree - trying from hist")
            sumw = self.getSumwFromHist(txtfile, dsid)
        logger.debug("Using sumw = {}".format(sumw))
        self.sumws[(txtfile, dsid)] = sumw
        return sumw

    def getCutFlows(self, txtfile):
        """
        Add the cutflows from rootfiles in
        txtfile and return dictionary of
        added cutflows
        """
        cutFlows = {}
        for rfName in self.yieldRootFiles(txtfile):
                rf = ROOT.TFile.Open(rfName, "READ")
                for k in rf.GetListOfKeys():
                    if not "___" in k.GetName():
                        # for now we ignore systematic cutflows
                        continue
                    if "cutFlow" in k.GetName():
                        cutFlowName = k.GetName()
                        hist = rf.Get(cutFlowName)
                        hist.SetDirectory(0)
                        if "weighted" in k.GetName() and self.rescale_by:
                            dsid = self.getDSID(rf)
                            logger.debug("DSID for {}: {}".format(rfName, dsid))
                            sumw = self.getSumw(txtfile, dsid)
                            logger.debug("Sumw for {}: {}".format(rfName, sumw))
                            try:
                                xsec = self.getXsec(rf)
                            except EmptyTreeException:
                                if not self.xsec_dir:
                                    logger.error("Need to provide an xsec_dir if there are empty trees, "
                                                 "but cutflows that should be rescaled!")
                                    raise
                                xsec = self.getXsecDSID(dsid, self.xsec_dir)
                            hist.Scale(self.rescale_by(sumw, xsec))
                        if cutFlowName in cutFlows:
                            self.syncAndAdd(cutFlows[cutFlowName], hist)
                        else:
                            cutFlows[cutFlowName] = hist
                rf.Close()
        return cutFlows

    @staticmethod
    def saveCutflowHists(cutflows, outputFile):
        rf = ROOT.TFile.Open(outputFile, "RECREATE")
        for name, hist in cutflows.items():
            hist.Write(name)
        rf.Close()

    def syncAndAdd(self, hist, newhist):
        """
        Synchronize the bin labels for two histograms
        and add them. The histograms need to have the
        same number of bins
        """
        for i in range(hist.GetNbinsX()):
            label = hist.GetXaxis().GetBinLabel(i)
            newlabel = newhist.GetXaxis().GetBinLabel(i)
            if (label == "" and not newlabel == ""):
                hist.GetXaxis().SetBinLabel(i, newlabel)
            if (newlabel == "" and not label == ""):
                newhist.GetXaxis().SetBinLabel(i, label)
        hist.Add(newhist)

    def makeTable(self):
        """
        create structure that
        contains all information
        to print the cutflow

        table["cutflows"] has a structure like:
        {'cutflow1': [('cutname1', [(yield1, error1),...]),
                      ('cutname2', [(yield1, error1),...]),
                     ...]
         'cutflow2' : ...
        }

        the error is only calculated for cutflows that don't have
        "unweighted" in their names
        """
        table = {}

        for processIndex,(_, process) in enumerate(self.processes):
            cutflows = self.getCutFlows(process)
            if self.save_merged_cutflows:
                rootfileName = "cutflows.root"
                if process:
                    rootfileName = process.replace(".txt", "")+".root"
                self.saveCutflowHists(cutflows, rootfileName)

            # loop over histograms of current process
            for name,hist in cutflows.items():
                logger.info(name)

                # if given, only print cutflow matching filter
                if self.filter and not self.filter in name:
                    continue

                # add cutflow to table
                if not name in table:
                    table[name] = []

                # loop over cuts
                for binIndex in range(hist.GetNbinsX()):
                    label = hist.GetXaxis().GetBinLabel(binIndex)
                    if label == "":
                        continue

                    # if label (cut) is found first time add it to list
                    if not label in [x[0] for x in table[name]]:

                        # initialize list of (_yield, _error) to 0
                        yieldlist = [(0,0) for i in range(len(self.processes))]

                        # add label and corresponding list
                        table[name].append((label, yieldlist))

                    # find index of current label
                    cutIndex = [x[0] for x in table[name]].index(label)

                    _yield = hist.GetBinContent(binIndex)
                    _error = hist.GetBinError(binIndex)

                    table[name][cutIndex][1][processIndex] = (_yield, _error)

                    logger.debug("-"*50)
                    logger.debug("cutFlow: {}".format(name))
                    logger.debug("process: {}".format(process))
                    logger.debug("cut label: {}".format(label))
                    logger.debug("cutIndex: {}".format(cutIndex))
                    logger.debug("binIndex: {}".format(binIndex))
                    logger.debug("_yield: {}".format(_yield))
                    logger.debug("_error: {}".format(_error))

        returntable = {}
        returntable["cutflows"] = table
        returntable["processes"] = self.processes
        return returntable

    def makeTableFromTrees(self):
        table = {}

        openTrees = {} # index "filename_treename"
        openFiles = {}

        for cutFlow, rows in self.cutFlows.items():
            table[cutFlow] = []
            table[cutFlow+"_unweighted"] = []
            for i, (cutname, cut, kwargs) in enumerate(rows):
                expr = "({})*(1".format(self.weights)
                noweight_expr = "(1"

                yields = []
                yields_unweighted = []
                row = (cutname, yields)
                row_unweighted = (cutname, yields_unweighted)

                # in case the user wants to ignore a specific cut for a given row
                for j,(cutname, cut, _) in enumerate(rows):
                    if j>i or j in kwargs.get("ignoreCuts",[]):
                        continue
                    expr+="&&"+cut
                    noweight_expr+="&&"+cut
                expr += ")"
                noweight_expr += ")"

                for _,treelist in self.treeprocesses:
                    _yield = 0
                    _yield_unweighted = 0
                    _error = 0
                    for filename, treename, kwargs in treelist:
                        index = "{}_{}".format(filename, treename)
                        if index in openTrees:
                            tree = openTrees[index]
                        else:
                            if filename in openFiles:
                                rootfile = openFiles[filename]
                            else:
                                rootfile = ROOT.TFile(filename)
                                openFiles[filename] = rootfile
                            tree = rootfile.Get(treename)
                            openTrees[index] = tree
                        # for process-specific weights
                        _expr = "({})*({})".format(expr,kwargs.get("process_weight","1"))
                        # helper hist to project to
                        # in order to get yield and error
                        h = ROOT.TH1F("h","",1,0.5,1.5)
                        h.Sumw2()
                        logger.debug("projecting {}".format(_expr))
                        logger.debug("tree: {}".format(treename))
                        n = tree.Project("h","1",_expr)
                        weighted = h.Integral()
                        raw = tree.GetEntries(noweight_expr)
                        _yield += weighted
                        _yield_unweighted += raw
                        _error += h.GetBinError(1)**2
                        del h
                    _error = math.sqrt(_error)
                    if self.lumifactor:
                        _yield = self.lumifactor*_yield
                        _error = self.lumifactor*_error
                    yields.append((_yield, _error))
                    yields_unweighted.append((_yield_unweighted, 0))
                table[cutFlow].append(row)
                table[cutFlow+"_unweighted"].append(row_unweighted)
        returntable = {}
        returntable["cutflows"] = table
        returntable["processes"] = self.treeprocesses
        return returntable



    def formatCutFlow(self, table):
        """
        Output formatted cutFlow
        """
        _format = self.format
        possibleFormats = ["txt", "tex", "csv", "yaml"]
        if not _format in possibleFormats:
            raise ValueError("Format \"{}\" unknown. Possible values: {}"
                             .format(_format, " ".join(possibleFormats)))
        # --------------------------------------------------
        if _format == "txt":
            firstColumnWidth = 30
            for name, cutFlow in sorted(table["cutflows"].items()):
                logger.info("cutflow for {}:".format(name))
                out = []
                p = out.append
                p("{0:<{1}}".format("",firstColumnWidth))
                for process, _ in table["processes"]:
                    p("{:<30}".format(process))
                if self.extracolumns:
                    for desc,_ in self.extracolumns:
                            p("{:<30}".format(desc))
                p("\n")
                for cut, yields in cutFlow:
                    p("{0:<{1}}".format(self.replaceNames(cut), firstColumnWidth))
                    for _yield, _error in yields:
                        if "unweighted" in name:
                            s = "{:>15.0f}".format(_yield)
                        else:
                            s = "{:>12.2f} +/- {:<13.2f}".format(_yield, _error)
                        p("{:<30}".format(s))

                    if self.extracolumns:
                        for _,func in self.extracolumns:
                            p(func(yields))

                    p("\n")
                print("".join(out))
        # --------------------------------------------------
        if _format == "csv":
            for name, cutFlow in sorted(table["cutflows"].items()):
                logger.info("cutflow for {}:".format(name))
                out = []
                p = out.append
                p(",")
                for process, _ in table["processes"]:
                    p("\"{}\",,".format(process))
                if self.extracolumns:
                    for desc,_ in self.extracolumns:
                            p("\"{}\",,".format(desc))
                p("\n")
                for cut, yields in cutFlow:
                    p("\"{}\",".format(self.replaceNames(cut)))
                    for _yield, _error in yields:
                        if "unweighted" in name:
                            s = "{},,".format(_yield)
                        else:
                            s = "{0},{1},".format(_yield, _error)
                        p(s)

                    if self.extracolumns:
                        for _,func in self.extracolumns:
                            p(func(yields).strip()+",")

                    p("\n")
                outputdir = self.outputdir
                if outputdir:
                    if not os.path.exists(outputdir):
                        os.mkdir(outputdir)
                    _filename = os.path.join(outputdir, "{}.csv".format(name))
                    logger.info("writing to file "+_filename)
                    with open(_filename, "w") as f:
                        f.write("".join(out))
                else:
                    print("".join(out))
        # --------------------------------------------------
        if _format == "tex":
            firstColumnWidth = 30
            for name, cutFlow in sorted(table["cutflows"].items()):
                logger.info("cutflow for {}:".format(name))
                out = []
                p = out.append
                if self.extracolumns:
                    nextra = len(self.extracolumns)
                else:
                    nextra = 0
                p("\\begin{{tabular}}{{l{0}}}\n"
                  .format("c"*(len(table["processes"])+nextra)))
                p("\\hline\\hline\n")
                if self.names and not "unweighted" in name:
                    p("{:<30}".format(self.names.pop(0)))
                else:
                    p("{0:<{1}}".format("",firstColumnWidth))
                for process, _ in table["processes"]:
                    p("{:<30}".format("& "+process))
                if self.extracolumns:
                    for desc,_ in self.extracolumns:
                            p("{:<30}".format("& "+desc))
                p("\\\\\n")
                p("\\hline\n")
                for cut, yields in cutFlow:
                    p("{0:<{1}}".format(self.replaceNames(cut), firstColumnWidth))
                    for _yield, _error in yields:
                        if "unweighted" in name:
                            s = "& {:>13.0f}".format(_yield)
                        else:
                            if self.pdgRounding:
                                (_yield,_error) = self.pdgRound(_yield,_error)
                                s = "& {}$\\pm${}".format(_yield, _error)
                            else:
                                s = "& {:>12.2f}$\\pm${:<11.2f}".format(_yield, _error)
                        p("{:<30}".format(s))

                    if self.extracolumns:
                        for _,func in self.extracolumns:
                            p("& "+func(yields))

                    p("\\\\\n")
                p("\\hline\\hline\n")
                p("\\end{tabular}\n")
                outputdir = self.outputdir
                if outputdir:
                    if not os.path.exists(outputdir):
                        os.mkdir(outputdir)
                    _filename = os.path.join(outputdir, "{}.tex".format(name))
                    logger.info("writing to file "+_filename)
                    with open(_filename, "w") as f:
                        f.write("".join(out))
                else:
                    print("".join(out))
        # --------------------------------------------------
        if _format == "yaml":
            for name, cutFlow in sorted(table["cutflows"].items()):
                if "unweighted" in name:
                    # skip unweighted for yaml, since this is mostly for hepdata anyway and we don't need raw events there ...
                    continue
                logger.info("cutflow for {}:".format(name))
                out = []
                p = out.append

                p("independent_variables:\n")
                p("- header: {{name: 'Cut', units: ''}}\n")
                p("  values:\n")

                for cut, yields in cutFlow:
                    p("- {{value: '{}'}}\n".format(cut))

                p("\n")
                for idx, (process, _) in enumerate(table["processes"]):
                    p("dependent_variables:\n")
                    p("- header: {{name: '{}', units: ''}}\n".format(process))
                    p("  qualifiers:\n")
                    p("  - {{name: SQRT(S), units: GEV, value: '13000.0'}}\n")
                    p("  values:\n")
                    for cut, yields in cutFlow:
                        (_yield, _error) = yields[idx]
                        if self.pdgRounding: (_yield, _error) = self.pdgRound(_yield,_error)
                        p("  - errors: [{{label: stat, symerror: {}}}]\n".format(_error))
                        p("    value: '{}'\n".format(_yield))
                    p("\n")

                p("\n")

                outputdir = self.outputdir
                if outputdir:
                    if not os.path.exists(outputdir):
                        os.mkdir(outputdir)
                    _filename = os.path.join(outputdir, "{}.yaml".format(name))
                    logger.info("writing to file "+_filename)
                    with open(_filename, "w") as f:
                        f.write("".join(out))
                else:
                    print("".join(out))
        # --------------------------------------------------
    def replaceNames(self, s):
        if not self.replacements:
            return s
        for pattern, replacement in self.replacements:
            return re.sub(pattern, replacement, s)
