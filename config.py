config = {
    "processes" : [("ttbar 410000", "ttbar_410000.txt"),],
    "format" : "csv",
    "outputdir" : "csv",


    # optional settings
    # --------------------------------------------------

    # rescale the weighted cutflows by the factor given by this function
    # to normalise them to cross section
    # Caveat: merging multiple samples with this will only work/make
    # sense if there is no further skimming of events that needs to be
    # applied (e.g. truth generator cuts like for ttbar met/ht
    # filtered samples)
    # "rescale_by" : lambda sumw, xsec : xsec/sumw*36065.96,

    # Save merged cutflows to root files
    # "save_merged_cutflows" : True,

    # if cross section can't be found in a tree, try to find it in the txt files here
    # (might be nescessary in case there are empty trees)
    # "xsec_dir" : "$ROOTCOREBIN/data/SUSYTools/mc15_13TeV",
}

