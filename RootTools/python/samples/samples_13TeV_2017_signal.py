import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### ----------------------------- mix of Spring16 and Summer16 ----------------------------------------



SMS_TChiWH_HToGG_mChargino300_mLSP1 = kreator.makeMCComponent("SMS_TChiWH_HToGG_mChargino300_mLSP1", "/SMS_TChiWH_HToGG_mChargino300_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 0.0141903)

#SMS_T1bbbb_mGluino1500_mLSP100 = kreator.makeMCComponent("SMS_T1bbbb_mGluino1500_mLSP100", "/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/MINIAODSIM", "CMS", ".*root", 0.0141903)



SMS_TChiWH_HToGG=kreator.makeMCComponent("SMS_TChiWH_HToGG","/SMS-TChiWH_HToGG_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM", "CMS",".*root",1)

SMS_TChiHZ_HToGG=kreator.makeMCComponent("SMS_TChiHZ_HToGG","/SMS-TChiHZ_HToGG_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM", "CMS",".*root",1)

SMS_TChiHH_HToGG=kreator.makeMCComponent("SMS_TChiHH_HToGG","/SMS-TChiHH_HToGG_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM", "CMS",".*root",1)

SMS_T2bH_HToGG=kreator.makeMCComponent("SMS_T2bH_HToGG","/SMS-T2bH_HToGG_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM", "CMS",".*root",1)

#missing points from the scans
SMS_TChiWH_HToGG_175=kreator.makeMCComponent("SMS_TChiWH_HToGG_175","/SMS-TChiWH_HToGG_mChargino-175_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM", "CMS",".*root",1)

SMS_T2bH_HToGG_250=kreator.makeMCComponent("SMS_T2bH_HToGG_250","/SMS-T2bH_HToGG_mSbot-250_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM", "CMS",".*root",1)



SignalSUSY = [
SMS_TChiWH_HToGG_mChargino300_mLSP1,
]



### ----------------------------- summary ----------------------------------------


signalSamples = SignalSUSY

samples = signalSamples

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

#Define splitting
for comp in signalSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 250 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012

if __name__ == "__main__":
   import sys
   if "test" in sys.argv:
       from CMGTools.RootTools.samples.ComponentCreator import testSamples
       testSamples(samples)
