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
lepAna.loose_muon_dxy = 0.2
lepAna.loose_muon_dz  = 0.5
lepAna.loose_muon_relIso  = 0.15
lepAna.loose_muon_isoCut = lambda muon :muon.miniRelIso < 0.2

lepAna.loose_electron_pt  = 5
lepAna.loose_electron_eta    = 2.4
lepAna.loose_electron_relIso = 0.15
lepAna.loose_electron_isoCut = lambda electron : electron.miniRelIso < 0.1

lepAna.loose_electron_id  = "POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto_full5x5"
lepAna.loose_electron_lostHits = 999. # no cut
lepAna.loose_electron_dxy    = 999.
lepAna.loose_electron_dz     = 999.

lepAna.inclusive_electron_id  = "POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto_full5x5"
lepAna.inclusive_electron_lostHits = 999. # no cut since embedded in ID
lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID

lepAna.mu_isoCorr = "deltaBeta"
lepAna.ele_isoCorr = "deltaBeta"
lepAna.ele_tightId = "Cuts_SPRING15_25ns_v1_ConvVetoDxyDz"
lepAna.notCleaningElectrons = True
lepAna.doMiniIsolation = True
lepAna.miniIsolationPUCorr = 'rhoArea'
lepAna.ele_effectiveAreas = 'Spring15_25ns_v1'             #new default 
lepAna.mu_effectiveAreas = 'Spring15_25ns_v1'              #new default
lepAna.rhoMuon= 'fixedGridRhoFastjetCentralNeutral',      #new default
lepAna.rhoElectron = 'fixedGridRhoFastjetCentralNeutral', #new default


lepAna.doIsoAnnulus = True

# JET (for event variables do apply the jetID and not PUID yet)
jetAna.relaxJetId = False
jetAna.doPuId = False
jetAna.doQG = True
jetAna.jetEta = 4.7
jetAna.jetEtaCentral = 2.5
jetAna.jetPt = 20. #was 10
jetAna.mcGT     = "Spring16_25nsV1_MC" # jec corrections
jetAna.dataGT   = "Spring16_25nsV1_MC" # jec corrections
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
photonAna.etaCentral = 2.5
photonAna.ptMin = 20
photonAna.gammaID = "POG_SPRING15_50ns_Loose_looseSieie_NoIso"
photonAna.do_randomCone = True
photonAna.do_mc_match = True

# Isolated Track
isoTrackAna.setOff=False
isoTrackAna.doIsoAnnulus = True

# recalibrate MET
metAna.recalibrate = 'type1' # 'type1' or False
metAna.old74XMiniAODs = False # get right Raw MET on old 74X MiniAODs

# store all taus by default
genAna.allGenTaus = True

# Core Analyzer
ttHCoreEventAna.mhtForBiasedDPhi = "mhtJetXjvec"
ttHCoreEventAna.jetPt = mt2JPt 

##------------------------------------------ 
##  CONTROL VARIABLES
##------------------------------------------ 

from CMGTools.TTHAnalysis.analyzers.ttHMT2Control import ttHMT2Control

