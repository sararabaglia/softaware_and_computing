#!/usr/bin/env python

from cutFlow import cutFlow


import logging
logging.basicConfig()

logging.getLogger("cutFlow").setLevel(logging.INFO)

logger = logging.getLogger(__name__)

import argparse
import traceback

parser = argparse.ArgumentParser(description="Print cutflows using a configfile. "\
                                             "Some options can also be given on the commandline, "\
                                             "so you don't have to edit the config file each time")
parser.add_argument('configfile', help='python based configfile', nargs="?")
parser.add_argument('-i', help='input root files', nargs="*")
parser.add_argument('--format', '-f', help='csv, txt, tex, yaml')
parser.add_argument('--outputdir', '-o', help='directory to write cutflows to')
parser.add_argument('--filter', help='only print cutflows that match filter')
parser.add_argument('--debug', action='store_true', help='print debug messages')
parser.add_argument('--pdg-rounding', action='store_true', default=False, help='use PDG rounding')
parser.add_argument('--save-merged-cutflows', action='store_true', default=False, help='save the merged cutflow histograms to a root file')
parser.add_argument('--rescale-cutflows', action='store_true', default=False, help='rescale weighted cutflows by xsec/sumw')
parser.add_argument('--xsec-dir', help='directory for cross section files (needed if input files contain empty trees where no xsec info can be extracted)')
parser.add_argument('--lumi', '-l', default=1, help='lumi to normalise the cutflows to (when rescaling)')

args = parser.parse_args()

if not args.i and not args.configfile:
    raise Exception("Need to specify either a config file or input root files")

if args.configfile:
    if args.i:
        raise Exception("Can't use input files if a config file is given")
    try:
        exec(open(args.configfile).read())
    except:
        print("can't read configfile {}".format(args.configfile))
        traceback.print_exc()

if not 'config' in locals():
    config = {}

if args.i:
    config["processes"] = [("", "")]
    config["rootfiles"] = args.i

if args.debug:
    logging.getLogger("cutFlow").setLevel(logging.DEBUG)

if args.format:
    config["format"] = args.format
    if not args.format == "txt" and not args.outputdir:
        raise Exception("Need to provide an output dir for format {}".format(args.format))
if args.outputdir:
    config["outputdir"] = args.outputdir
if args.filter:
    config["filter"] = args.filter
if args.save_merged_cutflows:
    config["save_merged_cutflows"] = args.save_merged_cutflows
if args.rescale_cutflows:
    config["rescale_by"] = lambda sumw, xsec : xsec/sumw
    if args.lumi:
        config["rescale_by"] = lambda sumw, xsec : float(args.lumi)*xsec/sumw
if args.pdg_rounding:
    config["pdgRounding"] = True


cutFlow = cutFlow(**config)

if "treeprocesses" in config:
    table = cutFlow.makeTableFromTrees()
    cutFlow.formatCutFlow(table)
else:
    cutFlow.createCutflows()
