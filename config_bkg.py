config = {
    # names and files containing a list of files with cutflow histograms
    "processes" : [(r"$t\bar t$", "txtfiles/ttbar.txt"),
                   (r"single Top", "txtfiles/singleTop.txt"),
                   (r"$t\bar t$V", "txtfiles/ttV.txt"),
                   (r"W+jets", "txtfiles/Wjets.txt"),
                   (r"Z+jets", "txtfiles/Zjets.txt"),
                   (r"diboson", "txtfiles/diboson.txt"),
                   #(r"1385", "txtfiles/GG_onestepCC_1385_705_25.txt"),
                   (r"total Bkg", "txtfiles/bkg.txt")],

    # you can add an extra column which is an arbitrary function of the 
    # values, for example the ratio of the first and second column:
    # "extracolumns" : [("ratio",
    #                   lambda x: "{:<30.2f}".format(x[0][0]/x[1][0]))],

    # replace strings for nice latex output
    "replacements" : [
        ("<", "$<$"),
        (">", "$>$"),
        ("j([0-9]) pT", "$p_{\mathrm{T}}^{j\\1}$"),
        ("l([0-9]) pT", "$p_{\mathrm{T}}^{l\\1}$"),
        ("mET", "$E_{\mathrm{T}}^{\mathrm{miss}}$"),
        ("mT", "$m_{\mathrm{T}}$"),
        ("meff", "$m_{\mathrm{eff}}$"),
    ],

    "format" : "tex", # possible: csv, txt, tex
    "outputdir" : "tex", # if given, cutflows are written there, otherwise dumped to stdout
}
