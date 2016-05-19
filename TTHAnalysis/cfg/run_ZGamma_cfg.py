import PhysicsTools.HeppyCore.framework.config as cfg


#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

# Comment this line if you want the diagnostic folders produced along with the output root file
cfg.Analyzer.nosubdir = True


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
lepAna.loose_muon_id = "POG_ID_Loose"
#lepAna.loose_muon_id = "POG_ID_HighPt_OR_Loose"
lepAna.loose_muon_dxy = 0.2
lepAna.loose_muon_dz  = 0.5
lepAna.loose_muon_relIso  = 0.15
lepAna.loose_muon_isoCut = lambda muon :muon.miniRelIso < 0.2

lepAna.loose_electron_pt  = 5
lepAna.loose_electron_eta    = 2.4
lepAna.loose_electron_relIso = 0.15
lepAna.loose_electron_isoCut = lambda electron : electron.miniRelIso < 0.1

lepAna.loose_electron_id  = "POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto_full5x5"
#lepAna.loose_electron_id  = "POG_Cuts_ID_PHYS14_25ns_v1_ConvVetoDxyDz_Veto_full5x5"
lepAna.loose_electron_lostHits = 999. # no cut
lepAna.loose_electron_dxy    = 999.
lepAna.loose_electron_dz     = 999.

lepAna.inclusive_electron_id  = "POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto_full5x5"
#lepAna.inclusive_electron_id  = "POG_Cuts_ID_PHYS14_25ns_v1_ConvVetoDxyDz_Veto_full5x5"
lepAna.inclusive_electron_lostHits = 999. # no cut since embedded in ID
lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID

lepAna.mu_isoCorr = "deltaBeta"
lepAna.ele_isoCorr = "deltaBeta"
#lepAna.ele_tightId = "Cuts_PHYS14_25ns_v1_ConvVetoDxyDz"
lepAna.ele_tightId = "Cuts_SPRING15_25ns_v1_ConvVetoDxyDz"
lepAna.notCleaningElectrons = True
lepAna.doMiniIsolation = True
lepAna.miniIsolationPUCorr = 'rhoArea'
#lepAna.ele_effectiveAreas = 'Phys14_25ns_v1'              #what we used with SnT       
#lepAna.mu_effectiveAreas = 'Phys14_25ns_v1'               #what we used with SnT
lepAna.ele_effectiveAreas = 'Spring15_25ns_v1'             #new default 
lepAna.mu_effectiveAreas = 'Spring15_25ns_v1'              #new default
#lepAna.rhoMuon= 'fixedGridRhoFastjetAll',                  #what we used with SnT       
#lepAna.rhoElectron = 'fixedGridRhoFastjetAll',             #what we used with SnT   
lepAna.rhoMuon= 'fixedGridRhoFastjetCentralNeutral',      #new default
lepAna.rhoElectron = 'fixedGridRhoFastjetCentralNeutral', #new default

lepAna.doIsoAnnulus = False


# JET (for event variables do apply the jetID and not PUID yet)
jetAna.relaxJetId = False
jetAna.doPuId = False
jetAna.doQG = False
jetAna.jetEta = 4.7
jetAna.jetEtaCentral = 2.5
jetAna.jetPt = 30. #was 10
jetAna.mcGT     = "Spring16_25nsV1_MC" # jec corrections
jetAna.dataGT   = "Spring16_25nsV1_MC" # jec corrections
jetAna.recalibrateJets = True # True or False
jetAna.applyL2L3Residual = True # 'Data'
jetAna.calculateSeparateCorrections = True
jetAna.jetLepDR = 0.4
jetAna.smearJets = False
jetAna.jetGammaDR = 0.4
jetAna.cleanFromLepAndGammaSimultaneously = True
jetAna.jetGammaLepDR = 0.4
jetAna.minGammaPt = 20.
jetAna.gammaEtaCentral = 2.4
jetAna.cleanJetsFromFirstPhoton = True
jetAna.cleanJetsFromIsoTracks = False ## added for Dominick


# Photon
photonAna.etaCentral = 2.5
photonAna.ptMin = 20
photonAna.gammaID = "POG_SPRING15_25ns_Loose_NoIso"
photonAna.do_randomCone = False
photonAna.do_mc_match = True
photonAna.conversionSafe_eleVeto = False




