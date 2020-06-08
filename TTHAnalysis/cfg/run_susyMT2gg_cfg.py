
import PhysicsTools.HeppyCore.framework.config as cfg


#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

# Comment this line if you want the diagnostic folders produced along with the output root file
cfg.Analyzer.nosubdir = True


# Load the producer module to build full 5x5 cluster shapes and whatever 
# else is needed for IDs
#from RecoEgamma.PhotonIdentification.PhotonIDValueMapProducer_cfi import *

# Load the producer for MVA IDs. Make sure it is also added to the sequence!
#from RecoEgamma.PhotonIdentification.PhotonMVAValueMapProducer_cfi import *

#and subsequently add these producers to the main sequence, like (order is important!)
#process.p = cms.Path(process.photonIDValueMapProducer * process.photonMVAValueMapProducer * process.myAnalyzer)






##------------------------------------------
## Redefine what I need
##------------------------------------------

### jet pt treshold for mt2 calculation
mt2JPt = 30.0

#JSON
jsonAna.useLumiBlocks = True

#Vertex
vertexAna.keepFailingEvents = True # keep events with no good vertices

#Lepton
lepAna.loose_muon_dxy = 0.2
lepAna.loose_muon_dz  = 0.5
lepAna.loose_muon_relIso  = 0.15
lepAna.loose_muon_isoCut = lambda muon :muon.miniRelIso < 0.2

lepAna.loose_electron_pt  = 5
lepAna.loose_electron_eta    = 2.4
lepAna.loose_electron_relIso = 0.15
lepAna.loose_electron_isoCut = lambda electron : electron.miniRelIso < 0.1

#lepAna.loose_electron_id  = "POG_Cuts_ID_SPRING16_25ns_v1_ConvVetoDxyDz_Veto"
#lepAna.loose_electron_id  = "POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto_full5x5"
#lepAna.loose_electron_id  = "POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto"
#lepAna.loose_electron_id  = "MVA_ID_NonTrig_Spring16_VLooseSI"
#lepAna.loose_electron_id  = "MVA_ID_NonTrig_94X_VLoose"
lepAna.loose_electron_id  = "POG_Cuts_ID_FALL17_94X_v2_ConvVetoDxyDz_Loose"
#lepAna.loose_electron_id  = "POG_Cuts_ID_FALL17_94X_v1_ConvVetoDxyDz_Loose"
lepAna.loose_electron_lostHits = 999. # no cut
lepAna.loose_electron_dxy    = 999.
lepAna.loose_electron_dz     = 999.


#lepAna.inclusive_electron_id  = "POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto_full5x5"
lepAna.inclusive_electron_id  = "POG_Cuts_ID_FALL17_94X_v2_ConvVetoDxyDz_Loose"
lepAna.inclusive_electron_lostHits = 999. # no cut since embedded in ID
lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID

lepAna.mu_isoCorr = "deltaBeta"
lepAna.ele_isoCorr = "deltaBeta"
lepAna.ele_tightId = "Cuts_FALL17_94X_v2_ConvVetoDxyDz"
lepAna.notCleaningElectrons = True
lepAna.doMiniIsolation = True
lepAna.miniIsolationPUCorr = 'rhoArea'
#lepAna.ele_effectiveAreas = 'Spring16_25ns_v1'             #new default 
#lepAna.mu_effectiveAreas = 'Spring16_25ns_v1'              #new default

lepAna.ele_effectiveAreas = 'Fall17'             #new default 
lepAna.mu_effectiveAreas = 'Fall17'              #new default
lepAna.rhoMuon= 'fixedGridRhoFastjetAll',      #new default
lepAna.rhoElectron = 'fixedGridRhoFastjetAll', #new default

#lepAna.rhoMuon= 'fixedGridRhoFastjetCentralNeutral',      #new default
#lepAna.rhoElectron = 'fixedGridRhoFastjetCentralNeutral', #new default
#lepAna.doIsoAnnulus = True
lepAna.doIsoAnnulus = False

#era="25ns"
#sync=False
#lepAna.doElectronScaleCorrections = {
#    'data' : 'EgammaAnalysis/ElectronTools/data/76X_16DecRereco<_2015',
#    'GBRForest': ('$CMSSW_BASE/src/CMGTools/RootTools/data/egamma_epComb_GBRForest_76X.root',
#                  'gedelectron_p4combination_'+era),
#    'isSync': sync
#    }
#
#
#smear="basic"
#lepAna.doMuonScaleCorrections = ( 'Kalman', {
#        'MC': 'MC_76X_13TeV',
#        'Data': 'DATA_76X_13TeV',
#        'isSync': sync,
#        'smearMode':smear
#        })


