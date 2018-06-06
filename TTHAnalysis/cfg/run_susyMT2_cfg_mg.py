import PhysicsTools.HeppyCore.framework.config as cfg

# Comment this line if you want the diagnostic folders produced along with the output root file
cfg.Analyzer.nosubdir = True

##------------------------------------------
##  Options from command line
##------------------------------------------
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
# rule: boolean options are all false by default, you activate only those you need
# example: heppy testdata_94X run_susyMT2_cfg_mg.py -o doLocal -o doData -o year="2017" -N 1000 -p 0
doFull = bool(getHeppyOption('doFull',False)) # false when running full productions
doLocal = bool(getHeppyOption('doLocal',False))
doData = bool(getHeppyOption('doData',False))
doMC = bool(getHeppyOption('doMC',False))
doSig = bool(getHeppyOption('doSig',False))
isForQCD = bool(getHeppyOption('isForQCD', False))
year = str(getHeppyOption('year', "2017")) # year of data taking




##------------------------------------------
##  Load all modules and override standards if needed
##------------------------------------------

## NB: all data 2016 recommendations are kept unchanged as Moriond 2017, will need to be updated at some point
## NB: all implemented data 2017 recommendations do not take into account possible changes in the code of lepAna, ecc...


##------------------------------------------
## SUSY-specific modules
##------------------------------------------
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

#JSON
jsonAna.useLumiBlocks = True

#Vertex
vertexAna.keepFailingEvents = True # keep events with no good vertices

#Lepton
lepAna.loose_muon_dxy = 0.2
lepAna.loose_muon_dz  = 0.5
lepAna.loose_muon_relIso  = 0.15
lepAna.loose_muon_isoCut = lambda muon : muon.miniRelIso < 0.2

lepAna.loose_electron_pt  = 5
lepAna.loose_electron_eta    = 2.4
lepAna.loose_electron_relIso = 0.15
lepAna.loose_electron_isoCut = lambda electron : electron.miniRelIso < 0.1

lepAna.loose_electron_id  = 'POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto' # this seems outdated, yet it's what was used for Moriond 2017
if year=='2017': lepAna.loose_electron_id  = 'POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto' # DON'T KNOW WHAT DEFINITION TO USE
lepAna.loose_electron_lostHits = 999. # no cut
lepAna.loose_electron_dxy    = 999.
lepAna.loose_electron_dz     = 999.

lepAna.inclusive_electron_id  = 'POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto' # this seems outdated, yet it's what was used for Moriond 2017
if year=='2017': lepAna.inclusive_electron_id  = 'POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto' # DON'T KNOW WHAT DEFINITION TO USE
lepAna.inclusive_electron_lostHits = 999. # no cut since embedded in ID
lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID

lepAna.mu_isoCorr = 'deltaBeta'
lepAna.ele_isoCorr = 'deltaBeta'
lepAna.ele_tightId = 'POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto' # not really used apparently (?)
lepAna.notCleaningElectrons = True
lepAna.doMiniIsolation = True
lepAna.miniIsolationPUCorr = 'rhoArea'

lepAna.ele_effectiveAreas = 'Spring15_25ns_v1'
lepAna.mu_effectiveAreas = 'Spring15_25ns_v1'
if year == '2017':
  lepAna.mu_effectiveAreas = 'Fall17'  #new susyCore default
  lepAna.ele_effectiveAreas = 'Fall17' #new susyCore default

lepAna.rhoMuon= 'fixedGridRhoFastjetCentralNeutral',
lepAna.rhoElectron = 'fixedGridRhoFastjetCentralNeutral',
if year == '2017':
  lepAna.rhoElectron = 'fixedGridRhoFastjetAll' # new susyCore default
  lepAna.rhoMuon = 'fixedGridRhoFastjetAll' # new susyCore default

lepAna.doIsoAnnulus = True


