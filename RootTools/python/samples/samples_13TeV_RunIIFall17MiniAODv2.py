# COMPONENT CREATOR
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()









#/ggZH_HToGG_ZToQQ_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
#/ggZH_HToGG_ZToNuNu_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
#/ggZH_HToGG_ZToLL_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
#/ZHiggs0PHToGG_M125_13TeV_JHUGenV7011_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
#/VBFHiggs0PHToGG_M125_13TeV_JHUGenV7011_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
#/ZH_HToGG_ZToAll_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
#/WplusH_HToGG_WToAll_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
#/WminusH_HToGG_WToAll_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM




VHToGG_M125_powheg = kreator.makeMCComponent("VHToGG_M125_powheg", "/VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)
VBFHToGG_M125_powheg = kreator.makeMCComponent("VBFHToGG_M_125_powheg", "/VBFHToGG_M-125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)
GluGluHToGG_M125_powheg = kreator.makeMCComponent("GluGluHToGG_M125_powheg", "/GluGluHToGG_M-125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)


THQ_ctcvcp_HToGG_M125 = kreator.makeMCComponent("THQ_ctcvcp_HToGG_M125", "/THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)
THW_ctcvcp_HToGG_M125 = kreator.makeMCComponent("THW_ctcvcp_HToGG_M125", "/THW_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)

VBFHToGG_M125 = kreator.makeMCComponent("VBFHToGG_M_125", "/VBFHToGG_M125_13TeV_amcatnlo_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)
VHToGG_M125 = kreator.makeMCComponent("VHToGG_M125", "/VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)
ttHToGG_M125 = kreator.makeMCComponent("ttHToGG_M125", "/ttHToGG_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)
ttHJetToGG_M125 = kreator.makeMCComponent("ttHJetToGG_M125", "/ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)

GluGluHToGG_M125 = kreator.makeMCComponent("GluGluHToGG_M125", "/GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)


GJet_Pt_20to40_MGG_80toInf = kreator.makeMCComponent("GJet_Pt_20to40_MGG_80toInf", "/GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)
GJet_Pt_40toInf_MGG_80toInf = kreator.makeMCComponent("GJet_Pt_40toInf_MGG_80toInf", "/GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 1)
GJet_Pt_20toInf_MGG_40to80 = kreator.makeMCComponent("GJet_Pt_20toInf_MGG_40to80", "/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)



QCD_Pt_40toInf_MGG_80toInf  = kreator.makeMCComponent("QCD_Pt_40toInf_MGG_80toInf", "/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)
QCD_Pt_30to40_MGG_80toInf  = kreator.makeMCComponent("QCD_Pt_30to40_MGG_80toInf", "/QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)
QCD_Pt_30toInf_MGG_40to80 = kreator.makeMCComponent("QCD_Pt_30toInf_MGG_40to80", "/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)

DiPhotonJetsBox_MGG_80toInf = kreator.makeMCComponent("DiPhotonJetsBox_MGG_80toInf", "/DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 1)

#DiPhotonJetsBox_MGG_80toInf = kreator.makeMCComponent("DiPhotonJetsBox_MGG_80toInf", "/DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v3/MINIAODSIM", "CMS", ".*root", 1)



bbHToGG_M125_4FS_yb2 = kreator.makeMCComponent("bbHToGG_M125_4FS_yb2", "/bbHToGG_M-125_4FS_yb2_13TeV_amcatnlo/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)




MT2hgg = [


    THQ_ctcvcp_HToGG_M125,
    THW_ctcvcp_HToGG_M125,

    VHToGG_M125_powheg,
    VBFHToGG_M125_powheg,
    GluGluHToGG_M125_powheg,

    VBFHToGG_M125,
    VHToGG_M125,
    ttHToGG_M125,
    ttHJetToGG_M125,

    GluGluHToGG_M125,

    GJet_Pt_20to40_MGG_80toInf,
    GJet_Pt_40toInf_MGG_80toInf,
    GJet_Pt_20toInf_MGG_40to80,

    DiPhotonJetsBox_MGG_80toInf,
 
    QCD_Pt_40toInf_MGG_80toInf,
    QCD_Pt_30to40_MGG_80toInf,
    QCD_Pt_30toInf_MGG_40to80,

    bbHToGG_M125_4FS_yb2,

]







# ----------------------------- summary ----------------------------------------


#mcSamples = QCDPtFlat + QCDPt + QCDHT + QCD_Mus + QCD_EMs + QCD_bcToE + Ws + DYs + VJetsQQHT + TTs + Ts + TTXs + TTXXs + DiBosons + TriBosons


#samples = mcSamples

# ---------------------------------------------------------------------

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples, localobjs=locals())