# JET (for event variables do apply the jetID and not PUID yet)
jetAna.relaxJetId = False
jetAna.doPuId = False
jetAna.doQG = True
jetAna.jetEta = 4.7
jetAna.jetEtaCentral = 2.4
jetAna.jetPt = 20. #was 10
#jetAna.mcGT     = "Spring16_25nsV6_MC" # jec corrections
#jetAna.dataGT   = "Spring16_25nsV6_DATA" # jec corrections

jetAna.mcGT="Fall17_17Nov2017_V32_MC"
jetAna.dataGT = [ [ -1, "Fall17_17Nov2017B_V32_DATA"], [299337 ,"Fall17_17Nov2017C_V32_DATA"] , [302030 ,"Fall17_17Nov2017DE_V32_DATA"] , [ 304911  ,"Fall17_17Nov2017F_V32_DATA"]  ]

# jetAna.mcGT="Fall17_17Nov2017_V6_MC"
# jetAna.dataGT = [ [ -1, "Fall17_17Nov2017B_V6_DATA"], [299337 ,"Fall17_17Nov2017C_V6_DATA"] , [302030 ,"Fall17_17Nov2017D_V6_DATA"] , [ 303435  ,"Fall17_17Nov2017E_V6_DATA"], [ 304911  ,"Fall17_17Nov2017F_V6_DATA"]  ]

# jetAna.recalibrateJets = False # False or False
# jetAna.applyL2L3Residual = False # 'Data'
# jetAna.calculateSeparateCorrections = False
# jetAna.calculateType1METCorrection = False

# #NOMINAL, go back to this change
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
#jetAna.cleanJetsFromFirstPhoton = True
jetAna.cleanJetsFromFirstPhoton = False
jetAna.cleanJetsFromIsoTracks = False ## added for Dominick
jetAna.doJetCleaning = False
#jetAna.alwaysCleanPhotons = True
jetAna.shiftJEC = 0

#For gamgam cleaning: done now directly for the gg_collection
#jetCleanAna.cleanJetsFromFirstPhoton = False, 


# TAU 
tauAna.inclusive_ptMin = 20.0
tauAna.inclusive_etaMax = 2.3
tauAna.inclusive_dxyMax = 99999.
tauAna.inclusive_dzMax = 99999.
tauAna.inclusive_vetoLeptons = False
tauAna.inclusive_vetoLeptonsPOG = False
#tauAna.inclusive_decayModeID = "byLooseCombinedIsolationDeltaBetaCorr3Hits" # ignored if not set or ""

tauAna.loose_ptMin = 20.0
tauAna.loose_etaMax = 2.3
tauAna.loose_dxyMax = 99999.
tauAna.loose_dzMax = 99999.
tauAna.loose_vetoLeptons = False
tauAna.loose_vetoLeptonsPOG = False
#tauAna.loose_decayModeID = "byLooseCombinedIsolationDeltaBetaCorr3Hits" # ignored if not set or ""

# Photon
photonAna.etaCentral = 1.5
#photonAna.etaCentral = 2.5
photonAna.ptMin = 20
#photonAna.gammaID = "POG_SPRING16_25ns_Loose_looseSieie_NoIso"
#photonAna.gammaID = "POG_SPRING15_50ns_Loose_looseSieie_NoIso"
#photonAna.gammaID = "POG_Spring16_Loose"
photonAna.gammaID = "POG_Spring17_Loose"
#photonAna.gammaID = "POG_Spring16_Medium"
photonAna.do_randomCone = False
photonAna.do_mc_match = True

# Isolated Track
isoTrackAna.setOff=False
isoTrackAna.doIsoAnnulus = True

# recalibrate MET
#metAna.recalibrate = False # 'type1' or False

# change back to this
metAna.recalibrate = 'type1' # 'type1' or False
metAna.old74XMiniAODs = False # get right Raw MET on old 74X MiniAODs



# store all taus by default
genAna.allGenTaus = True
susyScanAna.doLHE = True
#susyScanAna.doLHE = False

# Core Analyzer
ttHCoreEventAna.mhtForBiasedDPhi = "mhtJetXjvec"
ttHCoreEventAna.jetPt = mt2JPt 

##------------------------------------------ 
##  CONTROL VARIABLES
##------------------------------------------ 




#comment forSherpa
from PhysicsTools.Heppy.analyzers.gen.LHEAnalyzer import LHEAnalyzer
LHEAna = LHEAnalyzer.defaultConfig

from PhysicsTools.Heppy.analyzers.gen.TauDecayModeAnalyzer import TauDecayModeAnalyzer
TauDecayAna = TauDecayModeAnalyzer.defaultConfig

from CMGTools.TTHAnalysis.analyzers.ttHMT2Control import ttHMT2Control

ttHMT2Control = cfg.Analyzer(
            ttHMT2Control, name = 'ttHMT2Control',
            jetPt = mt2JPt, 
            )