# JET
mcGT={}
mcGT['2016']='Summer16_25nsV5_MC'     # newer recommendation 'Summer16_23Sep2016V4_MC'
mcGT['2017']='Fall17_17Nov2017_V6_MC'

dataGT={}
dataGT['2016']=[ [ -1, 'Spring16_23Sep2016BCDV2_DATA'], [276811 ,'Spring16_23Sep2016EFV2_DATA'] , [278802 ,'Spring16_23Sep2016GV2_DATA'] , [ 280385  ,'Spring16_23Sep2016HV2_DATA']  ]
# newer recommendation dataGT['2016']=[ [ -1, 'Summer16_23Sep2016BCDV4_DATA'], [276811 ,'Summer16_23Sep2016EFV4_DATA'] , [278802 ,'Summer16_23Sep2016GV4_DATA'] , [ 280385  ,'Summer16_23Sep2016HV4_DATA']  ]
dataGT['2017']=[ [ -1, 'Fall17_17Nov2017B_V6_DATA'], [299337 ,'Fall17_17Nov2017C_V6_DATA'] , [302030 ,'Fall17_17Nov2017D_V6_DATA'] , [ 303435  ,'Fall17_17Nov2017E_V6_DATA'], [ 304911  ,'Fall17_17Nov2017F_V6_DATA']  ]

jetAna.relaxJetId = False
jetAna.doPuId = False #
jetAna.doQG = True
jetAna.jetEta = 4.7
jetAna.jetEtaCentral = 2.4
jetAna.jetPt = 20. #was 10
jetAna.mcGT = mcGT[year]
jetAna.dataGT = dataGT[year]
jetAna.recalibrateJets = True # True or False
jetAna.applyL2L3Residual = True # 'Data'
jetAna.calculateSeparateCorrections = True
jetAna.calculateType1METCorrection = True
jetAna.jetLepDR = 0.4
jetAna.smearJets = False
jetAna.jetGammaDR = 0.4
jetAna.cleanFromLepAndGammaSimultaneously = True
jetAna.jetGammaLepDR = 0.4
jetAna.minGammaPt = 20.
jetAna.gammaEtaCentral = 2.4
jetAna.cleanJetsFromFirstPhoton = True
jetAna.cleanJetsFromIsoTracks = False ## added for Dominick
jetAna.doJetCleaning = False
jetAna.shiftJEC = 0

# TAU
tauAna.inclusive_ptMin = 20.0
tauAna.inclusive_etaMax = 2.3
tauAna.inclusive_dxyMax = 99999.
tauAna.inclusive_dzMax = 99999.
tauAna.inclusive_vetoLeptons = False
tauAna.inclusive_vetoLeptonsPOG = False
#tauAna.inclusive_decayModeID = 'byLooseCombinedIsolationDeltaBetaCorr3Hits' # ignored if not set or ''

tauAna.loose_ptMin = 20.0
tauAna.loose_etaMax = 2.3
tauAna.loose_dxyMax = 99999.
tauAna.loose_dzMax = 99999.
tauAna.loose_vetoLeptons = False
tauAna.loose_vetoLeptonsPOG = False
#tauAna.loose_decayModeID = 'byLooseCombinedIsolationDeltaBetaCorr3Hits' # ignored if not set or ''

# Photon
photonAna.etaCentral = 2.5
photonAna.ptMin = 20
#photonAna.gammaID = 'POG_SPRING16_25ns_Loose_looseSieie_NoIso'
photonAna.gammaID = 'POG_SPRING15_50ns_Loose_looseSieie_NoIso' # this seems VERY outdated, yet it's what was used for Moriond 2017
photonAna.do_randomCone = True
photonAna.do_mc_match = True

# Isolated Track
isoTrackAna.setOff=False
isoTrackAna.doIsoAnnulus = True

# recalibrate MET
metAna.recalibrate = 'type1' # 'type1' or False
metAna.old74XMiniAODs = False # get right Raw MET on old 74X MiniAODs, outdated