#era = "25ns"
#sync = False
#
#lepAna.doElectronScaleCorrections = {
#  'data' : 'EgammaAnalysis/ElectronTools/data/76X_16DecRereco_2015',
#  'GBRForest': ('$CMSSW_BASE/src/CMGTools/RootTools/data/egamma_epComb_GBRForest_76X.root',
#    'gedelectron_p4combination_'+era),
#  'isSync': sync
#}
#
#photonAna.doPhotonScaleCorrections = {
#  'data' : 'EgammaAnalysis/ElectronTools/data/76X_16DecRereco_2015',
#  'isSync': sync
#}
#
#smear = "basic"
#lepAna.doMuonScaleCorrections = ( 'Kalman', {
#  'MC': 'MC_76X_13TeV',
#  'Data': 'DATA_76X_13TeV',
#  'isSync': sync,
#  'smearMode':smear
#})


# recalibrate MET
metAna.recalibrate = 'type1' # 'type1' or False
metAna.old74XMiniAODs = False # get right Raw MET on old 74X MiniAODs

# store all taus by default
genAna.allGenTaus = True

# Core Analyzer
ttHCoreEventAna.mhtForBiasedDPhi = "mhtJetXjvec"
ttHCoreEventAna.jetPt = mt2JPt ### jet pt 30: this will change ht and mht

# switch off the SV and MC matching
#ttHSVAna.do_mc_match = False




##------------------------------------------
##  Z skim
##------------------------------------------

from CMGTools.TTHAnalysis.analyzers.ttHmllSkimmer import ttHmllSkimmer
# Tree Producer                                                                                                                                                                         
ttHZskim = cfg.Analyzer(
            ttHmllSkimmer, name='ttHmllSkimmer',
            lepId=[13],
            maxLeps=3,
            massMin=60,
            massMax=120,
            doZGen = False,
            doZReco = True
            )


##------------------------------------------
##  PRODUCER
##------------------------------------------





##  TRIGGERS DEFINITION
from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_photon75, triggers_photon90, triggers_photon120, triggers_photon75ps 
from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_photon90ps, triggers_photon120ps, triggers_photon155, triggers_photon165_HE10, triggers_photon175
from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_doubleele33, triggers_mumu_noniso