##------------------------------------------ 
##  NUMBER of ISR JETS
##------------------------------------------ 

from CMGTools.TTHAnalysis.analyzers.ttHIsrJetAnalyzer import ttHIsrJetAnalyzer

ttHIsrJetAna = cfg.Analyzer(
            ttHIsrJetAnalyzer, name = 'ttHIsrJetAnalyzer',
            jetPt = mt2JPt, 
            )

##------------------------------------------
##  TOPOLOGICAL VARIABLES: minMT, MT2
##------------------------------------------

from CMGTools.TTHAnalysis.analyzers.ttHTopoVarAnalyzer import ttHTopoVarAnalyzer

ttHTopoJetAna = cfg.Analyzer(
            ttHTopoVarAnalyzer, name = 'ttHTopoVarAnalyzer',
            doOnlyDefault = True,
            jetPt = mt2JPt,
            )

from PhysicsTools.Heppy.analyzers.eventtopology.MT2Analyzer import MT2Analyzer

#metname = "slimmedMETs"
    

MT2Ana = cfg.Analyzer(
    MT2Analyzer, name = 'MT2Analyzer',
    metCollection     = "slimmedMETsModifiedMET",
#    metCollection     = "slimmedMETs",
    doOnlyDefault = True,
    jetPt = mt2JPt, 
    collectionPostFix = "",
    )


##------------------------------------------
##  MT2 skim
##------------------------------------------

from CMGTools.TTHAnalysis.analyzers.MT2Skimmer import MT2Skimmer
# Tree Producer                                                                                                                                                                         
MT2skim = cfg.Analyzer(
            MT2Skimmer, name='MT2Skimmer',
            )



##------------------------------------------
##  PRODUCER
##------------------------------------------


##  TRIGGERS DEFINITION
from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_photon75, triggers_photon90, triggers_photon120, triggers_photon75ps 
from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_photon90ps, triggers_photon120ps, triggers_photon155, triggers_photon165_HE10, triggers_photon175
from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_doubleele33, triggers_mumu_noniso

from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_met90_mht90, triggers_metNoMu90_mhtNoMu90, triggers_metNoMu120_mhtNoMu120, triggers_Jet80MET90



