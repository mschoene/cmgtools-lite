import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### ----------------------------- Zero Tesla run  ----------------------------------------

dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"  # use environmental variable, useful for instance to run on CRAB
json=dataDir+'/json/json_DCSONLY.txt'

JetHT_Run2016B_PromptReco_v1          = kreator.makeDataComponent("JetHT_Run2016B_PromptReco_v1"         , "/JetHT/Run2016B-PromptReco-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016B_PromptReco_v1          = kreator.makeDataComponent("HTMHT_Run2016B_PromptReco_v1"         , "/HTMHT/Run2016B-PromptReco-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016B_PromptReco_v1            = kreator.makeDataComponent("MET_Run2016B_PromptReco_v1"           , "/MET/Run2016B-PromptReco-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016B_PromptReco_v1 = kreator.makeDataComponent("SingleElectron_Run2016B_PromptReco_v1", "/SingleElectron/Run2016B-PromptReco-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016B_PromptReco_v1     = kreator.makeDataComponent("SingleMuon_Run2016B_PromptReco_v1"    , "/SingleMuon/Run2016B-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016B_PromptReco_v1   = kreator.makeDataComponent("SinglePhoton_Run2016B_PromptReco_v1"  , "/SinglePhoton/Run2016B-PromptReco-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016B_PromptReco_v1       = kreator.makeDataComponent("DoubleEG_Run2016B_PromptReco_v1"      , "/DoubleEG/Run2016B-PromptReco-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016B_PromptReco_v1         = kreator.makeDataComponent("MuonEG_Run2016B_PromptReco_v1"        , "/MuonEG/Run2016B-PromptReco-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016B_PromptReco_v1     = kreator.makeDataComponent("DoubleMuon_Run2016B_PromptReco_v1"    , "/DoubleMuon/Run2016B-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json)

JetHT_Run2016B_PromptReco_v2          = kreator.makeDataComponent("JetHT_Run2016B_PromptReco_v2"         , "/JetHT/Run2016B-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016B_PromptReco_v2          = kreator.makeDataComponent("HTMHT_Run2016B_PromptReco_v2"         , "/HTMHT/Run2016B-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016B_PromptReco_v2            = kreator.makeDataComponent("MET_Run2016B_PromptReco_v2"           , "/MET/Run2016B-PromptReco-v2/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016B_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016B_PromptReco_v2", "/SingleElectron/Run2016B-PromptReco-v2/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016B_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016B_PromptReco_v2"    , "/SingleMuon/Run2016B-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016B_PromptReco_v2   = kreator.makeDataComponent("SinglePhoton_Run2016B_PromptReco_v2"  , "/SinglePhoton/Run2016B-PromptReco-v2/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016B_PromptReco_v2       = kreator.makeDataComponent("DoubleEG_Run2016B_PromptReco_v2"      , "/DoubleEG/Run2016B-PromptReco-v2/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016B_PromptReco_v2         = kreator.makeDataComponent("MuonEG_Run2016B_PromptReco_v2"        , "/MuonEG/Run2016B-PromptReco-v2/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016B_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016B_PromptReco_v2"    , "/DoubleMuon/Run2016B-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)

# runB re-reco have either v1 or v2, and all have v3. They include exclusive run range so both must be merged
JetHT_Run2016B_23Sep2016_v1          = kreator.makeDataComponent("JetHT_Run2016B_23Sep2016_v1"         , "/JetHT/Run2016B-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016B_23Sep2016_v1          = kreator.makeDataComponent("HTMHT_Run2016B_23Sep2016_v1"         , "/HTMHT/Run2016B-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016B_23Sep2016_v2            = kreator.makeDataComponent("MET_Run2016B_23Sep2016_v2"           , "/MET/Run2016B-23Sep2016-v2/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016B_23Sep2016_v2 = kreator.makeDataComponent("SingleElectron_Run2016B_23Sep2016_v2", "/SingleElectron/Run2016B-23Sep2016-v2/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016B_23Sep2016_v1     = kreator.makeDataComponent("SingleMuon_Run2016B_23Sep2016_v1"    , "/SingleMuon/Run2016B-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016B_23Sep2016_v1   = kreator.makeDataComponent("SinglePhoton_Run2016B_23Sep2016_v1"  , "/SinglePhoton/Run2016B-23Sep2016-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016B_23Sep2016_v2       = kreator.makeDataComponent("DoubleEG_Run2016B_23Sep2016_v2"      , "/DoubleEG/Run2016B-23Sep2016-v2/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016B_23Sep2016_v2         = kreator.makeDataComponent("MuonEG_Run2016B_23Sep2016_v2"        , "/MuonEG/Run2016B-23Sep2016-v2/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016B_23Sep2016_v1     = kreator.makeDataComponent("DoubleMuon_Run2016B_23Sep2016_v1"    , "/DoubleMuon/Run2016B-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)

JetHT_Run2016B_23Sep2016_v3          = kreator.makeDataComponent("JetHT_Run2016B_23Sep2016_v3"         , "/JetHT/Run2016B-23Sep2016-v3/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016B_23Sep2016_v3          = kreator.makeDataComponent("HTMHT_Run2016B_23Sep2016_v3"         , "/HTMHT/Run2016B-23Sep2016-v3/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016B_23Sep2016_v3            = kreator.makeDataComponent("MET_Run2016B_23Sep2016_v3"           , "/MET/Run2016B-23Sep2016-v3/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016B_23Sep2016_v3 = kreator.makeDataComponent("SingleElectron_Run2016B_23Sep2016_v3", "/SingleElectron/Run2016B-23Sep2016-v3/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016B_23Sep2016_v3     = kreator.makeDataComponent("SingleMuon_Run2016B_23Sep2016_v3"    , "/SingleMuon/Run2016B-23Sep2016-v3/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016B_23Sep2016_v3   = kreator.makeDataComponent("SinglePhoton_Run2016B_23Sep2016_v3"  , "/SinglePhoton/Run2016B-23Sep2016-v3/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016B_23Sep2016_v3       = kreator.makeDataComponent("DoubleEG_Run2016B_23Sep2016_v3"      , "/DoubleEG/Run2016B-23Sep2016-v3/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016B_23Sep2016_v3         = kreator.makeDataComponent("MuonEG_Run2016B_23Sep2016_v3"        , "/MuonEG/Run2016B-23Sep2016-v3/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016B_23Sep2016_v3     = kreator.makeDataComponent("DoubleMuon_Run2016B_23Sep2016_v3"    , "/DoubleMuon/Run2016B-23Sep2016-v3/MINIAOD"    , "CMS", ".*root", json)


#run_range = (275377, 284)
JetHT_Run2016C_PromptReco_v2          = kreator.makeDataComponent("JetHT_Run2016C_PromptReco_v2"         , "/JetHT/Run2016C-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016C_PromptReco_v2          = kreator.makeDataComponent("HTMHT_Run2016C_PromptReco_v2"         , "/HTMHT/Run2016C-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016C_PromptReco_v2            = kreator.makeDataComponent("MET_Run2016C_PromptReco_v2"           , "/MET/Run2016C-PromptReco-v2/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016C_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016C_PromptReco_v2", "/SingleElectron/Run2016C-PromptReco-v2/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016C_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016C_PromptReco_v2"    , "/SingleMuon/Run2016C-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016C_PromptReco_v2   = kreator.makeDataComponent("SinglePhoton_Run2016C_PromptReco_v2"  , "/SinglePhoton/Run2016C-PromptReco-v2/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016C_PromptReco_v2       = kreator.makeDataComponent("DoubleEG_Run2016C_PromptReco_v2"      , "/DoubleEG/Run2016C-PromptReco-v2/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016C_PromptReco_v2         = kreator.makeDataComponent("MuonEG_Run2016C_PromptReco_v2"        , "/MuonEG/Run2016C-PromptReco-v2/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016C_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016C_PromptReco_v2"    , "/DoubleMuon/Run2016C-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)

JetHT_Run2016C_23Sep2016_v1          = kreator.makeDataComponent("JetHT_Run2016C_23Sep2016_v1"         , "/JetHT/Run2016C-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016C_23Sep2016_v1          = kreator.makeDataComponent("HTMHT_Run2016C_23Sep2016_v1"         , "/HTMHT/Run2016C-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016C_23Sep2016_v1            = kreator.makeDataComponent("MET_Run2016C_23Sep2016_v1"           , "/MET/Run2016C-23Sep2016-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016C_23Sep2016_v1 = kreator.makeDataComponent("SingleElectron_Run2016C_23Sep2016_v1", "/SingleElectron/Run2016C-23Sep2016-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016C_23Sep2016_v1     = kreator.makeDataComponent("SingleMuon_Run2016C_23Sep2016_v1"    , "/SingleMuon/Run2016C-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016C_23Sep2016_v1   = kreator.makeDataComponent("SinglePhoton_Run2016C_23Sep2016_v1"  , "/SinglePhoton/Run2016C-23Sep2016-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016C_23Sep2016_v1       = kreator.makeDataComponent("DoubleEG_Run2016C_23Sep2016_v1"      , "/DoubleEG/Run2016C-23Sep2016-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016C_23Sep2016_v1         = kreator.makeDataComponent("MuonEG_Run2016C_23Sep2016_v1"        , "/MuonEG/Run2016C-23Sep2016-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016C_23Sep2016_v1     = kreator.makeDataComponent("DoubleMuon_Run2016C_23Sep2016_v1"    , "/DoubleMuon/Run2016C-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)

#run_rangeD = (276311 , 276811) #full runD range
JetHT_Run2016D_PromptReco_v2          = kreator.makeDataComponent("JetHT_Run2016D_PromptReco_v2"         , "/JetHT/Run2016D-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016D_PromptReco_v2          = kreator.makeDataComponent("HTMHT_Run2016D_PromptReco_v2"         , "/HTMHT/Run2016D-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016D_PromptReco_v2            = kreator.makeDataComponent("MET_Run2016D_PromptReco_v2"           , "/MET/Run2016D-PromptReco-v2/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016D_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016D_PromptReco_v2", "/SingleElectron/Run2016D-PromptReco-v2/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016D_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016D_PromptReco_v2"    , "/SingleMuon/Run2016D-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016D_PromptReco_v2   = kreator.makeDataComponent("SinglePhoton_Run2016D_PromptReco_v2"  , "/SinglePhoton/Run2016D-PromptReco-v2/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016D_PromptReco_v2       = kreator.makeDataComponent("DoubleEG_Run2016D_PromptReco_v2"      , "/DoubleEG/Run2016D-PromptReco-v2/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016D_PromptReco_v2         = kreator.makeDataComponent("MuonEG_Run2016D_PromptReco_v2"        , "/MuonEG/Run2016D-PromptReco-v2/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016D_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016D_PromptReco_v2"    , "/DoubleMuon/Run2016D-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)

JetHT_Run2016D_23Sep2016_v1          = kreator.makeDataComponent("JetHT_Run2016D_23Sep2016_v1"         , "/JetHT/Run2016D-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016D_23Sep2016_v1          = kreator.makeDataComponent("HTMHT_Run2016D_23Sep2016_v1"         , "/HTMHT/Run2016D-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016D_23Sep2016_v1            = kreator.makeDataComponent("MET_Run2016D_23Sep2016_v1"           , "/MET/Run2016D-23Sep2016-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016D_23Sep2016_v1 = kreator.makeDataComponent("SingleElectron_Run2016D_23Sep2016_v1", "/SingleElectron/Run2016D-23Sep2016-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016D_23Sep2016_v1     = kreator.makeDataComponent("SingleMuon_Run2016D_23Sep2016_v1"    , "/SingleMuon/Run2016D-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016D_23Sep2016_v1   = kreator.makeDataComponent("SinglePhoton_Run2016D_23Sep2016_v1"  , "/SinglePhoton/Run2016D-23Sep2016-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016D_23Sep2016_v1       = kreator.makeDataComponent("DoubleEG_Run2016D_23Sep2016_v1"      , "/DoubleEG/Run2016D-23Sep2016-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016D_23Sep2016_v1         = kreator.makeDataComponent("MuonEG_Run2016D_23Sep2016_v1"        , "/MuonEG/Run2016D-23Sep2016-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016D_23Sep2016_v1     = kreator.makeDataComponent("DoubleMuon_Run2016D_23Sep2016_v1"    , "/DoubleMuon/Run2016D-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)

#run_range = (276831, 277420) #full runE range
JetHT_Run2016E_PromptReco_v2          = kreator.makeDataComponent("JetHT_Run2016E_PromptReco_v2"         , "/JetHT/Run2016E-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016E_PromptReco_v2          = kreator.makeDataComponent("HTMHT_Run2016E_PromptReco_v2"         , "/HTMHT/Run2016E-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016E_PromptReco_v2            = kreator.makeDataComponent("MET_Run2016E_PromptReco_v2"           , "/MET/Run2016E-PromptReco-v2/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016E_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016E_PromptReco_v2", "/SingleElectron/Run2016E-PromptReco-v2/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016E_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016E_PromptReco_v2"    , "/SingleMuon/Run2016E-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016E_PromptReco_v2   = kreator.makeDataComponent("SinglePhoton_Run2016E_PromptReco_v2"  , "/SinglePhoton/Run2016E-PromptReco-v2/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016E_PromptReco_v2       = kreator.makeDataComponent("DoubleEG_Run2016E_PromptReco_v2"      , "/DoubleEG/Run2016E-PromptReco-v2/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016E_PromptReco_v2         = kreator.makeDataComponent("MuonEG_Run2016E_PromptReco_v2"        , "/MuonEG/Run2016E-PromptReco-v2/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016E_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016E_PromptReco_v2"    , "/DoubleMuon/Run2016E-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)

JetHT_Run2016E_23Sep2016_v1          = kreator.makeDataComponent("JetHT_Run2016E_23Sep2016_v1"         , "/JetHT/Run2016E-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016E_23Sep2016_v1          = kreator.makeDataComponent("HTMHT_Run2016E_23Sep2016_v1"         , "/HTMHT/Run2016E-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016E_23Sep2016_v1            = kreator.makeDataComponent("MET_Run2016E_23Sep2016_v1"           , "/MET/Run2016E-23Sep2016-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016E_23Sep2016_v1 = kreator.makeDataComponent("SingleElectron_Run2016E_23Sep2016_v1", "/SingleElectron/Run2016E-23Sep2016-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016E_23Sep2016_v1     = kreator.makeDataComponent("SingleMuon_Run2016E_23Sep2016_v1"    , "/SingleMuon/Run2016E-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016E_23Sep2016_v1   = kreator.makeDataComponent("SinglePhoton_Run2016E_23Sep2016_v1"  , "/SinglePhoton/Run2016E-23Sep2016-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016E_23Sep2016_v1       = kreator.makeDataComponent("DoubleEG_Run2016E_23Sep2016_v1"      , "/DoubleEG/Run2016E-23Sep2016-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016E_23Sep2016_v1         = kreator.makeDataComponent("MuonEG_Run2016E_23Sep2016_v1"        , "/MuonEG/Run2016E-23Sep2016-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016E_23Sep2016_v1     = kreator.makeDataComponent("DoubleMuon_Run2016E_23Sep2016_v1"    , "/DoubleMuon/Run2016E-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)

#run_rangeF = ( 277772, 278808) # full runF range
JetHT_Run2016F_PromptReco_v1          = kreator.makeDataComponent("JetHT_Run2016F_PromptReco_v1"         , "/JetHT/Run2016F-PromptReco-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016F_PromptReco_v1          = kreator.makeDataComponent("HTMHT_Run2016F_PromptReco_v1"         , "/HTMHT/Run2016F-PromptReco-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016F_PromptReco_v1            = kreator.makeDataComponent("MET_Run2016F_PromptReco_v1"           , "/MET/Run2016F-PromptReco-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016F_PromptReco_v1 = kreator.makeDataComponent("SingleElectron_Run2016F_PromptReco_v1", "/SingleElectron/Run2016F-PromptReco-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016F_PromptReco_v1     = kreator.makeDataComponent("SingleMuon_Run2016F_PromptReco_v1"    , "/SingleMuon/Run2016F-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016F_PromptReco_v1   = kreator.makeDataComponent("SinglePhoton_Run2016F_PromptReco_v1"  , "/SinglePhoton/Run2016F-PromptReco-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016F_PromptReco_v1       = kreator.makeDataComponent("DoubleEG_Run2016F_PromptReco_v1"      , "/DoubleEG/Run2016F-PromptReco-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016F_PromptReco_v1         = kreator.makeDataComponent("MuonEG_Run2016F_PromptReco_v1"        , "/MuonEG/Run2016F-PromptReco-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016F_PromptReco_v1     = kreator.makeDataComponent("DoubleMuon_Run2016F_PromptReco_v1"    , "/DoubleMuon/Run2016F-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json)

JetHT_Run2016F_23Sep2016_v1          = kreator.makeDataComponent("JetHT_Run2016F_23Sep2016_v1"         , "/JetHT/Run2016F-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016F_23Sep2016_v1          = kreator.makeDataComponent("HTMHT_Run2016F_23Sep2016_v1"         , "/HTMHT/Run2016F-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016F_23Sep2016_v1            = kreator.makeDataComponent("MET_Run2016F_23Sep2016_v1"           , "/MET/Run2016F-23Sep2016-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016F_23Sep2016_v1 = kreator.makeDataComponent("SingleElectron_Run2016F_23Sep2016_v1", "/SingleElectron/Run2016F-23Sep2016-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016F_23Sep2016_v1     = kreator.makeDataComponent("SingleMuon_Run2016F_23Sep2016_v1"    , "/SingleMuon/Run2016F-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016F_23Sep2016_v1   = kreator.makeDataComponent("SinglePhoton_Run2016F_23Sep2016_v1"  , "/SinglePhoton/Run2016F-23Sep2016-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016F_23Sep2016_v1       = kreator.makeDataComponent("DoubleEG_Run2016F_23Sep2016_v1"      , "/DoubleEG/Run2016F-23Sep2016-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016F_23Sep2016_v1         = kreator.makeDataComponent("MuonEG_Run2016F_23Sep2016_v1"        , "/MuonEG/Run2016F-23Sep2016-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016F_23Sep2016_v1     = kreator.makeDataComponent("DoubleMuon_Run2016F_23Sep2016_v1"    , "/DoubleMuon/Run2016F-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)

#run_rangeG = ( 278820, 280385) # full runG range
JetHT_Run2016G_PromptReco_v1          = kreator.makeDataComponent("JetHT_Run2016G_PromptReco_v1"         , "/JetHT/Run2016G-PromptReco-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016G_PromptReco_v1          = kreator.makeDataComponent("HTMHT_Run2016G_PromptReco_v1"         , "/HTMHT/Run2016G-PromptReco-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016G_PromptReco_v1            = kreator.makeDataComponent("MET_Run2016G_PromptReco_v1"           , "/MET/Run2016G-PromptReco-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016G_PromptReco_v1 = kreator.makeDataComponent("SingleElectron_Run2016G_PromptReco_v1", "/SingleElectron/Run2016G-PromptReco-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016G_PromptReco_v1     = kreator.makeDataComponent("SingleMuon_Run2016G_PromptReco_v1"    , "/SingleMuon/Run2016G-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016G_PromptReco_v1   = kreator.makeDataComponent("SinglePhoton_Run2016G_PromptReco_v1"  , "/SinglePhoton/Run2016G-PromptReco-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016G_PromptReco_v1       = kreator.makeDataComponent("DoubleEG_Run2016G_PromptReco_v1"      , "/DoubleEG/Run2016G-PromptReco-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016G_PromptReco_v1         = kreator.makeDataComponent("MuonEG_Run2016G_PromptReco_v1"        , "/MuonEG/Run2016G-PromptReco-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016G_PromptReco_v1     = kreator.makeDataComponent("DoubleMuon_Run2016G_PromptReco_v1"    , "/DoubleMuon/Run2016G-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json)

JetHT_Run2016G_23Sep2016_v1          = kreator.makeDataComponent("JetHT_Run2016G_23Sep2016_v1"         , "/JetHT/Run2016G-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016G_23Sep2016_v2          = kreator.makeDataComponent("HTMHT_Run2016G_23Sep2016_v2"         , "/HTMHT/Run2016G-23Sep2016-v2/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016G_23Sep2016_v1            = kreator.makeDataComponent("MET_Run2016G_23Sep2016_v1"           , "/MET/Run2016G-23Sep2016-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016G_23Sep2016_v1 = kreator.makeDataComponent("SingleElectron_Run2016G_23Sep2016_v1", "/SingleElectron/Run2016G-23Sep2016-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016G_23Sep2016_v1     = kreator.makeDataComponent("SingleMuon_Run2016G_23Sep2016_v1"    , "/SingleMuon/Run2016G-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016G_23Sep2016_v1   = kreator.makeDataComponent("SinglePhoton_Run2016G_23Sep2016_v1"  , "/SinglePhoton/Run2016G-23Sep2016-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016G_23Sep2016_v1       = kreator.makeDataComponent("DoubleEG_Run2016G_23Sep2016_v1"      , "/DoubleEG/Run2016G-23Sep2016-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016G_23Sep2016_v1         = kreator.makeDataComponent("MuonEG_Run2016G_23Sep2016_v1"        , "/MuonEG/Run2016G-23Sep2016-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016G_23Sep2016_v1     = kreator.makeDataComponent("DoubleMuon_Run2016G_23Sep2016_v1"    , "/DoubleMuon/Run2016G-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)

# runH, both v2 and v3 are needed (v1 has nothing)
#run_rangeH = ( 280919, 284044) # runH 
JetHT_Run2016H_PromptReco_v2          = kreator.makeDataComponent("JetHT_Run2016H_PromptReco_v2"         , "/JetHT/Run2016H-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016H_PromptReco_v2          = kreator.makeDataComponent("HTMHT_Run2016H_PromptReco_v2"         , "/HTMHT/Run2016H-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016H_PromptReco_v2            = kreator.makeDataComponent("MET_Run2016H_PromptReco_v2"           , "/MET/Run2016H-PromptReco-v2/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016H_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016H_PromptReco_v2", "/SingleElectron/Run2016H-PromptReco-v2/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016H_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016H_PromptReco_v2"    , "/SingleMuon/Run2016H-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016H_PromptReco_v2   = kreator.makeDataComponent("SinglePhoton_Run2016H_PromptReco_v2"  , "/SinglePhoton/Run2016H-PromptReco-v2/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016H_PromptReco_v2       = kreator.makeDataComponent("DoubleEG_Run2016H_PromptReco_v2"      , "/DoubleEG/Run2016H-PromptReco-v2/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016H_PromptReco_v2         = kreator.makeDataComponent("MuonEG_Run2016H_PromptReco_v2"        , "/MuonEG/Run2016H-PromptReco-v2/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016H_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016H_PromptReco_v2"    , "/DoubleMuon/Run2016H-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)

JetHT_Run2016H_PromptReco_v3          = kreator.makeDataComponent("JetHT_Run2016H_PromptReco_v3"         , "/JetHT/Run2016H-PromptReco-v3/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016H_PromptReco_v3          = kreator.makeDataComponent("HTMHT_Run2016H_PromptReco_v3"         , "/HTMHT/Run2016H-PromptReco-v3/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016H_PromptReco_v3            = kreator.makeDataComponent("MET_Run2016H_PromptReco_v3"           , "/MET/Run2016H-PromptReco-v3/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016H_PromptReco_v3 = kreator.makeDataComponent("SingleElectron_Run2016H_PromptReco_v3", "/SingleElectron/Run2016H-PromptReco-v3/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016H_PromptReco_v3     = kreator.makeDataComponent("SingleMuon_Run2016H_PromptReco_v3"    , "/SingleMuon/Run2016H-PromptReco-v3/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016H_PromptReco_v3   = kreator.makeDataComponent("SinglePhoton_Run2016H_PromptReco_v3"  , "/SinglePhoton/Run2016H-PromptReco-v3/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016H_PromptReco_v3       = kreator.makeDataComponent("DoubleEG_Run2016H_PromptReco_v3"      , "/DoubleEG/Run2016H-PromptReco-v3/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016H_PromptReco_v3         = kreator.makeDataComponent("MuonEG_Run2016H_PromptReco_v3"        , "/MuonEG/Run2016H-PromptReco-v3/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016H_PromptReco_v3     = kreator.makeDataComponent("DoubleMuon_Run2016H_PromptReco_v3"    , "/DoubleMuon/Run2016H-PromptReco-v3/MINIAOD"    , "CMS", ".*root", json)


# old bad data (unlikely a run will be certified as good from this period)
dataSamples_Run2016B_PromptV1 = [JetHT_Run2016B_PromptReco_v1, HTMHT_Run2016B_PromptReco_v1, MET_Run2016B_PromptReco_v1, SingleElectron_Run2016B_PromptReco_v1, SingleMuon_Run2016B_PromptReco_v1, SinglePhoton_Run2016B_PromptReco_v1, DoubleEG_Run2016B_PromptReco_v1, MuonEG_Run2016B_PromptReco_v1, DoubleMuon_Run2016B_PromptReco_v1] 

# runB
dataSamples_Run2016B_PromptV2 = [JetHT_Run2016B_PromptReco_v2, HTMHT_Run2016B_PromptReco_v2, MET_Run2016B_PromptReco_v2, SingleElectron_Run2016B_PromptReco_v2, SingleMuon_Run2016B_PromptReco_v2, SinglePhoton_Run2016B_PromptReco_v2, DoubleEG_Run2016B_PromptReco_v2, MuonEG_Run2016B_PromptReco_v2, DoubleMuon_Run2016B_PromptReco_v2]
dataSamples_Run2016B_PromptV2_forQCD = [JetHT_Run2016B_PromptReco_v2, MET_Run2016B_PromptReco_v2, SingleElectron_Run2016B_PromptReco_v2]

# runC
dataSamples_Run2016C_PromptV2 = [JetHT_Run2016C_PromptReco_v2, HTMHT_Run2016C_PromptReco_v2, MET_Run2016C_PromptReco_v2, SingleElectron_Run2016C_PromptReco_v2, SingleMuon_Run2016C_PromptReco_v2, SinglePhoton_Run2016C_PromptReco_v2, DoubleEG_Run2016C_PromptReco_v2, MuonEG_Run2016C_PromptReco_v2, DoubleMuon_Run2016C_PromptReco_v2]
dataSamples_Run2016C_PromptV2_forQCD = [JetHT_Run2016C_PromptReco_v2, MET_Run2016C_PromptReco_v2, SingleElectron_Run2016C_PromptReco_v2]

# runD
dataSamples_Run2016D_PromptV2 = [JetHT_Run2016D_PromptReco_v2, HTMHT_Run2016D_PromptReco_v2, MET_Run2016D_PromptReco_v2, SingleElectron_Run2016D_PromptReco_v2, SingleMuon_Run2016D_PromptReco_v2, SinglePhoton_Run2016D_PromptReco_v2, DoubleEG_Run2016D_PromptReco_v2, MuonEG_Run2016D_PromptReco_v2, DoubleMuon_Run2016D_PromptReco_v2]
dataSamples_Run2016D_PromptV2_forQCD = [JetHT_Run2016D_PromptReco_v2, MET_Run2016D_PromptReco_v2, SingleElectron_Run2016D_PromptReco_v2]

# runE
dataSamples_Run2016E_PromptV2 = [JetHT_Run2016E_PromptReco_v2, HTMHT_Run2016E_PromptReco_v2, MET_Run2016E_PromptReco_v2, SingleElectron_Run2016E_PromptReco_v2, SingleMuon_Run2016E_PromptReco_v2, SinglePhoton_Run2016E_PromptReco_v2, DoubleEG_Run2016E_PromptReco_v2, MuonEG_Run2016E_PromptReco_v2, DoubleMuon_Run2016E_PromptReco_v2]
dataSamples_Run2016E_PromptV2_forQCD = [JetHT_Run2016E_PromptReco_v2, MET_Run2016E_PromptReco_v2, SingleElectron_Run2016E_PromptReco_v2]

# runF
dataSamples_Run2016F_PromptV1 = [JetHT_Run2016F_PromptReco_v1, HTMHT_Run2016F_PromptReco_v1, MET_Run2016F_PromptReco_v1, SingleElectron_Run2016F_PromptReco_v1, SingleMuon_Run2016F_PromptReco_v1, SinglePhoton_Run2016F_PromptReco_v1, DoubleEG_Run2016F_PromptReco_v1, MuonEG_Run2016F_PromptReco_v1, DoubleMuon_Run2016F_PromptReco_v1]
dataSamples_Run2016F_PromptV1_forQCD = [JetHT_Run2016F_PromptReco_v1, MET_Run2016F_PromptReco_v1, SingleElectron_Run2016F_PromptReco_v1]

# runG
dataSamples_Run2016G_PromptV1 = [JetHT_Run2016G_PromptReco_v1, HTMHT_Run2016G_PromptReco_v1, MET_Run2016G_PromptReco_v1, SingleElectron_Run2016G_PromptReco_v1, SingleMuon_Run2016G_PromptReco_v1, SinglePhoton_Run2016G_PromptReco_v1, DoubleEG_Run2016G_PromptReco_v1, MuonEG_Run2016G_PromptReco_v1, DoubleMuon_Run2016G_PromptReco_v1]
dataSamples_Run2016G_PromptV1_forQCD = [JetHT_Run2016G_PromptReco_v1, MET_Run2016G_PromptReco_v1, SingleElectron_Run2016G_PromptReco_v1]

# runH (v3 adds little lumi to v2, v1 has nothing)
dataSamples_Run2016H_PromptV2 = [JetHT_Run2016H_PromptReco_v2, HTMHT_Run2016H_PromptReco_v2, MET_Run2016H_PromptReco_v2, SingleElectron_Run2016H_PromptReco_v2, SingleMuon_Run2016H_PromptReco_v2, SinglePhoton_Run2016H_PromptReco_v2, DoubleEG_Run2016H_PromptReco_v2, MuonEG_Run2016H_PromptReco_v2, DoubleMuon_Run2016H_PromptReco_v2]
dataSamples_Run2016H_PromptV2_forQCD = [JetHT_Run2016H_PromptReco_v2, MET_Run2016H_PromptReco_v2, SingleElectron_Run2016H_PromptReco_v2]
dataSamples_Run2016H_PromptV3 = [JetHT_Run2016H_PromptReco_v3, HTMHT_Run2016H_PromptReco_v3, MET_Run2016H_PromptReco_v3, SingleElectron_Run2016H_PromptReco_v3, SingleMuon_Run2016H_PromptReco_v3, SinglePhoton_Run2016H_PromptReco_v3, DoubleEG_Run2016H_PromptReco_v3, MuonEG_Run2016H_PromptReco_v3, DoubleMuon_Run2016H_PromptReco_v3]
dataSamples_Run2016H_PromptV3_forQCD = [JetHT_Run2016H_PromptReco_v3, MET_Run2016H_PromptReco_v3, SingleElectron_Run2016H_PromptReco_v3]

# ReRecoed data
# runB re-reco have either v1 or v2, and all have v3. They include exclusive run range so both must be merged
dataSamples_Run2016B_ReReco23Sep_V12 = [JetHT_Run2016B_23Sep2016_v1, HTMHT_Run2016B_23Sep2016_v1, MET_Run2016B_23Sep2016_v2, SingleElectron_Run2016B_23Sep2016_v2, SingleMuon_Run2016B_23Sep2016_v1, SinglePhoton_Run2016B_23Sep2016_v1, DoubleEG_Run2016B_23Sep2016_v2, MuonEG_Run2016B_23Sep2016_v2, DoubleMuon_Run2016B_23Sep2016_v1]
dataSamples_Run2016B_ReReco23Sep_V12_forQCD = [JetHT_Run2016B_23Sep2016_v1, MET_Run2016B_23Sep2016_v2, SingleElectron_Run2016B_23Sep2016_v2]
dataSamples_Run2016B_ReReco23Sep_V3 = [JetHT_Run2016B_23Sep2016_v3, HTMHT_Run2016B_23Sep2016_v3, MET_Run2016B_23Sep2016_v3, SingleElectron_Run2016B_23Sep2016_v3, SingleMuon_Run2016B_23Sep2016_v3, SinglePhoton_Run2016B_23Sep2016_v3, DoubleEG_Run2016B_23Sep2016_v3, MuonEG_Run2016B_23Sep2016_v3, DoubleMuon_Run2016B_23Sep2016_v3]
dataSamples_Run2016B_ReReco23Sep_V3_forQCD = [JetHT_Run2016B_23Sep2016_v3, MET_Run2016B_23Sep2016_v3, SingleElectron_Run2016B_23Sep2016_v3]

# runC
dataSamples_Run2016C_ReReco23Sep = [JetHT_Run2016C_23Sep2016_v1, HTMHT_Run2016C_23Sep2016_v1, MET_Run2016C_23Sep2016_v1, SingleElectron_Run2016C_23Sep2016_v1, SingleMuon_Run2016C_23Sep2016_v1, SinglePhoton_Run2016C_23Sep2016_v1, DoubleEG_Run2016C_23Sep2016_v1, MuonEG_Run2016C_23Sep2016_v1, DoubleMuon_Run2016C_23Sep2016_v1]
dataSamples_Run2016C_ReReco23Sep_forQCD = [JetHT_Run2016C_23Sep2016_v1, MET_Run2016C_23Sep2016_v1, SingleElectron_Run2016C_23Sep2016_v1]

# runD
dataSamples_Run2016D_ReReco23Sep = [JetHT_Run2016D_23Sep2016_v1, HTMHT_Run2016D_23Sep2016_v1, MET_Run2016D_23Sep2016_v1, SingleElectron_Run2016D_23Sep2016_v1, SingleMuon_Run2016D_23Sep2016_v1, SinglePhoton_Run2016D_23Sep2016_v1, DoubleEG_Run2016D_23Sep2016_v1, MuonEG_Run2016D_23Sep2016_v1, DoubleMuon_Run2016D_23Sep2016_v1]
dataSamples_Run2016D_ReReco23Sep_forQCD = [JetHT_Run2016D_23Sep2016_v1, MET_Run2016D_23Sep2016_v1, SingleElectron_Run2016D_23Sep2016_v1]

# runE
dataSamples_Run2016E_ReReco23Sep = [JetHT_Run2016E_23Sep2016_v1, HTMHT_Run2016E_23Sep2016_v1, MET_Run2016E_23Sep2016_v1, SingleElectron_Run2016E_23Sep2016_v1, SingleMuon_Run2016E_23Sep2016_v1, SinglePhoton_Run2016E_23Sep2016_v1, DoubleEG_Run2016E_23Sep2016_v1, MuonEG_Run2016E_23Sep2016_v1, DoubleMuon_Run2016E_23Sep2016_v1]
dataSamples_Run2016E_ReReco23Sep_forQCD = [JetHT_Run2016E_23Sep2016_v1, MET_Run2016E_23Sep2016_v1, SingleElectron_Run2016E_23Sep2016_v1]

# runF
dataSamples_Run2016F_ReReco23Sep = [JetHT_Run2016F_23Sep2016_v1, HTMHT_Run2016F_23Sep2016_v1, MET_Run2016F_23Sep2016_v1, SingleElectron_Run2016F_23Sep2016_v1, SingleMuon_Run2016F_23Sep2016_v1, SinglePhoton_Run2016F_23Sep2016_v1, DoubleEG_Run2016F_23Sep2016_v1, MuonEG_Run2016F_23Sep2016_v1, DoubleMuon_Run2016F_23Sep2016_v1]
dataSamples_Run2016F_ReReco23Sep_forQCD = [JetHT_Run2016F_23Sep2016_v1, MET_Run2016F_23Sep2016_v1, SingleElectron_Run2016F_23Sep2016_v1]

# runG
dataSamples_Run2016G_ReReco23Sep = [JetHT_Run2016G_23Sep2016_v1, HTMHT_Run2016G_23Sep2016_v2, MET_Run2016G_23Sep2016_v1, SingleElectron_Run2016G_23Sep2016_v1, SingleMuon_Run2016G_23Sep2016_v1, SinglePhoton_Run2016G_23Sep2016_v1, DoubleEG_Run2016G_23Sep2016_v1, MuonEG_Run2016G_23Sep2016_v1, DoubleMuon_Run2016G_23Sep2016_v1]
dataSamples_Run2016G_ReReco23Sep_forQCD = [JetHT_Run2016G_23Sep2016_v1, MET_Run2016G_23Sep2016_v1, SingleElectron_Run2016G_23Sep2016_v1]


### ----------------------------- summary ----------------------------------------

dataSamplesB = dataSamples_Run2016B_PromptV1 + dataSamples_Run2016B_PromptV2 + dataSamples_Run2016B_PromptV2_forQCD
dataSamplesC = dataSamples_Run2016C_PromptV2 + dataSamples_Run2016C_PromptV2_forQCD
dataSamplesD = dataSamples_Run2016D_PromptV2 + dataSamples_Run2016D_PromptV2_forQCD
dataSamplesE = dataSamples_Run2016E_PromptV2 + dataSamples_Run2016E_PromptV2_forQCD
dataSamplesF = dataSamples_Run2016F_PromptV1 + dataSamples_Run2016F_PromptV1_forQCD
dataSamplesG = dataSamples_Run2016G_PromptV1 + dataSamples_Run2016G_PromptV1_forQCD
dataSamplesH = dataSamples_Run2016H_PromptV2 + dataSamples_Run2016H_PromptV3 + dataSamples_Run2016H_PromptV2_forQCD +dataSamples_Run2016H_PromptV3_forQCD
dataSamplesBrereco = dataSamples_Run2016B_ReReco23Sep_V12 + dataSamples_Run2016B_ReReco23Sep_V3 + dataSamples_Run2016B_ReReco23Sep_V12_forQCD + dataSamples_Run2016B_ReReco23Sep_V3_forQCD
dataSamplesCrereco = dataSamples_Run2016C_ReReco23Sep + dataSamples_Run2016C_ReReco23Sep_forQCD
dataSamplesDrereco = dataSamples_Run2016D_ReReco23Sep + dataSamples_Run2016D_ReReco23Sep_forQCD
dataSamplesErereco = dataSamples_Run2016E_ReReco23Sep + dataSamples_Run2016E_ReReco23Sep_forQCD
dataSamplesFrereco = dataSamples_Run2016F_ReReco23Sep + dataSamples_Run2016F_ReReco23Sep_forQCD
dataSamplesGrereco = dataSamples_Run2016G_ReReco23Sep + dataSamples_Run2016G_ReReco23Sep_forQCD
samples = dataSamplesB + dataSamplesC + dataSamplesD + dataSamplesE + dataSamplesF + dataSamplesG + dataSamplesH + dataSamplesBrereco + dataSamplesCrereco + dataSamplesDrereco + dataSamplesErereco + dataSamplesFrereco + dataSamplesGrereco

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

for comp in samples:
    comp.splitFactor = 2000
#    comp.splitFactor = 400
    comp.isMC = False
    comp.isData = True

if __name__ == "__main__":
   import sys
   if "test" in sys.argv:
       from CMGTools.RootTools.samples.ComponentCreator import testSamples
       testSamples(samples)
