import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### ----------------------------- Zero Tesla run  ----------------------------------------

dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"  # use environmental variable, useful for instance to run on CRAB
json_prompt='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
json='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'


run_range = (273158, 284044)
label = "_runs%s_%s"%(run_range[0], run_range[1])


DoubleEG_Run2017A_PromptReco_v2 = kreator.makeDataComponent("DoubleEG_Run2017A_PromptReco_v2", "/DoubleEG/Run2017A-PromptReco-v2/MINIAOD", "CMS", ".*root", json_prompt )
DoubleEG_Run2017A_PromptReco_v3 = kreator.makeDataComponent("DoubleEG_Run2017A_PromptReco_v3", "/DoubleEG/Run2017A-PromptReco-v3/MINIAOD", "CMS", ".*root", json_prompt )
DoubleEG_Run2017B_PromptReco_v1 = kreator.makeDataComponent("DoubleEG_Run2017B_PromptReco_v1", "/DoubleEG/Run2017B-PromptReco-v1/MINIAOD", "CMS", ".*root", json_prompt )
DoubleEG_Run2017B_PromptReco_v2 = kreator.makeDataComponent("DoubleEG_Run2017B_PromptReco_v2", "/DoubleEG/Run2017B-PromptReco-v2/MINIAOD", "CMS", ".*root", json_prompt )
DoubleEG_Run2017C_PromptReco_v1 = kreator.makeDataComponent("DoubleEG_Run2017C_PromptReco_v1", "/DoubleEG/Run2017C-PromptReco-v1/MINIAOD", "CMS", ".*root", json_prompt )
DoubleEG_Run2017C_PromptReco_v2 = kreator.makeDataComponent("DoubleEG_Run2017C_PromptReco_v2", "/DoubleEG/Run2017C-PromptReco-v2/MINIAOD", "CMS", ".*root", json_prompt )
DoubleEG_Run2017C_PromptReco_v3 = kreator.makeDataComponent("DoubleEG_Run2017C_PromptReco_v3", "/DoubleEG/Run2017C-PromptReco-v3/MINIAOD", "CMS", ".*root", json_prompt )
DoubleEG_Run2017D_PromptReco_v1 = kreator.makeDataComponent("DoubleEG_Run2017D_PromptReco_v1", "/DoubleEG/Run2017D-PromptReco-v1/MINIAOD", "CMS", ".*root", json_prompt )
DoubleEG_Run2017E_PromptReco_v1 = kreator.makeDataComponent("DoubleEG_Run2017E_PromptReco_v1", "/DoubleEG/Run2017E-PromptReco-v1/MINIAOD", "CMS", ".*root", json_prompt )
DoubleEG_Run2017F_PromptReco_v1 = kreator.makeDataComponent("DoubleEG_Run2017F_PromptReco_v1", "/DoubleEG/Run2017F-PromptReco-v1/MINIAOD", "CMS", ".*root", json_prompt )



dataSamples_Run2017_DoubleEG_promptReco = [ DoubleEG_Run2017A_PromptReco_v2, DoubleEG_Run2017A_PromptReco_v3, DoubleEG_Run2017B_PromptReco_v1, DoubleEG_Run2017B_PromptReco_v2, DoubleEG_Run2017C_PromptReco_v1, DoubleEG_Run2017C_PromptReco_v2, DoubleEG_Run2017C_PromptReco_v3, DoubleEG_Run2017D_PromptReco_v1, DoubleEG_Run2017E_PromptReco_v1, DoubleEG_Run2017F_PromptReco_v1 ]

samples = dataSamples_Run2017_DoubleEG_promptReco


DoubleEG_Run2017B_17Nov2017_v1 = kreator.makeDataComponent("DoubleEG_Run2017B_17Nov2017_v1", "/DoubleEG/Run2017B-17Nov2017-v1/MINIAOD", "CMS", ".*root", json )
DoubleEG_Run2017C_17Nov2017_v1 = kreator.makeDataComponent("DoubleEG_Run2017C_17Nov2017_v1", "/DoubleEG/Run2017C-17Nov2017-v1/MINIAOD", "CMS", ".*root", json )
DoubleEG_Run2017D_17Nov2017_v1 = kreator.makeDataComponent("DoubleEG_Run2017D_17Nov2017_v1", "/DoubleEG/Run2017D-17Nov2017-v1/MINIAOD", "CMS", ".*root", json )
DoubleEG_Run2017E_17Nov2017_v1 = kreator.makeDataComponent("DoubleEG_Run2017E_17Nov2017_v1", "/DoubleEG/Run2017E-17Nov2017-v1/MINIAOD", "CMS", ".*root", json )
DoubleEG_Run2017F_17Nov2017_v1 = kreator.makeDataComponent("DoubleEG_Run2017F_17Nov2017_v1", "/DoubleEG/Run2017F-17Nov2017-v1/MINIAOD", "CMS", ".*root", json )


dataSamples_Run2017_DoubleEG_reReco = [ DoubleEG_Run2017A_PromptReco_v2, DoubleEG_Run2017A_PromptReco_v3, DoubleEG_Run2017B_17Nov2017_v1, DoubleEG_Run2017C_17Nov2017_v1, DoubleEG_Run2017D_17Nov2017_v1, DoubleEG_Run2017E_17Nov2017_v1, DoubleEG_Run2017F_17Nov2017_v1 ]

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

for comp in samples:
    comp.splitFactor = 1000
    comp.isMC = False
    comp.isData = True

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples)