triggerFlagsAna.triggerBits = {
#diphoton signal triggers
'DiPhoton30' : ["HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v*","HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v*" ],

'DiPhoton30_2017' : ["HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v*","HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v*"],


# # signal triggers 
# 'PFHT800' : ["HLT_PFHT800_v*"],
# 'PFHT900' : ["HLT_PFHT900_v*"],
# 'PFMET170' : ["HLT_PFMET170_NoiseCleaned_v*","HLT_PFMET170_NotCleaned_v*","HLT_PFMET170_HBHECleaned_v*","HLT_PFMET170_JetIdCleaned_v*"],
# 'PFHT300_PFMET100' : ["HLT_PFHT300_PFMET100_v*"],
# 'PFHT300_PFMET110' : ["HLT_PFHT300_PFMET110_v*"],
# 'PFHT350_PFMET100' : ["HLT_PFHT350_PFMET100_NoiseCleaned_v*","HLT_PFHT350_PFMET100_JetIdCleaned_v*","HLT_PFHT350_PFMET100_v*"],
# 'PFHT350_PFMET120' : ["HLT_PFHT350_PFMET120_NoiseCleaned_v*","HLT_PFHT350_PFMET120_JetIdCleaned_v*"],
# 'PFJet450' : ["HLT_PFJet450_v*"],
# 'PFJet500' : ["HLT_PFJet500_v*"],
# #
# # mono-jet signal triggers
# 'PFMETNoMu90_PFMHTNoMu90' : ["HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v*","HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v*","HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v*"],
# 'MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90' : ["HLT_MonoCentralPFJet80_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v*","HLT_MonoCentralPFJet80_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v*",
#                                                 "HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90_IDTight_v*"],
# #
# 'PFMETNoMu100_PFMHTNoMu100' : ["HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_v*"],
# 'PFMETNoMu110_PFMHTNoMu110' : ["HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v*"],
# 'PFMETNoMu120_PFMHTNoMu120' : ["HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v*","HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v*","HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v*"],
# 'PFMET90_PFMHT90'           : ["HLT_PFMET90_PFMHT90_IDTight_v*","HLT_PFMET90_PFMHT90_IDLoose_v*"],
# 'PFMET100_PFMHT100'         : ["HLT_PFMET100_PFMHT100_IDTight_v*"],
# 'PFMET110_PFMHT110'         : ["HLT_PFMET110_PFMHT110_IDTight_v*"],
# 'PFMET120_PFMHT120'         : ["HLT_PFMET120_PFMHT120_IDTight_v*"],
# #
# # lepton triggers
# 'SingleMu'     : ["HLT_IsoMu27_v*", "HLT_IsoTkMu27_v*","HLT_IsoMu17_eta2p1_v*","HLT_IsoMu20_v*","HLT_IsoMu20_eta2p1_v*","HLT_IsoTkMu20_v*","HLT_IsoTkMu20_eta2p1_v*","HLT_IsoMu24_v*","HLT_IsoTkMu24_v*"],
# 'SingleEl'     : ["HLT_Ele32_eta2p1_WPTight_Gsf_v*", "HLT_Ele23_WPLoose_Gsf_v*","HLT_Ele22_eta2p1_WPLoose_Gsf_v*","HLT_Ele23_WP75_Gsf_v*","HLT_Ele22_eta2p1_WP75_Gsf_v*","HLT_Ele25_eta2p1_WPTight_Gsf_v*","HLT_Ele27_eta2p1_WPLoose_Gsf_v*","HLT_Ele27_eta2p1_WPTight_Gsf_v*"],
# 'DoubleEl'     : ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*","HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*"],
# 'DoubleEl33'   : ["HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v*","HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v*"],
# 'MuX_Ele12' : ["HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*","HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*","HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*"],
# 'Mu8_EleX' : ["HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*","HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v*"],
# 'DoubleMu'     : ["HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*", "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*","HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*","HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v*","HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v*"],
# 'DoubleMu_NonIso'    : ["HLT_Mu40_TkMu11_v*","HLT_Mu30_TkMu11_v*"],
# 'Mu30_Ele30_NonIso'  : ["HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v*"],
# 'Mu33_Ele33_NonIso'  : ["HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL_v*"],
# 'SingleMu_NonIso'    : ["HLT_Mu55_v*", "HLT_Mu50_v*","HLT_TkMu50_v*"],
# 'SingleEl_NonIso'    : ["HLT_Ele105_CaloIdVT_GsfTrkIdT_v*"],
# # for single-photon control region
# 'Photon120' : ["HLT_Photon120_v*"], 
# 'Photon165_HE10' : ["HLT_Photon165_HE10_v*"], 
# # photon backups
# 'Photon250_NoHE' : ["HLT_Photon250_NoHE_v*"], 
# 'ECALHT800' : ["HLT_ECALHT800_v*"], 

# # for QCD control region
# 'PFHT125_Prescale'  : ["HLT_PFHT125_v*"],
# 'PFHT200_Prescale'  : ["HLT_PFHT200_v*"],
# 'PFHT300_Prescale'  : ["HLT_PFHT300_v*"],
# 'PFHT350_Prescale'  : ["HLT_PFHT350_v*"],
# 'PFHT475_Prescale'  : ["HLT_PFHT475_v*"],
# 'PFHT600_Prescale'  : ["HLT_PFHT600_v*"],

# 'DiCentralPFJet70_PFMET120'  : ["HLT_DiCentralPFJet70_PFMET120_NoiseCleaned_v*","HLT_DiCentralPFJet70_PFMET120_JetIdCleaned_v*"], 
# 'DiCentralPFJet55_PFMET110'  : ["HLT_DiCentralPFJet55_PFMET110_NoiseCleaned_v*","HLT_DiCentralPFJet55_PFMET110_JetIdCleaned_v*"], 

# #Francesco's ?? 
# 'Photon75_R9Id90_HE10_IsoM' : triggers_photon75,
# 'Photon90_R9Id90_HE10_IsoM' : triggers_photon90,
# 'Photon120_R9Id90_HE10_IsoM' : triggers_photon120,
# 'Photon75' : triggers_photon75ps,
# 'Photon90' : triggers_photon90ps,
# 'Photon155' : triggers_photon155,
# 'Photon175' : triggers_photon175,

# ## monojet triggers
# 'PFMET90_PFMHT90' : triggers_met90_mht90,
# 'PFMETNoMu90_PFMHTNoMu90' : triggers_metNoMu90_mhtNoMu90,
# 'PFMETNoMu120_PFMHTNoMu120' : triggers_metNoMu120_mhtNoMu120,
# 'MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90' : triggers_Jet80MET90,

# ### ZGamma triggers
# 'DoubleEle33' : triggers_doubleele33,
# 'Mu30_TkMu11' : triggers_mumu_noniso,



}

# Get full list of triggers. To be used later to filter events
allTriggers = []
for key,value in triggerFlagsAna.triggerBits.items():
    allTriggers = allTriggers + value
#print "trigger list: %s" % (allTriggers)