triggerFlagsAna.triggerBits = {
# signal triggers 
'PFHT800' : ["HLT_PFHT800_v*"],
'PFHT900' : ["HLT_PFHT900_v*"],
'PFMET170' : ["HLT_PFMET170_NoiseCleaned_v*","HLT_PFMET170_NotCleaned_v*","HLT_PFMET170_HBHECleaned_v*","HLT_PFMET170_JetIdCleaned_v*"],
'PFHT300_PFMET100' : ["HLT_PFHT300_PFMET100_v*"],
'PFHT300_PFMET110' : ["HLT_PFHT300_PFMET110_v*"],
'PFHT350_PFMET100' : ["HLT_PFHT350_PFMET100_NoiseCleaned_v*","HLT_PFHT350_PFMET100_JetIdCleaned_v*","HLT_PFHT350_PFMET100_v*"],
'PFHT350_PFMET120' : ["HLT_PFHT350_PFMET120_NoiseCleaned_v*","HLT_PFHT350_PFMET120_JetIdCleaned_v*"],
#
# mono-jet signal triggers
'PFMETNoMu90_PFMHTNoMu90' : ["HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v*","HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v*","HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v*"],
'MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90' : ["HLT_MonoCentralPFJet80_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v*","HLT_MonoCentralPFJet80_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v*",
                                                "HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90_IDTight_v*"],
'PFMETNoMu120_PFMHTNoMu120' : ["HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v*","HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v*","HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v*"],
'PFMET90_PFMHT90'           : ["HLT_PFMET90_PFMHT90_IDTight_v*","HLT_PFMET90_PFMHT90_IDLoose_v*"],
'PFMET100_PFMHT100'         : ["HLT_PFMET100_PFMHT100_IDTight_v*"],
'PFMET110_PFMHT110'         : ["HLT_PFMET110_PFMHT110_IDTight_v*"],
'PFMET120_PFMHT120'         : ["HLT_PFMET120_PFMHT120_IDTight_v*"],
#
# lepton triggers
'SingleMu'     : ["HLT_IsoMu17_eta2p1_v*","HLT_IsoMu20_v*","HLT_IsoMu20_eta2p1_v*","HLT_IsoTkMu20_v*","HLT_IsoTkMu20_eta2p1_v*","HLT_IsoMu24_v*","HLT_IsoTkMu24_v*"],
'SingleEl'     : ["HLT_Ele23_WPLoose_Gsf_v*","HLT_Ele22_eta2p1_WPLoose_Gsf_v*","HLT_Ele23_WP75_Gsf_v*","HLT_Ele22_eta2p1_WP75_Gsf_v*","HLT_Ele25_eta2p1_WPTight_Gsf_v*"],
'DoubleEl'     : ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*","HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*"],
'DoubleEl33'   : ["HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v*"],
'MuX_Ele12' : ["HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*","HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*"],
'Mu8_EleX' : ["HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*","HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v*"],
'DoubleMu'     : ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*","HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*","HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v*","HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v*"],
# for single-photon control region
'Photon120' : ["HLT_Photon120_v*"], 
'Photon165_HE10' : ["HLT_Photon165_HE10_v*"], 

# for QCD control region
'PFHT125_Prescale'  : ["HLT_PFHT125_v*"],
'PFHT200_Prescale'  : ["HLT_PFHT200_v*"],
'PFHT300_Prescale'  : ["HLT_PFHT300_v*"],
'PFHT350_Prescale'  : ["HLT_PFHT350_v*"],
'PFHT475_Prescale'  : ["HLT_PFHT475_v*"],
'PFHT600_Prescale'  : ["HLT_PFHT600_v*"],

'DiCentralPFJet70_PFMET120'  : ["HLT_DiCentralPFJet70_PFMET120_NoiseCleaned_v*","HLT_DiCentralPFJet70_PFMET120_JetIdCleaned_v*"], 
'DiCentralPFJet55_PFMET110'  : ["HLT_DiCentralPFJet55_PFMET110_NoiseCleaned_v*","HLT_DiCentralPFJet55_PFMET110_JetIdCleaned_v*"], 

#Francesco's ?? 
'Photon75_R9Id90_HE10_IsoM' : triggers_photon75,
'Photon90_R9Id90_HE10_IsoM' : triggers_photon90,
'Photon120_R9Id90_HE10_IsoM' : triggers_photon120,
'Photon75' : triggers_photon75ps,
'Photon90' : triggers_photon90ps,
'Photon155' : triggers_photon155,
'Photon175' : triggers_photon175,

### ZGamma triggers
'DoubleEle33' : triggers_doubleele33,
'Mu30_TkMu11' : triggers_mumu_noniso,
}


##  FILTERS DEFINITION
eventFlagsAna.triggerBits = {
# recommended filters for 80X
    "HBHENoiseFilter" : [ "Flag_HBHENoiseFilter" ], 
    "HBHENoiseIsoFilter" : [ "Flag_HBHENoiseIsoFilter" ], 
    "CSCTightHalo2015Filter" : [ "Flag_CSCTightHalo2015Filter" ],
    "EcalDeadCellTriggerPrimitiveFilter" : [ "Flag_EcalDeadCellTriggerPrimitiveFilter" ],
    "goodVertices" : [ "Flag_goodVertices" ],
    "eeBadScFilter" : [ "Flag_eeBadScFilter" ],
# filter under study 
    "globalTightHalo2016Filter" : [ "Flag_globalTightHalo2016Filter" ],
}


#-------- SEQUENCE

from CMGTools.TTHAnalysis.analyzers.treeProducerZGamma import *

treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerZGamma',
##     AutoFillTreeProducer, name='treeProducerSusyCore',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     PDFWeights = PDFWeights,
     globalVariables = zgamma_globalVariables,
     globalObjects = zgamma_globalObjects,
     collections = zgamma_collections,
     defaultFloatType = 'F',
     treename = 'mt2'
)

susyCoreSequence.insert(susyCoreSequence.index(skimAnalyzer),
                        susyCounter)

#susyCoreSequence.insert(susyCoreSequence.index(ttHLepSkim),
#                        ttHZskim)

#susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
#                        ttHSVAna)