# store all taus by default
genAna.allGenTaus = True

# ?
susyScanAna.doLHE = False


# Core Analyzer
# jet pt treshold for mt2 calculation
mt2JPt = 30.0
ttHCoreEventAna.mhtForBiasedDPhi = 'mhtJetXjvec'
ttHCoreEventAna.jetPt = mt2JPt

from PhysicsTools.Heppy.analyzers.gen.LHEAnalyzer import LHEAnalyzer
LHEAna = LHEAnalyzer.defaultConfig

from PhysicsTools.Heppy.analyzers.gen.TauDecayModeAnalyzer import TauDecayModeAnalyzer
TauDecayAna = TauDecayModeAnalyzer.defaultConfig


# TRIGGERS and Filters
import CMGTools.RootTools.samples.triggers_13TeV_DATA2016 as trg2016
import CMGTools.RootTools.samples.triggers_13TeV_DATA2017 as trg2017
#from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_photon75, triggers_photon90, triggers_photon120, triggers_photon75ps
#from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_photon90ps, triggers_photon120ps, triggers_photon155, triggers_photon165_HE10, triggers_photon175
#from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_doubleele33, triggers_mumu_noniso

#from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_met90_mht90, triggers_metNoMu90_mhtNoMu90, triggers_metNoMu120_mhtNoMu120, triggers_Jet80MET90