ttHMT2Control = cfg.Analyzer(
            ttHMT2Control, name = 'ttHMT2Control',
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

MT2Ana = cfg.Analyzer(
    MT2Analyzer, name = 'MT2Analyzer',
    metCollection     = "slimmedMETs",
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
    "CSCTightHalo2015Filter" : [ "Flag_CSCTightHalo2015Filter" ],
    "EcalDeadCellTriggerPrimitiveFilter" : [ "Flag_EcalDeadCellTriggerPrimitiveFilter" ],
    "goodVertices" : [ "Flag_goodVertices" ],
    "eeBadScFilter" : [ "Flag_eeBadScFilter" ],
# filter under study 
    "globalTightHalo2016Filter" : [ "Flag_globalTightHalo2016Filter" ],
}


#-------- SEQUENCE

from CMGTools.TTHAnalysis.analyzers.treeProducerSusyFullHad import *
from CMGTools.TTHAnalysis.analyzers.treeProducerMT2forQCDStudies import *

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
    ttHMT2Control,
    MT2Ana,
    ttHTopoJetAna,
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
test = 3
#test = 2
isData = False # will be changed accordingly if chosen to run on data
doSpecialSettingsForMECCA = 1 # set to 1 for comparisons with americans
runPreprocessor = False




if test==0:
    # ------------------------------------------------------------------------------------------- #
    # --- all this lines taken from CMGTools.RootTools.samples.samples_13TeV_PHYS14
    # --- They may not be in synch anymore 
    from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
    kreator = ComponentCreator()
    testComponent = kreator.makeMCComponent("testComponent", "/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1/MINIAODSIM", "CMS", ".*root",489.9)
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
    #comp.files = ['root://xrootd.unl.edu//store/mc/RunIISpring16MiniAODv1/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1/00000/109B2CAB-1205-E611-A9BE-0CC47A0AD6C4.root']
        
    selectedComponents = [comp]
#    comp.splitFactor = 10
#    comp.fineSplitFactor = 100





elif test==1:
    # Uncomment the two following lines to run on a specific event
    #eventSelector.toSelect = [ 84142401 ]
    #sequence = cfg.Sequence([eventSelector] + sequence)
    
    from CMGTools.RootTools.samples.samples_13TeV_RunIIFall15MiniAODv2 import *


    selectedComponents = [TTJets_LO]
    for comp in selectedComponents:
        comp.files = ['root://xrootd.unl.edu//store/mc/RunIIFall15MiniAODv2/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/00000/00D010B5-1EB9-E511-B950-02163E014965.root']
        comp.splitFactor = 1200

#    comp.triggers = triggers_HT900 + triggers_HTMET + triggers_photon155 + triggers_1mu_isolow + triggers_MT2_mumu + triggers_MT2_ee + triggers_MT2_mue # to apply trigger skimming






elif test==2:

    from CMGTools.RootTools.samples.samples_13TeV_RunIISpring16MiniAODv1 import *
    # full production

    selectedComponents = [ 
        TTJets, 
        #TTJets_ext, 
        #TTJets_LO,
        #TT_pow_ext3, 
        #TT_pow_ext4, 
        TTJets_SingleLeptonFromTbar, 
        TTJets_SingleLeptonFromTbar_ext, 
        TTJets_SingleLeptonFromT, 
        #TTJets_SingleLeptonFromT_ext, 
        TTJets_DiLepton, 
        TTJets_DiLepton_ext, 
        #TTLep_pow, 
        #TTLep_pow_ext, 
        #TTJets_LO_HT600to800, 
        #TTJets_LO_HT600to800_ext, 
        #TTJets_LO_HT800to1200, 
        #TTJets_LO_HT800to1200_ext, 
        #TTJets_LO_HT1200to2500, 
        #TTJets_LO_HT1200to2500_ext, 
        #TTJets_LO_HT2500toInf,
        WJetsToLNu,
        WJetsToLNu_LO, 
        #DYJetsToLL_M10to50, 
        #DYJetsToLL_M10to50_ext1,
        ##DYJetsToLL_M5to50_LO, 
        #DYJetsToLL_M50, 
        DYJetsToLL_M50_LO, 
        #DYJetsToNuNu_M50,
        DYJetsToLL_M50_flatPu,
        DYJetsToLL_M50_HT100to200,
        DYJetsToLL_M50_HT200to400,
        #DYJetsToLL_M50_HT400to600,
        #DYJetsToLL_M50_HT600toInf,
        #WJetsToLNu_HT100to200,
        WJetsToLNu_HT100to200_ext,
        WJetsToLNu_HT200to400,
        WJetsToLNu_HT200to400_ext,
        WJetsToLNu_HT400to600,
        #WJetsToLNu_HT600toInf,
        WJetsToLNu_HT600to800,
        WJetsToLNu_HT800to1200,
        WJetsToLNu_HT800to1200_ext,
        WJetsToLNu_HT1200to2500,
        WJetsToLNu_HT2500toInf,
        GJets_HT40to100,
        GJets_HT100to200,
        GJets_HT200to400,
        GJets_HT400to600,
        GJets_HT600toInf,
        ZJetsToNuNu_HT100to200,
        ZJetsToNuNu_HT200to400,
        ZJetsToNuNu_HT200to400_ext,
        ZJetsToNuNu_HT400to600,
        ZJetsToNuNu_HT600to800,
        ZJetsToNuNu_HT800to1200,
        ZJetsToNuNu_HT1200to2500,
        ZJetsToNuNu_HT2500toInf,
        QCD_HT100to200,
        QCD_HT200to300,
        QCD_HT200to300_ext,
        QCD_HT300to500,
        QCD_HT300to500_ext,
        QCD_HT500to700,
        QCD_HT500to700_ext,
        QCD_HT700to1000,
        QCD_HT700to1000_ext,
        QCD_HT1000to1500,
        QCD_HT1000to1500_ext,
        QCD_HT1500to2000,
        QCD_HT2000toInf,
    ]


    for comp in selectedComponents:
        comp.splitFactor = 1200
        comp.fineSplitFactor = 4 # to run two jobs per file
        comp.files = comp.files[:]
        #comp.files = comp.files[:1]
        #comp.files = comp.files[57:58]  # to process only file [57]  
        # triggers on MC
        #comp.triggers = triggers_HT900 + triggers_HTMET + triggers_photon155 + triggers_1mu_isolow + triggers_MT2_mumu + triggers_MT2_ee + triggers_MT2_mue # to apply trigger skimming







elif test==3:
    # run on data

    # magic string to submit jobs via heppy_crab.py script:
    # python heppy_crab.py -c ../run_susyMT2_cfg.py --AAAconfig=full -s T3_CH_PSI -d crab -v MT2_8_0_5 -l data30May_v1 -u mt2.root,RLTInfo.root

    isData = True
    from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import *

    dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"
    json=dataDir+'/json/json_DCSONLY.txt'

    # Warning: this only works when running (e.g. locally) and having access to afs
    #json='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/DCSOnly/json_DCSONLY.txt' 

    #For synch on a single file
    #comp = JetHT_Run2016B_PromptReco_v1
    #comp.files = ['/afs/cern.ch/user/m/mangano/work/datasets/data/80X/HTMHT.root'
                  #'/scratch/mangano/80X/DoubleEG.root',
                  #'/scratch/mangano/80X/DoubleMuon.root',
                  #'/scratch/mangano/80X/HTMHT.root',
                  #'/scratch/mangano/80X/JetHT.root',
                  #'/scratch/mangano/80X/MET.root',
                  ##'/scratch/mangano/80X/MuonEG_v2.root',
                  #'/scratch/mangano/80X/SingleElectron.root',
                  #'/scratch/mangano/80X/SingleMuon.root',
                  #'/scratch/mangano/80X/SinglePhoton.root'
    #              ]
    #json='./testJson.txt'
    #selectedComponents = [comp]

    #For runnin on a single dataset
    #selectedComponents  = [JetHT_Run2016B_PromptReco_v2]


    #For running on the full list of samples
    selectedComponents  = dataSamples_Run2016B_PromptV2

    for comp in selectedComponents:
        comp.json=json
        comp.files=comp.files[:]
        comp.triggers = allTriggers

    # Here I add the skim to the sequence
    sequence.insert(sequence.index(treeProducer),
                        MT2skim)    
    

    # Tree configuration for QCD studies
    #treeProducer.globalVariables = MT2forQCDStudies_globalVariables
    #treeProducer.globalObjects = MT2forQCDStudies_globalObjects
    #treeProducer.collections = MT2forQCDStudies_collections


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


if doSpecialSettingsForMECCA:
    jetAna.doQG = False
    # photonAna.do_randomCone = False
    # Below slow things note: it will in any case try it only on MC, not on data
    # photonAna.do_mc_match = False
    # jetAna.do_mc_match = False
    lepAna.do_mc_match = False
    isoTrackAna.do_mc_match = False
    genAna.makeLHEweights = False

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
#from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
#event_class = EOSEventsWithDownload
#if getHeppyOption("nofetch"):
#    event_class = Events





##------------------------------------------------------------------------------
##  EVERYTHING THAT FOLLOWS IS FOR RUNNING PRE-PROCESSOR (turned off by default)
##------------------------------------------------------------------------------

#if runPreprocessor:
#    removeResiduals = False
#    # -------------------- Running pre-processor
#    import subprocess
#
#    if isData:
#        #    uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_50nsV4_DATA_UncertaintySources_AK4PFchs.txt'
#        #    jecDBFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_50nsV4_DATA.db'
#        #    jecEra    = 'Summer15_50nsV4_DATA'
#        uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_DATA_UncertaintySources_AK4PFchs.txt'
#        jecDBFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_DATA.db'
#        jecEra    = 'Summer15_25nsV6_DATA'
#    else:
#        #    uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_50nsV4_DATA_UncertaintySources_AK4PFchs.txt'
#        #    jecDBFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_50nsV4_MC.db'
#        #    jecEra    = 'Summer15_50nsV4_MC'
#        uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_MC_UncertaintySources_AK4PFchs.txt'
#        jecDBFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_MC.db'
#        jecEra    = 'Summer15_25nsV6_MC'
#    preprocessorFile = "$CMSSW_BASE/tmp/MetType1_jec_%s.py"%(jecEra)
#    extraArgs=[]
#    if isData:
#        extraArgs.append('--isData')
#        GT= '74X_dataRun2_Prompt_v1'
#    else:
#        GT= 'MCRUN2_74_V9A'
#    if removeResiduals:extraArgs.append('--removeResiduals')
#    args = ['python',
#            os.path.expandvars('$CMSSW_BASE/python/CMGTools/ObjectStudies/corMETMiniAOD_cfgCreator.py'),\
#                '--GT='+GT,
#            '--outputFile='+preprocessorFile,
#            '--jecDBFile='+jecDBFile,
#            '--uncFile='+uncFile,
#            '--jecEra='+jecEra
#            ] + extraArgs
#    #print "Making pre-processorfile:"
#    #print " ".join(args)
#    subprocess.call(args)
#    from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
#    preprocessor = CmsswPreprocessor(preprocessorFile)
#
#
#    config = cfg.Config( components = selectedComponents,
#                         sequence = sequence,
#                         services = [output_service],
#                         preprocessor=preprocessor, # comment if pre-processor non needed
#                         #                     events_class = event_class)
#                         events_class = Events)



#printComps(config.components, True)
