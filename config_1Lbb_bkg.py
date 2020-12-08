_treefilename = "/project/etp4/eschanet/ntuples/common/full_run_2/v1-20/allTrees_v1_20_1_combined_bkg.root"

config = {
    "treeprocesses" : [
        ("ttbar", [(_treefilename, "ttbar_NoSys")]),
        ("singletop", [(_treefilename, "singletop_NoSys")]),
        ("wjets", [(_treefilename, "wjets_NoSys")]),
        ("zjets", [(_treefilename, "zjets_NoSys")]),
        ("diboson", [(_treefilename, "diboson_NoSys")]),
        ("ttv", [(_treefilename, "ttv_NoSys")]),
        ("tth", [(_treefilename, "tth_NoSys")]),
        ("multiboson", [(_treefilename, "multiboson_NoSys")]),
        ("vh", [(_treefilename, "vh_NoSys")])
    ],
    "cutFlows" : {
        "cutflow_1lbb" : [
            ("Preselection 1 lepton, $N_\mathrm{jet30} = $ 2-3, $E_\mathrm{T}^\mathrm{miss} > $ 200 GeV", "met>200&&nJet30>=2&&nJet30<4&&nLep_base==1&&nLep_signal==1"),
            ("$m_{\mathrm{T}}$ $>$ 50 GeV", "mt>50"),
            ("$N_{\mathrm{b-jets,30}} =$ 2", "nBJet30_MV2c10==2"),
            ("$m_{\mathrm{bb}}$ $>$ 50 GeV", "mbb>50"),
            ("105 $<$ $m_{\mathrm{bb}}$ $<$ 135 GeV", "mbb>105&&mbb<135"),
            ("$m_{\mathrm{CT}}$ $>$ 160 GeV", "mct2>240"),
            ("$E_\mathrm{T}^\mathrm{miss} > $ 240 GeV", "met>240"),
            ("$m_{\mathrm{T}}$ $>$ 100 GeV", "mt>100")
        ]
    },
    "lumifactor" : 140500, # multiply the cutflows by this factor
    "format" : "tex",
    "outputdir" : "tex",
    "weights" : "genWeight*eventWeight*pileupWeight*leptonWeight*bTagWeight*jvtWeight",
}