# default list, 2016
triggerFlagsAna.triggerBits = {
# signal triggers
'PFHT800' : ['HLT_PFHT800_v*'],
'PFHT900' : ['HLT_PFHT900_v*'],
'PFMET170' : ['HLT_PFMET170_NoiseCleaned_v*','HLT_PFMET170_NotCleaned_v*','HLT_PFMET170_HBHECleaned_v*','HLT_PFMET170_JetIdCleaned_v*'],
'PFHT300_PFMET100' : ['HLT_PFHT300_PFMET100_v*'],
'PFHT300_PFMET110' : ['HLT_PFHT300_PFMET110_v*'],
'PFHT350_PFMET100' : ['HLT_PFHT350_PFMET100_NoiseCleaned_v*','HLT_PFHT350_PFMET100_JetIdCleaned_v*','HLT_PFHT350_PFMET100_v*'],
'PFHT350_PFMET120' : ['HLT_PFHT350_PFMET120_NoiseCleaned_v*','HLT_PFHT350_PFMET120_JetIdCleaned_v*'],
'PFJet450' : ['HLT_PFJet450_v*'],
'PFJet500' : ['HLT_PFJet500_v*'],
#
# mono-jet signal triggers
'PFMETNoMu90_PFMHTNoMu90' : ['HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v*','HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v*','HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v*'],
'MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90' : ['HLT_MonoCentralPFJet80_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v*','HLT_MonoCentralPFJet80_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v*',
                                                'HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90_IDTight_v*'],
#
'PFMETNoMu100_PFMHTNoMu100' : ['HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_v*'],
'PFMETNoMu110_PFMHTNoMu110' : ['HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v*'],
'PFMETNoMu120_PFMHTNoMu120' : ['HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v*','HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v*','HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v*'],
'PFMET90_PFMHT90'           : ['HLT_PFMET90_PFMHT90_IDTight_v*','HLT_PFMET90_PFMHT90_IDLoose_v*'],
'PFMET100_PFMHT100'         : ['HLT_PFMET100_PFMHT100_IDTight_v*'],
'PFMET110_PFMHT110'         : ['HLT_PFMET110_PFMHT110_IDTight_v*'],
'PFMET120_PFMHT120'         : ['HLT_PFMET120_PFMHT120_IDTight_v*'],
#
# lepton triggers
'SingleMu'     : ['HLT_IsoMu27_v*', 'HLT_IsoTkMu27_v*','HLT_IsoMu17_eta2p1_v*','HLT_IsoMu20_v*','HLT_IsoMu20_eta2p1_v*','HLT_IsoTkMu20_v*','HLT_IsoTkMu20_eta2p1_v*','HLT_IsoMu24_v*','HLT_IsoTkMu24_v*'],
'SingleEl'     : ['HLT_Ele32_eta2p1_WPTight_Gsf_v*', 'HLT_Ele23_WPLoose_Gsf_v*','HLT_Ele22_eta2p1_WPLoose_Gsf_v*','HLT_Ele23_WP75_Gsf_v*','HLT_Ele22_eta2p1_WP75_Gsf_v*','HLT_Ele25_eta2p1_WPTight_Gsf_v*','HLT_Ele27_eta2p1_WPLoose_Gsf_v*','HLT_Ele27_eta2p1_WPTight_Gsf_v*'],
# MG correcetd 'DoubleEl'     : ['HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*','HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*'],
'DoubleEl'     : ['HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*'],
'DoubleEl33'   : ['HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v*','HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v*'],
'MuX_Ele12' : ['HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*','HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*','HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*'],
'Mu8_EleX' : ['HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*', 'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*','HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v*'],
'Mu33_Ele33_NonIso'  : ['HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL_v*'],
'Mu30_Ele30_NonIso'  : ['HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v*'],

'DoubleMu'     : ['HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*', 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*','HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*','HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v*','HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v*'],
'DoubleMu_NonIso'    : ['HLT_Mu40_TkMu11_v*','HLT_Mu30_TkMu11_v*'],
'SingleMu_NonIso'    : ['HLT_Mu55_v*', 'HLT_Mu50_v*','HLT_TkMu50_v*'],
'SingleEl_NonIso'    : ['HLT_Ele105_CaloIdVT_GsfTrkIdT_v*'],
# for single-photon control region
'Photon120' : ['HLT_Photon120_v*'],
'Photon165_HE10' : ['HLT_Photon165_HE10_v*'],
# photon backups
'Photon250_NoHE' : ['HLT_Photon250_NoHE_v*'],
'ECALHT800' : ['HLT_ECALHT800_v*'],

# for QCD control region
'PFHT125_Prescale'  : ['HLT_PFHT125_v*'],
'PFHT200_Prescale'  : ['HLT_PFHT200_v*'],
'PFHT300_Prescale'  : ['HLT_PFHT300_v*'],
'PFHT350_Prescale'  : ['HLT_PFHT350_v*'],
'PFHT475_Prescale'  : ['HLT_PFHT475_v*'],
'PFHT600_Prescale'  : ['HLT_PFHT600_v*'],

'DiCentralPFJet70_PFMET120'  : ['HLT_DiCentralPFJet70_PFMET120_NoiseCleaned_v*','HLT_DiCentralPFJet70_PFMET120_JetIdCleaned_v*'],
'DiCentralPFJet55_PFMET110'  : ['HLT_DiCentralPFJet55_PFMET110_NoiseCleaned_v*','HLT_DiCentralPFJet55_PFMET110_JetIdCleaned_v*'],

#Francesco's ??
'Photon75_R9Id90_HE10_IsoM' : trg2016.triggers_photon75,
'Photon90_R9Id90_HE10_IsoM' : trg2016.triggers_photon90,
'Photon120_R9Id90_HE10_IsoM' : trg2016.triggers_photon120,
'Photon75' : trg2016.triggers_photon75ps,
'Photon90' : trg2016.triggers_photon90ps,
'Photon155' : trg2016.triggers_photon155,
'Photon175' : trg2016.triggers_photon175,

## monojet triggers
#'PFMET90_PFMHT90' : triggers_met90_mht90,
#'PFMETNoMu90_PFMHTNoMu90' : triggers_metNoMu90_mhtNoMu90,
#'PFMETNoMu120_PFMHTNoMu120' : triggers_metNoMu120_mhtNoMu120,
#'MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90' : triggers_Jet80MET90,
# TODO: understand : these overwrite those above, why ?

### ZGamma triggers
'DoubleEle33' : ['HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v*'],
'Mu30_TkMu11' : ['HLT_Mu30_TkMu11_v*'],
}
# TODO: understand why the above should be needed ?

# add triggers that are needed for 2017 and not present in list above
if year == '2017':
  # additions of hadronic triggers
  triggerFlagsAna.triggerBits['PFHT1050'] = ['HLT_PFHT1050_v*']
  triggerFlagsAna.triggerBits['PFHT500_PFMET100_PFMHT100'] = ['HLT_PFHT500_PFMET100_PFMHT100_IDTight_v*']
  triggerFlagsAna.triggerBits['PFHT800_PFMET75_PFMHT75'] = ['HLT_PFHT800_PFMET75_PFMHT75_IDTight_v*']
  triggerFlagsAna.triggerBits['PFMETNoMu140_PFMHTNoMu140'] = ['HLT_PFMETNoMu140_PFMHTNoMu140_IDTight*']
  triggerFlagsAna.triggerBits['PFMET120_PFMHT120_PFHT60'] = ['HLT_PFMET120_PFMHT120_IDTight_PFHT60*']
  triggerFlagsAna.triggerBits['PFMETNoMu120_PFMHTNoMu120_PFHT60'] = ['HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60*']

 # TODO: add triggers for QCD control region

  # additions of leptonic / photonic triggers
  triggerFlagsAna.triggerBits['DoubleMu'].append('HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*')
  triggerFlagsAna.triggerBits['DoubleMu'].append('HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v*')
  triggerFlagsAna.triggerBits['DoubleMu_NonIso'].append('HLT_Mu37_TkMu27_v*')
  triggerFlagsAna.triggerBits['DoubleEl'].append('HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v*')
  triggerFlagsAna.triggerBits['DoubleEl33'].append('HLT_DoubleEle25_CaloIdL_MW_v*')
  triggerFlagsAna.triggerBits['DoubleEl33'].append('HLT_DoubleEle33_CaloIdL_MW_v*')

  triggerFlagsAna.triggerBits['Mu30_Ele30_NonIso'].append('HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v*')

  triggerFlagsAna.triggerBits['Photon200'] = ['HLT_Photon200_v*']

  #triggerFlagsAna.triggerBits['Mu27_Ele37_NonIso'] = ['HLT_Mu27_Ele37_CaloIdL_MW_v*']
  #triggerFlagsAna.triggerBits['Mu37_Ele27_NonIso'] = ['HLT_Mu37_Ele27_CaloIdL_MW_v*']


# Get full list of triggers. To be used later to filter events
allTriggers = []
for key,value in triggerFlagsAna.triggerBits.items():
    allTriggers = allTriggers + value
#print 'trigger list: %s' % (allTriggers)


##  FILTERS DEFINITION
#https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFiltersRun2
eventFlagsAna.triggerBits = {
# recommended filters for 80X
    'HBHENoiseFilter' : [ 'Flag_HBHENoiseFilter' ],
    'HBHENoiseIsoFilter' : [ 'Flag_HBHENoiseIsoFilter' ],
    'CSCTightHalo2015Filter' : [ 'Flag_CSCTightHalo2015Filter' ],
    'EcalDeadCellTriggerPrimitiveFilter' : [ 'Flag_EcalDeadCellTriggerPrimitiveFilter' ],
    'goodVertices' : [ 'Flag_goodVertices' ],
    'eeBadScFilter' : [ 'Flag_eeBadScFilter' ],
    # Halo filter to be used
    'globalTightHalo2016Filter' : [ 'Flag_globalTightHalo2016Filter' ],
}

if year == '2017':
  eventFlagsAna.triggerBits['BadPFMuonFilter'] = ['Flag_BadPFMuonFilter']
  eventFlagsAna.triggerBits['ecalBadCalibFilter'] = ['Flag_ecalBadCalibFilter']



##------------------------------------------
## MT2 modules
##------------------------------------------

from CMGTools.TTHAnalysis.analyzers.ttHMT2Control import ttHMT2Control



ttHMT2Control = cfg.Analyzer(
            ttHMT2Control, name = 'ttHMT2Control',
            jetPt = mt2JPt,
            )

##  NUMBER of ISR JETS
from CMGTools.TTHAnalysis.analyzers.ttHIsrJetAnalyzer import ttHIsrJetAnalyzer

ttHIsrJetAna = cfg.Analyzer(
            ttHIsrJetAnalyzer, name = 'ttHIsrJetAnalyzer',
            jetPt = mt2JPt,
            )

##  TOPOLOGICAL VARIABLES: minMT, MT2
from CMGTools.TTHAnalysis.analyzers.ttHTopoVarAnalyzer import ttHTopoVarAnalyzer

ttHTopoJetAna = cfg.Analyzer(
            ttHTopoVarAnalyzer, name = 'ttHTopoVarAnalyzer',
            doOnlyDefault = True,
            jetPt = mt2JPt,
            )

from PhysicsTools.Heppy.analyzers.eventtopology.MT2Analyzer import MT2Analyzer

MT2Ana = cfg.Analyzer(
    MT2Analyzer, name = 'MT2Analyzer',
    metCollection     = 'slimmedMETs',
    doOnlyDefault = True,
    jetPt = mt2JPt,
    collectionPostFix = '',
    )


##  MT2 skim
from CMGTools.TTHAnalysis.analyzers.MT2Skimmer import MT2Skimmer
# Tree Producer
MT2skim = cfg.Analyzer(
            MT2Skimmer, name='MT2Skimmer',
            )



##------------------------------------------
##  TREE PRODUCER
##------------------------------------------

from CMGTools.TTHAnalysis.analyzers.treeProducerSusyFullHad import *
from CMGTools.TTHAnalysis.analyzers.treeProducerMT2forQCDStudies import *
from CMGTools.TTHAnalysis.analyzers.treeProducerMT2forJECstudies import *

treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerSusyFullHad',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     PDFWeights = PDFWeights,
     globalVariables = susyFullHad_globalVariables, # simple variables, floats, ints, ...
     globalObjects = susyFullHad_globalObjects,
     collections = susyFullHad_collections, # collection of objects
     defaultFloatType = 'F',
     treename = 'mt2'
)