##  FILTERS DEFINITION
eventFlagsAna.triggerBits = {
    # recommended filters for 80X
    "HBHENoiseFilter" : [ "Flag_HBHENoiseFilter" ], 
    "HBHENoiseIsoFilter" : [ "Flag_HBHENoiseIsoFilter" ], 
    # "CSCTightHalo2015Filter" : [ "Flag_CSCTightHalo2015Filter" ],
    "EcalDeadCellTriggerPrimitiveFilter" : [ "Flag_EcalDeadCellTriggerPrimitiveFilter" ],
    "goodVertices" : [ "Flag_goodVertices" ],
    "eeBadScFilter" : [ "Flag_eeBadScFilter" ],
    # Halo filter to be used
    #    "globalTightHalo2016Filter" : [ "Flag_globalTightHalo2016Filter" ],    
    #"badMuons" : [ "Flag_badMuons" ],
    #"duplicateMuons" : [ "Flag_duplicateMuons" ],
    #"noBadMuons" : [ "Flag_noBadMuons" ],
    "globalSuperTightHalo2016Filter" : ["Flag_globalSuperTightHalo2016Filter"],
    "globalTightHalo2016Filter" : ["Flag_globalTightHalo2016Filter"],
    "badMuons" : [ "Flag_BadPFMuonFilter" ],
    "badChHad" : [ "Flag_BadChargedCandidateFilter" ],
    "eeBadCalibFilter" : [ "Flag_ecalBadCalibFilter" ],
    }


#-------- SEQUENCE

from CMGTools.TTHAnalysis.analyzers.treeProducerSusyFullHad import *
from CMGTools.TTHAnalysis.analyzers.treeProducerMT2forQCDStudies import *
from CMGTools.TTHAnalysis.analyzers.treeProducerMT2forJECstudies import *

treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerSusyFullHad',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     PDFWeights = PDFWeights,
     globalVariables = susyFullHad_globalVariables,
     globalObjects = susyFullHad_globalObjects,
     collections = susyFullHad_collections,
     defaultFloatType = 'F',
     treename = 'mt2'
)






susyCoreSequence.insert(susyCoreSequence.index(skimAnalyzer),
                        susyCounter)

### Here we are moving the jet cleaning module so that the JEC corrections are already propagated
### to jets, met, and isoTracks
susyCoreSequence.remove(isoTrackAna)
susyCoreSequence.insert(susyCoreSequence.index(metAna)+1,isoTrackAna)
susyCoreSequence.insert(susyCoreSequence.index(isoTrackAna)+1,jetCleanAna)



sequence = cfg.Sequence(
    susyCoreSequence+[
        #comment forSherpa    LHEAna,
        LHEAna,
        #
        TauDecayAna,
        #
        ttHMT2Control,
        MT2Ana,
        ttHTopoJetAna,
        ttHIsrJetAna,
        treeProducer,
        ])


###---- to switch off the compression
#treeProducer.isCompressed = 0





from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

#-------- HOW TO RUN
# choose 0 for quick validations tests. It doesn't require to load the sample files
# choose 2 for full mc production
# choose 3 for data production
# choose 4 for signal production
test = int(getHeppyOption('test',0))
test = 4
isData = False # will be changed accordingly if chosen to run on data
doSpecialSettingsForMECCA = 1 # set to 1 for comparisons with americans
runPreprocessor = True #because of the EEModifiedMET
#runPreprocessor = False

#from CMGTools.RootTools.samples.samples_13TeV_RunIIFall17MiniAODv2 import *



if test==0:
    # ------------------------------------------------------------------------------------------- #
    # --- all this lines taken from CMGTools.RootTools.samples.samples_13TeV_PHYS14
    # --- They may not be in synch anymore 
    from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
    kreator = ComponentCreator()
    testComponent = kreator.makeMCComponent("testComponent", "/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1/MINIAODSIM", "CMS", ".*root",489.9)


    samples=[testComponent]

    json='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'

    dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"

    from CMGTools.TTHAnalysis.setup.Efficiencies import *

    for comp in samples:
        comp.isMC = False
        comp.isData = True
        comp.splitFactor = 250 
        comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
        comp.puFileData=dataDir+"/puProfile_Data12.root"
        comp.efficiency = eff2012
        comp.json = json
    # ------------------------------------------------------------------------------------------- #

    #eventSelector.toSelect = [ 442430994 ]
    #sequence = cfg.Sequence([eventSelector] + sequence)
    comp=testComponent

    comp.files = ['file:/afs/cern.ch/user/c/casal/public/96E8E959-E191-E611-8593-002590DB9232.root']
    
    selectedComponents = [comp]
    #comp.splitFactor = 10
    #    comp.fineSplitFactor = 100

    #for comp in selectedComponents:
    #    comp.splitFactor = 1200
    #    comp.files = comp.files[:]
    #    comp.fineSplitFactor = 4 



