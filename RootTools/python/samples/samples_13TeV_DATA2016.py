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

run_range = (275377 , 276097)
#label = "_runs%s_%s"%(run_range[0], run_range[1])
JetHT_Run2016C_PromptReco_v2          = kreator.makeDataComponent("JetHT_Run2016C_PromptReco_v2"         , "/JetHT/Run2016C-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json, run_range)
HTMHT_Run2016C_PromptReco_v2          = kreator.makeDataComponent("HTMHT_Run2016C_PromptReco_v2"         , "/HTMHT/Run2016C-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json, run_range)
MET_Run2016C_PromptReco_v2            = kreator.makeDataComponent("MET_Run2016C_PromptReco_v2"           , "/MET/Run2016C-PromptReco-v2/MINIAOD"           , "CMS", ".*root", json, run_range)
SingleElectron_Run2016C_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016C_PromptReco_v2", "/SingleElectron/Run2016C-PromptReco-v2/MINIAOD", "CMS", ".*root", json, run_range)
SingleMuon_Run2016C_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016C_PromptReco_v2"    , "/SingleMuon/Run2016C-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, run_range)
SinglePhoton_Run2016C_PromptReco_v2   = kreator.makeDataComponent("SinglePhoton_Run2016C_PromptReco_v2"  , "/SinglePhoton/Run2016C-PromptReco-v2/MINIAOD"  , "CMS", ".*root", json, run_range)
DoubleEG_Run2016C_PromptReco_v2       = kreator.makeDataComponent("DoubleEG_Run2016C_PromptReco_v2"      , "/DoubleEG/Run2016C-PromptReco-v2/MINIAOD"      , "CMS", ".*root", json, run_range)
MuonEG_Run2016C_PromptReco_v2         = kreator.makeDataComponent("MuonEG_Run2016C_PromptReco_v2"        , "/MuonEG/Run2016C-PromptReco-v2/MINIAOD"        , "CMS", ".*root", json, run_range)
DoubleMuon_Run2016C_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016C_PromptReco_v2"    , "/DoubleMuon/Run2016C-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, run_range)



dataSamples_Run2016B_PromptV1 = [JetHT_Run2016B_PromptReco_v1, HTMHT_Run2016B_PromptReco_v1, MET_Run2016B_PromptReco_v1, SingleElectron_Run2016B_PromptReco_v1, SingleMuon_Run2016B_PromptReco_v1, SinglePhoton_Run2016B_PromptReco_v1, DoubleEG_Run2016B_PromptReco_v1, MuonEG_Run2016B_PromptReco_v1, DoubleMuon_Run2016B_PromptReco_v1] 


dataSamples_Run2016B_PromptV2 = [JetHT_Run2016B_PromptReco_v2, HTMHT_Run2016B_PromptReco_v2, MET_Run2016B_PromptReco_v2, SingleElectron_Run2016B_PromptReco_v2, SingleMuon_Run2016B_PromptReco_v2, SinglePhoton_Run2016B_PromptReco_v2, DoubleEG_Run2016B_PromptReco_v2, MuonEG_Run2016B_PromptReco_v2, DoubleMuon_Run2016B_PromptReco_v2]

dataSamples_Run2016B_PromptV2_forQCD = [JetHT_Run2016B_PromptReco_v2, MET_Run2016B_PromptReco_v2, SingleElectron_Run2016B_PromptReco_v2]


dataSamples_Run2016C_PromptV2 = [JetHT_Run2016C_PromptReco_v2, HTMHT_Run2016C_PromptReco_v2, MET_Run2016C_PromptReco_v2, SingleElectron_Run2016C_PromptReco_v2, SingleMuon_Run2016C_PromptReco_v2, SinglePhoton_Run2016C_PromptReco_v2, DoubleEG_Run2016C_PromptReco_v2, MuonEG_Run2016C_PromptReco_v2, DoubleMuon_Run2016C_PromptReco_v2]

dataSamples_Run2016C_PromptV2_forQCD = [JetHT_Run2016C_PromptReco_v2, MET_Run2016C_PromptReco_v2, SingleElectron_Run2016C_PromptReco_v2]



### ----------------------------- summary ----------------------------------------

dataSamplesB = dataSamples_Run2016B_PromptV1 + dataSamples_Run2016B_PromptV2 + dataSamples_Run2016B_PromptV2_forQCD
dataSamplesC = dataSamples_Run2016C_PromptV2 + dataSamples_Run2016C_PromptV2_forQCD
samples = dataSamplesB + dataSamplesC

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

for comp in samples:
    comp.splitFactor = 1000
#    comp.splitFactor = 400
    comp.isMC = False
    comp.isData = True

if __name__ == "__main__":
   import sys
   if "test" in sys.argv:
       from CMGTools.RootTools.samples.ComponentCreator import testSamples
       testSamples(samples)