# ------------------------------------------------------------------------------------------- #
# Sequence
# ------------------------------------------------------------------------------------------- #

susyCoreSequence.insert(susyCoreSequence.index(skimAnalyzer),
                        susyCounter)

### Here we are moving the jet cleaning module so that the JEC corrections are already propagated
### to jets, met, and isoTracks
susyCoreSequence.remove(isoTrackAna)
susyCoreSequence.insert(susyCoreSequence.index(metAna)+1,isoTrackAna)
susyCoreSequence.insert(susyCoreSequence.index(isoTrackAna)+1,jetCleanAna)



sequence = cfg.Sequence(
    susyCoreSequence+[
    LHEAna,
    TauDecayAna,
    ttHMT2Control,
    MT2Ana,
    ttHTopoJetAna,
    ttHIsrJetAna,
    treeProducer,
    ])

# skim only the data for some reason - I find this quite stupid
if doData:
  sequence.insert(sequence.index(treeProducer), MT2skim)

###---- to switch off the compression
#treeProducer.isCompressed = 0

# ------------------------------------------------------------------------------------------- #
# Dataset components depending on the jobs you want to send
# ------------------------------------------------------------------------------------------- #

json = {}
json['2016'] = os.environ['CMSSW_BASE']+'/src/CMGTools/TTHAnalysis/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
json['2017'] = os.environ['CMSSW_BASE']+'/src/CMGTools/TTHAnalysis/data/json/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'