elif test==1:
    # Uncomment the two following lines to run on a specific event
    #eventSelector.toSelect = [ 84142401 ]
    #sequence = cfg.Sequence([eventSelector] + sequence)

#    isData = False
    isData = True
    #from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import *
    #from CMGTools.RootTools.samples.samples_13TeV_RunIISummer16MiniAODv2 import *
    from CMGTools.RootTools.samples.samples_13TeV_DATA2017 import *


    #dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"
    ##json=dataDir+'/json/json_DCSONLY.txt'
    # json=dataDir+'/json/json_ichep2016.txt'
    
    # --------------- ALL THIS IS FOR TESTS -----------------------------------------------------
    # Warning: this only works when running (e.g. locally) and having access to afs
    #json='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/DCSOnly/json_DCSONLY.txt' 

    #For synch on a single file
    #comp = JetHT_Run2016B_PromptReco_v1
    #comp.files = ['root://xrootd.unl.edu//store/data/Run2016C/HTMHT/MINIAOD/PromptReco-v2/000/275/420/00000/4AD126B0-F539-E611-AD77-02163E013390.root'
#/store/data/Run2016C/HTMHT/MINIAOD/PromptReco-v2/000/275/658/00000/227E1B3A-A53B-E611-A53E-02163E0136C4.root'
#'/afs/cern.ch/user/m/mangano/work/datasets/data/80X/HTMHT.root'
   
#TTJets_SingleLeptonFromTbar_ext = kreator.makeMCComponent("TTJets_SingleLeptonFromTbar_ext", "/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(1-3*0.108) )

    #    selectedComponents = [TTJets_SingleLeptonFromTbar_ext]
    #    selectedComponents = [ DoubleEG_Run2017F_17Nov2017]
    #    selectedComponents = [ DoubleEG_Run2017F_31Mar2018_v1 ]

    selectedComponents = [ DoubleEG_Run2017C_31Mar2018_v1 ]


  #  runPreprocessor = False #because of the EEModifiedMET

    for comp in selectedComponents:
        
        # comp.files = ['root://xrootd.unl.edu//store/data/Run2016F/JetHT/MINIAOD/23Sep2016-v1/100000/322B5B83-B184-E611-A5B1-0026B927862A.root']
#        isData = True
        comp.isMC = False
        comp.isData = True
        #comp.isMC = True
        #comp.isData = False

        #comp.files = ['root://xrootd.unl.edu//store/data/Run2016G/DoubleEG/MINIAOD/03Feb2017-v1/80000/FEA99FAC-F6EA-E611-9BE7-003048F5B69C.root']
        
#  comp.files = ['file:testFileWH.root']

        comp.files = ['root://xrootd.unl.edu//store/data/Run2017F/DoubleEG/MINIAOD/31Mar2018-v1/90000/8EDA21E9-2437-E811-8F9F-0025905C431A.root']

        eventSelector.toSelect = [(305044,119, 202739699 )         ]


   #     eventSelector.toSelect = [ 305044 ,  ]
        sequence = cfg.Sequence([eventSelector] + sequence)

#eventsToProcess = cms.untracked.VEventRange('305044:1-305044:max'),


        #comp.files = ['root://xrootd.unl.edu//store/mc/RunIIFall17MiniAODv2/VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/028340E8-D442-E811-813C-0025905B8560.root']

#        comp.files = ['file:Data2017F_31Mar2018-v1.root']
#        comp.files = comp.files[:1]
#        comp.files = ['root://xrootd.unl.edu//store/data/Run2017F/DoubleEG/MINIAOD/31Mar2018-v1/00000/005DCBA4-6137-E811-964C-0025904C67BA.root']

    # # Tree configuration for JEC variations
    # if jetAna.shiftJEC > 0.5 or jetAna.shiftJEC < -0.5:
    #     treeProducer.globalVariables = MT2forJECstudies_globalVariables
    #     treeProducer.globalObjects = MT2forJECstudies_globalObjects
    #     treeProducer.collections = MT2forJECstudies_collections



elif test==2:

    # FULLSIM submission
    #    from CMGTools.RootTools.samples.samples_13TeV_RunIIFall17MiniAOD import *
    isData = False
    from CMGTools.RootTools.samples.samples_13TeV_RunIIFall17MiniAODv2 import *