sequence = cfg.Sequence(
    susyCoreSequence+[
#    hbheFilterAna,
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

test = 0 # this is for local tests
#test = 2 # this is for 76X ZGamma MC
#test = 3 # this is for data 2016

isData = False # will be changed accordingly if chosen to run on data
runPreprocessor = False

if test==0:
    # ------------------------------------------------------------------------------------------- #
    # --- all this lines taken from CMGTools.RootTools.samples.samples_13TeV_PHYS14
    # --- They may not be in synch anymore 
    from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
    kreator = ComponentCreator()
    testComponent = kreator.makeMCComponent("testComponent", "/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",489.9)
    samples=[testComponent]

    json='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/DCSOnly/json_DCSONLY.txt'

    dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"

    from CMGTools.TTHAnalysis.setup.Efficiencies import *

    for comp in samples:
#        comp.isMC = True
#        comp.isData = False
        comp.splitFactor = 250 
        comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
        comp.puFileData=dataDir+"/puProfile_Data12.root"
        comp.efficiency = eff2012
        comp.json = json
    # ------------------------------------------------------------------------------------------- #

    #eventSelector.toSelect = [ 442430994 ]
    #sequence = cfg.Sequence([eventSelector] + sequence)
    comp=testComponent
    # 80X TTJets SingleLeptFromT for synch with SnT
    comp.files = ['file:/afs/cern.ch/user/m/mangano/public/MECCA/dataset/80X/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_109B2CAB-1205-E611-A9BE-0CC47A0AD6C4.root']
    ## 74X TTbar
    #comp.files = ['/afs/cern.ch/user/d/dalfonso/public/SYNCHfiles/0066F143-F8FD-E411-9A0B-D4AE526A0D2E.root']

    # 74X GJets
    #comp.files = ['root://xrootd.unl.edu//store/mc/RunIISpring15DR74/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/16E31BE7-7C18-E511-A551-00266CF2454C.root']

    # 747 Data
    #comp.files = ['/afs/cern.ch/user/m/mangano/public/MECCA/dataset/74X/data/JetHT_promptReco_Run2015B.root']
    #comp.files = ['/afs/cern.ch/work/m/mmasciov/CMSSW_7_4_7_MT2/src/CMGTools/TTHAnalysis/cfg/pickevents.root']

    # 7_4_12 data
    #isData = True
    #comp.files = ['/afs/cern.ch/user/c/casal/public/synch/86ACFECD-3C5F-E511-B8F2-02163E014374.root']

    selectedComponents = [comp]
#    comp.splitFactor = 10
#    comp.fineSplitFactor = 100

elif test==1:
    # Uncomment the two following lines to run on a specific event
    #eventSelector.toSelect = [ 84142401 ]
    #sequence = cfg.Sequence([eventSelector] + sequence)
    
#    from CMGTools.RootTools.samples.samples_13TeV_PHYS14 import *
#    from CMGTools.RootTools.samples.samples_13TeV_74X import *
#    from CMGTools.RootTools.samples.samples_13TeV_RunIISpring15MiniAODv2 import *
    from CMGTools.RootTools.samples.samples_13TeV_RunIIFall15MiniAODv2 import *
#    from CMGTools.RootTools.samples.samples_8TeVReReco_74X import *
#    from CMGTools.RootTools.samples.samples_13TeV_DATA2015 import *

#    comp=GJets_HT200to400
#    comp.files = ['/afs/cern.ch/user/d/dalfonso/public/TESTfilesPHY14/gjets_ht200to400_miniaodsim_fix.root']

#    comp=TTJets
#    #comp.files = ['/afs/cern.ch/user/d/dalfonso/public/TESTfilesPHY14/TTJets_miniAOD_fixPhoton_forSynch.root']
#    comp.files = ['/afs/cern.ch/user/d/dalfonso/public/TESTspring/ttbar25nsmad_1ECE44F9-5F02-E511-9A65-02163E00EA1F.root']
#    #comp.files = ['/afs/cern.ch/user/d/dalfonso/public/74samples/JetHT_GR_R_74_V12_19May_RelVal/1294BDDB-B7FE-E411-8028-002590596490.root']
#    comp.files = ['/afs/cern.ch/user/m/mangano/public/MECCA/dataset/74X/data/JetHT_promptReco_Run2015B.root']

#    #synche file MC (v1 of the miniAOD)
#    comp=comp=TTJets_LO_50ns
#    comp.files = ['/afs/cern.ch/user/d/dalfonso/public/SYNCHfiles/0066F143-F8FD-E411-9A0B-D4AE526A0D2E.root']

    #synche file MC (v2 of the miniAOD)
#    comp=TTJets_LO
#    comp.files = ['/afs/cern.ch/work/d/dalfonso/public/001F4F14-786E-E511-804F-0025905A60FE.root']
   
#    comp=JetHT_Run2015D_Promptv4
#    comp.files = ['/afs/cern.ch/work/d/dalfonso/public/8ED4BA45-706D-E511-8D36-02163E014418.root']
#    comp.json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/DCSOnly/json_DCSONLY.txt'

    selectedComponents = [TTJets_LO]
    for comp in selectedComponents:
        comp.files = ['root://xrootd.unl.edu//store/mc/RunIIFall15MiniAODv2/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/00000/00D010B5-1EB9-E511-B950-02163E014965.root']
        #comp.files = ['TTJets_76X.002590DE6E34.root']
        #comp.files = ['GluGluSpin0ToZG_ZToLL_W-0p014_M-5000.root']
        comp.splitFactor = 1200


#    comp.triggers = triggers_HT900 + triggers_HTMET + triggers_photon155 + triggers_1mu_isolow + triggers_MT2_mumu + triggers_MT2_ee + triggers_MT2_mue # to apply trigger skimming

elif test==2:

    #from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *
    # full production
#    selectedComponents = [ 
#TTJets, # TTJets
#TToLeptons_tch, TToLeptons_sch, TBarToLeptons_tch, TBarToLeptons_sch, TBar_tWch, T_tWch, #singleTop
#TTWJets, TTZJets, TTH, #TT+boson
#ZJetsToNuNu_HT100to200, ZJetsToNuNu_HT200to400, ZJetsToNuNu_HT400to600, ZJetsToNuNu_HT600toInf, # ZJetsToNuNu_HT
#WJetsToLNu_HT100to200, WJetsToLNu_HT200to400, WJetsToLNu_HT400to600, WJetsToLNu_HT600toInf, # WJetsToLNu_HT
#GJets_HT100to200_fixPhoton, GJets_HT200to400_fixPhoton, GJets_HT400to600_fixPhoton, GJets_HT600toInf_fixPhoton, # GJets_HT
#QCD_HT_100To250_fixPhoton, QCD_HT_250To500_fixPhoton, QCD_HT_500To1000_fixPhoton, QCD_HT_1000ToInf_fixPhoton, QCD_HT_250To500_ext1_fixPhoton, QCD_HT_500To1000_ext1_fixPhoton,QCD_HT_1000ToInf_ext1_fixPhoton, # QCD_HT
#QCD_Pt170to300_fixPhoton, QCD_Pt300to470_fixPhoton, QCD_Pt470to600_fixPhoton, QCD_Pt600to800_fixPhoton, QCD_Pt800to1000_fixPhoton, QCD_Pt1000to1400_fixPhoton, QCD_Pt1400to1800_fixPhoton, QCD_Pt1800to2400_fixPhoton, QCD_Pt2400to3200_fixPhoton, QCD_Pt3200_fixPhoton, # QCD_Pt
#QCD_Pt50to80, QCD_Pt80to120, QCD_Pt120to170, #For QCD Estimate
#SMS_T2tt_2J_mStop850_mLSP100, SMS_T2tt_2J_mStop650_mLSP325, SMS_T2tt_2J_mStop500_mLSP325, SMS_T2tt_2J_mStop425_mLSP325, SMS_T2qq_2J_mStop600_mLSP550, SMS_T2qq_2J_mStop1200_mLSP100, SMS_T2bb_2J_mStop900_mLSP100, SMS_T2bb_2J_mStop600_mLSP580, SMS_T1tttt_2J_mGl1500_mLSP100, SMS_T1tttt_2J_mGl1200_mLSP800, SMS_T1qqqq_2J_mGl1400_mLSP100, SMS_T1qqqq_2J_mGl1000_mLSP800, SMS_T1bbbb_2J_mGl1500_mLSP100, SMS_T1bbbb_2J_mGl1000_mLSP900, # SMS
#DYJetsToLL_M50_HT100to200, DYJetsToLL_M50_HT200to400, DYJetsToLL_M50_HT400to600, DYJetsToLL_M50_HT600toInf # DYJetsToLL_M50_HT
#]

#    from CMGTools.RootTools.samples.samples_13TeV_74X import *
#### 25 ns
##    selectedComponents = [ 
##TTJets, TTJets_LO, # TTJets
##QCD_Pt80to120, QCD_Pt120to170, QCD_Pt300to470, QCD_Pt470to600, QCD_Pt1000to1400, QCD_Pt1400to1800, QCD_Pt1800to2400, QCD_Pt2400to3200, QCD_Pt3200toInf, # QCD_Pt
##]
#
#### 25    
##    selectedComponents = [DYJetsToLL_M50_Zpt150toInf_LO]
#
#    selectedComponents = ZJetsToNuNuHT + DYJetsM50HT + QCDPt + QCDHT + [
#TTJets_SingleLeptonFromT, TTJets_SingleLeptonFromTbar, TTJets_DiLepton,
#TTV, TToLeptons_tch, TbarToLeptons_tch, 
#TTJets_LO,
##                                                                                                                                                                      
#GJets_HT100to200,
#GJets_HT200to400,
#GJets_HT400to600,
#GJets_HT600toInf,
##
#WJetsToLNu_HT100to200,
#WJetsToLNu_HT200to400,
#WJetsToLNu_HT400to600,
#WJetsToLNu_HT600toInf,
#] ### Full SM BG Spring15
#
#    # test all components (1 thread per component).
#    for comp in selectedComponents:
#        comp.splitFactor = 1200
#        #comp.fineSplitFactor = 2 # to run two jobs per file
#        comp.files = comp.files[:]
#        #comp.files = comp.files[:1]
#        #comp.files = comp.files[57:58]  # to process only file [57]  
#        # triggers on MC
#        #comp.triggers = triggers_HT900 + triggers_HTMET + triggers_photon155 + triggers_1mu_isolow + triggers_MT2_mumu + triggers_MT2_ee + triggers_MT2_mue # to apply trigger skimming

    from CMGTools.RootTools.samples.samples_13TeV_RunIIFall15MiniAODv2 import *
    #from CMGTools.RootTools.samples.samples_13TeV_RunIIFall15MiniAODv2 import ZGammaSig
### 25 ns
    selectedComponents = [ZGTo2LG, DYJetsToLL_M50_LO] + ZGsignal

    for comp in selectedComponents:
        comp.splitFactor = 1200
        #comp.fineSplitFactor = 2 # to run two jobs per file
        comp.files = comp.files[:]
        #comp.files = comp.files[:1]
        #comp.files = comp.files[57:58]  # to process only file [57]  
        # triggers on MC
        #comp.triggers = triggers_HT900 + triggers_HTMET + triggers_photon155 + triggers_1mu_isolow + triggers_MT2_mumu + triggers_MT2_ee + triggers_MT2_mue # to apply trigger skimming


elif test==3:
    # run on data
    isData = True
    from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import *

    dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"
    json=dataDir+'/json/json_DCSONLY.txt'
    #synche file DATA
    #comp = JetHT_Run2015B_PromptReco
    #comp.files = ['/afs/cern.ch/user/m/mangano/public/MECCA/dataset/74X/data/JetHT_promptReco_Run2015B.root']
    #comp.files = ['root://eoscms.cern.ch//eos/cms/store/data/Run2015B/JetHT/MINIAOD/PromptReco-v1/000/251/643/00000/0AF95D60-992C-E511-8D36-02163E0146A4.root']
    #selectedComponents = [comp]

    ##selectedComponents = [JetHT_Run2015B, HTMHT_Run2015B, MET_Run2015B, SingleElectron_Run2015B, SingleMuon_Run2015B, SinglePhoton_Run2015B, DoubleEG_Run2015B, DoubleMuon_Run2015B, MuonEG_Run2015B]
    #selectedComponents = [JetHT_Run2015B_17Jul2015, HTMHT_Run2015B_17Jul2015, MET_Run2015B_17Jul2015, SingleElectron_Run2015B_17Jul2015, SingleMuon_Run2015B_17Jul2015, SinglePhoton_Run2015B_17Jul2015, DoubleEG_Run2015B_17Jul2015, MuonEG_Run2015B_17Jul2015, DoubleMuon_Run2015B_17Jul2015, JetHT_Run2015B_PromptReco, HTMHT_Run2015B_PromptReco, MET_Run2015B_PromptReco, SingleElectron_Run2015B_PromptReco, SingleMuon_Run2015B_PromptReco, SinglePhoton_Run2015B_PromptReco, DoubleEG_Run2015B_PromptReco, MuonEG_Run2015B_PromptReco, DoubleMuon_Run2015B_PromptReco]

    #selectedComponents = [JetHT_Run2015D, HTMHT_Run2015D, MET_Run2015D, SingleElectron_Run2015D, SingleMuon_Run2015D, SinglePhoton_Run2015D, DoubleEG_Run2015D, MuonEG_Run2015D, DoubleMuon_Run2015D]
###    selectedComponents  = dataSamples_Run2015C_27Jan + [ SingleElectron_Run2015D_16Dec, DoubleEG_Run2015D_16Dec, MuonEG_Run2015D_16Dec, DoubleMuon_Run2015D_16Dec ]
#    selectedComponents = dataSamples_Run2015C_16Dec + [ SingleElectron_Run2015D_16Dec, SingleMuon_Run2015D_16Dec, DoubleEG_Run2015D_16Dec, MuonEG_Run2015D_16Dec, DoubleMuon_Run2015D_16Dec ] 
    selectedComponents  = [ DoubleMuon_Run2016B_PromptReco_v1 ]
    #selectedComponents  = [ SingleMuon_Run2016B_PromptReco_v1, SingleMuon_Run2016B_PromptReco_v2, DoubleMuon_Run2016B_PromptReco_v1, DoubleMuon_Run2016B_PromptReco_v2, DoubleEG_Run2016B_PromptReco_v1, DoubleEG_Run2016B_PromptReco_v2 ]

    for comp in selectedComponents:
        comp.json=json
        comp.files=comp.files[:]
        
elif test==4:

    from CMGTools.RootTools.samples.samples_13TeV_signals import *

### 25
    selectedComponents = + SignalSUSY + SignalEXO #+ SignalSUSYFullScan ###Signal Spring15
    
    # test all components (1 thread per component).
    for comp in selectedComponents:
        comp.splitFactor = 1200
        #comp.fineSplitFactor = 2 # to run two jobs per file
        comp.files = comp.files[:]
        # triggers on MC
        #comp.triggers = triggers_HT900 + triggers_HTMET + triggers_photon155 + triggers_1mu_isolow + triggers_MT2_mumu + triggers_MT2_ee + triggers_MT2_mue # to apply trigger skimming

# ------------------------------------------------------------------------------------------- #



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

# -------------------- Running Download from EOS

# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
event_class = EOSEventsWithDownload
if getHeppyOption("nofetch"):
    event_class = Events


if runPreprocessor:
    removeResiduals = False
    # -------------------- Running pre-processor
    import subprocess

    if isData:
        #    uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_50nsV4_DATA_UncertaintySources_AK4PFchs.txt'
        #    jecDBFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_50nsV4_DATA.db'
        #    jecEra    = 'Summer15_50nsV4_DATA'
        uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_DATA_UncertaintySources_AK4PFchs.txt'
        jecDBFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_DATA.db'
        jecEra    = 'Summer15_25nsV6_DATA'
    else:
        #    uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_50nsV4_DATA_UncertaintySources_AK4PFchs.txt'
        #    jecDBFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_50nsV4_MC.db'
        #    jecEra    = 'Summer15_50nsV4_MC'
        uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_MC_UncertaintySources_AK4PFchs.txt'
        jecDBFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_MC.db'
        jecEra    = 'Summer15_25nsV6_MC'
    preprocessorFile = "$CMSSW_BASE/tmp/MetType1_jec_%s.py"%(jecEra)
    extraArgs=[]
    if isData:
        extraArgs.append('--isData')
        GT= '74X_dataRun2_Prompt_v1'
    else:
        GT= 'MCRUN2_74_V9A'
    if removeResiduals:extraArgs.append('--removeResiduals')
    args = ['python',
            os.path.expandvars('$CMSSW_BASE/python/CMGTools/ObjectStudies/corMETMiniAOD_cfgCreator.py'),\
                '--GT='+GT,
            '--outputFile='+preprocessorFile,
            '--jecDBFile='+jecDBFile,
            '--uncFile='+uncFile,
            '--jecEra='+jecEra
            ] + extraArgs
    #print "Making pre-processorfile:"
    #print " ".join(args)
    subprocess.call(args)
    from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
    preprocessor = CmsswPreprocessor(preprocessorFile)


    config = cfg.Config( components = selectedComponents,
                         sequence = sequence,
                         services = [output_service],
                         preprocessor=preprocessor, # comment if pre-processor non needed
                         #                     events_class = event_class)
                         events_class = Events)
else:
    config = cfg.Config( components = selectedComponents,
                         sequence = sequence,
                         services = [output_service],
                         #                     events_class = event_class)
                         events_class = Events)


#printComps(config.components, True)