# TODO: send them to option
doSpecialSettingsForMECCA = 1 # set to 1 for comparisons with americans
runPreprocessor = False

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()
# ------------------------------------------------------------------------------------------- #
if doFull==False and doMC:
  if doLocal:
    dataset_nickname = 'WJetsToLNu_HT-800To1200'
    #local_files = ['SMS-T2qq__A_FILE.root']
    #local_files = ['ZJetsToNuNu_HT-800To1200_13TeV-madgraph_PU2017_12Apr2018_94X_mc2017_realistic_v14-v1__A_FILE.root']
    #local_files = ['ZJetsToNuNu_HT-800To1200_13TeV-madgraph_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v3__A_FILE.root']
    local_files = ['WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2__A_FILE.root']
    path='/scratch/mratti/MT2_test_samples/80X'
    comp = kreator.makePrivateMCComponent(name=dataset_nickname, dataset=path, files=local_files)
    selectedComponents = [comp]
  else:
    ZJetsToNuNu_HT800to1200 = kreator.makeMCComponent('ZJetsToNuNu_HT800to1200', '/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v3/MINIAODSIM', 'CMS', '.*root',1.474*1.23)
    WJetsToLNu_HT100to200 = kreator.makeMCComponent('WJetsToLNu_HT100to200', '/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v3/MINIAODSIM', 'CMS', '.*root',1345*1.21)
    selectedComponents = [ZJetsToNuNu_HT800to1200,WJetsToLNu_HT100to200]

    for comp in selectedComponents:
        comp.splitFactor = 1200
        comp.fineSplitFactor = 4 # to run two jobs per file
        #comp.files = comp.files[:1]
        #comp.files = comp.files[57:58]  # to process only file [57]
        #comp.triggers = triggers_HT900 + triggers_HTMET + triggers_photon155 + triggers_1mu_isolow + triggers_MT2_mumu + triggers_MT2_ee + triggers_MT2_mue # to apply trigger skimming