#    selectedComponents = MT2hgg 

    selectedComponents = [
        #     THQ_ctcvcp_HToGG_M125,
        #     THW_ctcvcp_HToGG_M125,
        #     VHToGG_M125_powheg,
        #     VBFHToGG_M125_powheg,
        #     GluGluHToGG_M125_powheg,
        VBFHToGG_M125,
        VHToGG_M125,
        #        ttHToGG_M125,
        ttHJetToGG_M125,
        GluGluHToGG_M125,
        bbHToGG_M125_4FS_yb2,
        ]

    #    selectedComponents = [DiPhotonJetsBox_MGG_80toInf]
    #    selectedComponents = [GJet_Pt_40toInf_MGG_80toInf]


    for comp in selectedComponents:
        comp.isMC = True
        comp.isData = False
        #        comp.files=comp.files[5:6]
        comp.fineSplitFactor = 8 # to run two jobs per file
        comp.files = comp.files[:]
        #        comp.splitFactor = 2400
        comp.splitFactor = 1200
        # triggers on MC
        #comp.triggers = triggers_HT900 + triggers_HTMET + triggers_photon155 + triggers_1mu_isolow + triggers_MT2_mumu + triggers_MT2_ee + triggers_MT2_mue # to apply trigger skimming`

    # Tree configuration for JEC variations
    if jetAna.shiftJEC > 0.5 or jetAna.shiftJEC < -0.5:
        treeProducer.globalVariables = MT2forJECstudies_globalVariables
        treeProducer.globalObjects = MT2forJECstudies_globalObjects
        treeProducer.collections = MT2forJECstudies_collections



elif test==3:
    # run on data

    # magic string to submit jobs via heppy_crab.py script:
    # python heppy_crab.py -c ../run_susyMT2_cfg.py --AAAconfig=full -s T3_CH_PSI -d crab -v MT2_8_0_5 -l data30May_v1 -u mt2.root,RLTInfo.root

    isData = True
    #from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import *
    from CMGTools.RootTools.samples.samples_13TeV_DATA2017 import *

    dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"
    # wont run with crab like this json='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    #    json=dataDir+'/json/json_ReReco_final_2016Run.txt'
    #    json=dataDir+'/json/json_PromptReco_Run2017.txt'
    json=dataDir+'/json/json_EOY_reReco_2017Run.txt'


    
    # --------------- ALL THIS IS FOR TESTS -----------------------------------------------------
    # Warning: this only works when running (e.g. locally) and having access to afs
    #json='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/DCSOnly/json_DCSONLY.txt' 

    #For synch on a single file
    #comp = JetHT_Run2016B_PromptReco_v1
    #comp.files = ['root://xrootd.unl.edu//store/data/Run2016C/HTMHT/MINIAOD/PromptReco-v2/000/275/420/00000/4AD126B0-F539-E611-AD77-02163E013390.root'
#/store/data/Run2016C/HTMHT/MINIAOD/PromptReco-v2/000/275/658/00000/227E1B3A-A53B-E611-A53E-02163E0136C4.root'
#'/afs/cern.ch/user/m/mangano/work/datasets/data/80X/HTMHT.root'
    #For runnin on a single dataset
    #selectedComponents  = [JetHT_Run2016B_PromptReco_v2]
    # --------------------------------------------------------------------


    # --------------- HERE IS THE PART YOU SHOULD PAY ATTENTION TO --------------------------------------------
    #For running on the full list of samples
        
#    selectedComponents  = [ DoubleEG_Run2017B_31Mar2018_v1 ]
#        selectedComponents  = dataSamples_Run2017_DoubleEG_reReco

    selectedComponents  = doubleEG_31Mar2018
 
    for comp in selectedComponents:
        comp.json=json
        comp.isMC = False
        comp.isData = True
        #        comp.fineSplitFactor = 8
        #        comp.fineSplitFactor = 8
        comp.splitFactor = 800
        comp.files=comp.files[:]
#        comp.files=comp.files[50:51]
        comp.triggers = allTriggers
        
    sequence.insert(sequence.index(treeProducer), MT2skim)
    

elif test==4:

    #    from CMGTools.RootTools.samples.samples_13TeV_signals import *
    from CMGTools.RootTools.samples.samples_13TeV_2017_signal import *


#    jetAna.mcGT     = "Spring16_FastSimV1_MC" # jec corrections for FastSim V1### 25

    jetAna.mcGT     = "Fall17_FastsimV1" # jec corrections for FastSim V1### 25
    jetAna.applyL2L3Residual = False # 'Data'
    jetAna.do_mc_match = True
    jetAna.relaxJetId = True
    jetCleanAna.relaxJetId = True

    lheWeightAna.doFastSim=True



    selectedComponents = [
        SMS_T2bH_HToGG_250,
        SMS_TChiWH_HToGG_175,
        SMS_T2bH_HToGG,
        SMS_TChiWH_HToGG,
        SMS_TChiHZ_HToGG,
        SMS_TChiHH_HToGG,
        ]

    # test all components (1 thread per component).
    for comp in selectedComponents:
        comp.splitFactor = 1200
        comp.fineSplitFactor = 4 # to run 4 jobs per file
        #comp.files = comp.files[:1]
        comp.files = comp.files[:]
        #comp.triggers = triggers_HT900 + triggers_HTMET + triggers_photon155 + triggers_1mu_isolow + triggers_MT2_mumu + triggers_MT2_ee + triggers_MT2_mue # to apply trigger skimming


    # Tree configuration for JEC variations
    if jetAna.shiftJEC > 0.5 or jetAna.shiftJEC < -0.5:
        treeProducer.globalVariables = MT2forJECstudies_globalVariables
        treeProducer.globalObjects = MT2forJECstudies_globalObjects
        treeProducer.collections = MT2forJECstudies_collections


# ------------------------------------------------------------------------------------------- #


if doSpecialSettingsForMECCA:
    jetAna.doQG = False
    # photonAna.do_randomCone = False
    # Below slow things note: it will in any case try it only on MC, not on data
    # photonAna.do_mc_match = False
    # jetAna.do_mc_match = False
    lepAna.do_mc_match = False
    isoTrackAna.do_mc_match = False
#    genAna.makeLHEweights = False ### Such option does not exist (anymore)
    genAna.makeLHEweights = True ### Such option does not exist (anymore)

if isData:
    for comp in samples:
        comp.isMC = False
        comp.isData = True
        #comp.files = ['/afs/cern.ch/user/d/dalfonso/public/74samples/JetHT_GR_R_74_V12_19May_RelVal/1294BDDB-B7FE-E411-8028-002590596490.root']



# ------------------------------------------------------------------------------------------- #


from PhysicsTools.HeppyCore.framework.services.tfile import TFileService 
output_service = cfg.Service(
      TFileService,
      'outputfile',
      name="outputfile",
      fname='mt2.root',
      option='recreate'
    )


from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [output_service],
                     #                     events_class = event_class)
                     events_class = Events)



##------------------------------------------------------------------------------
## DON'T KNOW WHAT THIS IS FOR
##------------------------------------------------------------------------------

# -------------------- Running Download from EOS
# the following is declared in case this cfg is used in input to the heppy.py script
from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
event_class = EOSEventsWithDownload
if getHeppyOption("nofetch"):
    event_class = Events





#------------------------------------------------------------------------------
# EVERYTHING THAT FOLLOWS IS FOR RUNNING PRE-PROCESSOR (turned off by default)
#------------------------------------------------------------------------------

if runPreprocessor:
    
    removeResiduals = False
    # -------------------- Running pre-processor
    import subprocess

#jetAna.mcGT="Fall17_17Nov2017_V6_MC"
#jetAna.dataGT = [ [ -1, "Fall17_17Nov2017B_V6_DATA"], [299337 ,"Fall17_17Nov2017C_V6_DATA"] , [302030 ,"Fall17_17Nov2017D_V6_DATA"] , [ 303435  ,"Fall17_17Nov2017E_V6_DATA"], [ 304911  ,"Fall17_17Nov2017F_V6_DATA"]  ]
    # if isData:
    #     uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_DATA_UncertaintySources_AK4PFchs.txt'
    #     jecDBFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_DATA.db'
    #     jecEra    = 'Summer15_25nsV6_DATA'
    # else:
    #     uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_MC_UncertaintySources_AK4PFchs.txt'
    #     jecDBFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_MC.db'
    #     jecEra    = 'Summer15_25nsV6_MC'
    #preprocessorFile = "$CMSSW_BASE/tmp/MetType1_jec_%s.py"%(jecEra)
    
    extraArgs=[]
    if isData:
        extraArgs.append('--isData')
        #     GT= '74X_dataRun2_Prompt_v1'
        # else:
        #     GT= 'MCRUN2_74_V9A'
    GT='94X_dataRun2_ReReco_EOY17_v6'

    preprocessorFile = "$CMSSW_BASE/tmp/MetType1_jec.py"
#    preprocessorFile = "$CMSSW_BASE/tmp/MetType1_jec_%s.py"%(GT)

    if removeResiduals:extraArgs.append('--removeResiduals')
    args = ['python',
            os.path.expandvars('$CMSSW_BASE/python/CMGTools/ObjectStudies/corMETMiniAOD_cfgCreator.py'),
            '--GT='+GT,
            '--outputFile='+preprocessorFile,
            #'--jecDBFile='+jecDBFile,
            #'--uncFile='+uncFile,
            #'--jecEra='+jecEra
            ] + extraArgs

    print "Making pre-processorfile:"
    print " ".join(args)

    subprocess.call(args)
    from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
    preprocessor = CmsswPreprocessor(preprocessorFile)


    config = cfg.Config( components = selectedComponents,
                         sequence = sequence,
                         services = [output_service],
                         preprocessor=preprocessor, # comment if pre-processor non needed
                         #                     events_class = event_class)
                         events_class = Events)


#printComps(config.components, True)