# ------------------------------------------------------------------------------------------- #
if doFull==False and doData and doLocal:
  dataset_nickname = 'testData'
  local_files = []
  if year == '2016': local_files.append('/scratch/mratti/MT2_test_samples/80X/Run2016B_HTMHT_MINIAOD_PromptReco-v2___A_FILE.root')
  elif year == '2017': local_files.append('/scratch/mratti/MT2_test_samples/94X/Run2017D_HTMHT_31Mar2018-v1__A_FILE.root')
  comp = kreator.makePrivateDataComponent(name=dataset_nickname, dataset='', files=local_files, json=json[year], xSec=1)
  comp.files=[local_files[0]]
  comp.json=json[year]
  comp.triggers = allTriggers # why here ?

  selectedComponents = [comp]
# ------------------------------------------------------------------------------------------- #
if doFull and doMC:
   #TODO: add full MC samples list and change indentation
  ZJetsToNuNu_HT800to1200 = kreator.makeMCComponent('ZJetsToNuNu_HT800to1200', '/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v3/MINIAODSIM', 'CMS', '.*root',1.474*1.23)
  WJetsToLNu_HT100to200 = kreator.makeMCComponent('WJetsToLNu_HT100to200', '/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v3/MINIAODSIM', 'CMS', '.*root',1345*1.21)
  selectedComponents = [
        ZJetsToNuNu_HT800to1200,
        WJetsToLNu_HT100to200
        ]
  for comp in selectedComponents:
    comp.splitFactor = 1200
    comp.fineSplitFactor = 4 # to run two jobs per file
    comp.files = comp.files[:]
    #comp.files = comp.files[:1]
    #comp.files = comp.files[57:58]  # to process only file [57]
    # triggers on MC
    #comp.triggers = triggers_HT900 + triggers_HTMET + triggers_photon155 + triggers_1mu_isolow + triggers_MT2_mumu + triggers_MT2_ee + triggers_MT2_mue # to apply trigger skimming
# ------------------------------------------------------------------------------------------- #
if doFull and doData:
  selectedComponents = []
  if year== '2016':
    from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import *
    selectedComponents = dataSamples_23Sep2016PlusPrompt
    # TODO: get the right samples for 2016
  if year == '2017':
    from CMGTools.RootTools.samples.samples_13TeV_DATA2017 import dataSamples_31Mar2018
    selectedComponents = dataSamples_31Mar2018

  for comp in selectedComponents:
    comp.json=json[year]
    comp.triggers = allTriggers

  #if not isForQCD:
  #  sequence.insert(sequence.index(treeProducer), MT2skim)
# ------------------------------------------------------------------------------------------- #
if doFull and doSig:
    jetAna.mcGT     = 'Spring16_FastSimV1_MC' # jec corrections for FastSim V1### 25
    jetAna.applyL2L3Residual = False # 'Data'
    jetAna.do_mc_match = True
    jetAna.relaxJetId = True
    jetCleanAna.relaxJetId = True

#    from CMGTools.RootTools.samples.samples_13TeV_signals import *
    ew_samples = {}
    ew_samples['SMS_T2qq'] = '/SMS-T2qq_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM'
    #ew_samples['TChiWZ_genHT-160_genMET'] = '/TChiWZ_genHT-160_genMET-80_3points_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
    #ew_samples['SMS-N2C1-higgsino_genHT-160_genMET-80'] = '/SMS-N2C1-higgsino_genHT-160_genMET-80_3points_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
    #ew_samples['SMS-N2N1-higgsino_genHT-160_genMET-80'] = '/SMS-N2N1-higgsino_genHT-160_genMET-80_3points_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
    #ew_samples['SMS-C1C1-higgsino_genHT-160_genMET-80'] = '/SMS-C1C1-higgsino_genHT-160_genMET-80_3points_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
    #ew_samples['SMS-C1N1-higgsino_genHT-160_genMET-80'] = '/SMS-C1N1-higgsino_genHT-160_genMET-80_3points_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
    #ew_samples['MSSM-higgsino_genHT-160_genMET-80'] = '/MSSM-higgsino_genHT-160_genMET-80_3points_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'

    selectedComponents = []
    for nick_name,sample_name in ew_samples.items():
      comp = kreator.makeMCComponent(nick_name, sample_name, 'CMS', '.*root',1)
      selectedComponents.append(comp)

    # test all components (1 thread per component).
    for comp in selectedComponents:
        comp.splitFactor = 1200
        comp.fineSplitFactor = 4 # to run 4 jobs per file
        comp.files = comp.files[:]
        # triggers on MC
        #comp.triggers = triggers_HT900 + triggers_HTMET + triggers_photon155 + triggers_1mu_isolow + triggers_MT2_mumu + triggers_MT2_ee + triggers_MT2_mue # to apply trigger skimming

# -------------------------------------------------------------------------------------------
if doSpecialSettingsForMECCA:
    jetAna.doQG = False
    # photonAna.do_randomCone = False
    # Below slow things note: it will in any case try it only on MC, not on data
    # photonAna.do_mc_match = False
    # jetAna.do_mc_match = False
    lepAna.do_mc_match = False
    isoTrackAna.do_mc_match = False
    ###genAna.makeLHEweights = False ### Such option does not exist (anymore)

# ------------------------------------------------------------------------------------------- #
# Actually Run the whole thing
# ------------------------------------------------------------------------------------------- #

from PhysicsTools.HeppyCore.framework.services.tfile import TFileService
output_service = cfg.Service(
      TFileService,
      'outputfile',
      name='outputfile',
      fname='mt2.root',
      option='recreate'
    )


from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [output_service],
                     events_class = Events)


#    # Tree configuration for JEC variations
#    if jetAna.shiftJEC > 0.5 or jetAna.shiftJEC < -0.5:
#        treeProducer.globalVariables = MT2forJECstudies_globalVariables
#        treeProducer.globalObjects = MT2forJECstudies_globalObjects
#        treeProducer.collections = MT2forJECstudies_collections
