from CMGTools.TTHAnalysis.analyzers.treeProducerSusyCore import *
from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *

MT2forQCDStudies_globalVariables = susyCore_globalVariables + [
        
    ##--------------------------------------------------
    ## energy sums
    ##--------------------------------------------------
    NTupleVariable("ht", lambda ev : ev.htJetXj10l5t, help="H_{T} computed from jets (with |eta|<2.5, pt > 40 GeV) and leptons (electrons and muons with |eta|<2.5, pt > 10 GeV)"),
    NTupleVariable("mht_pt", lambda ev : ev.mhtJetXj10l5t, help="H_{T}^{miss} computed from jets (with |eta|<2.5, pt > 40 GeV) and leptons (electrons ans muons with |eta|<2.5, pt > 10 GeV)"),
    NTupleVariable("mht_phi", lambda ev : ev.mhtPhiJetXj10l5t, help="H_{T}^{miss} #phi computed from jets (with |eta|<2.5, pt > 40 GeV) and leptons (electrons ans muons with |eta|<2.5, pt > 10 GeV)"),
    NTupleVariable("diffMetMht", lambda ev : ev.diffMetMht_Xj, help="abs( vec(mht) - vec(met) ) - with jets and leptons"),
    NTupleVariable("deltaPhiMin", lambda ev : ev.deltaPhiMin_Xj, help="minimal deltaPhi between the MET and the four leading jets with pt>40 and eta<2.4 and leptons (electrons ans muons with |eta|<2.5, pt > 10 GeV)"),
    

    ##--------------------------------------------------
    # Physics object multplicities
    ##--------------------------------------------------
    
    NTupleVariable("nJet20", lambda ev: sum([j.pt() > 20 for j in ev.cleanJets]), int, help="Number of jets with pt > 20, |eta|<2.4"),
    NTupleVariable("nJet20a", lambda ev: sum([j.pt() > 20 for j in ev.cleanJetsAll]), int, help="Number of jets with pt > 20, |eta|<4.7"),
    NTupleVariable("nBJetLoose20", lambda ev: sum([j.btagWP("CSVv2IVFL") for j in ev.cleanJets if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CSV loose"),
    NTupleVariable("nBJetMedium20", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.bjetsMedium if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CSV medium"),
    NTupleVariable("nBJetTight20", lambda ev: sum([j.btagWP("CSVv2IVFT") for j in ev.bjetsMedium if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CSV tight"),

    NTupleVariable("nJet20FailId", lambda ev: sum([j.pt() > 20 for j in ev.cleanJetsFailIdAll]), int, help="Number of jets after photon-cleaning with pt > 20, |eta|<4.7"),
    NTupleVariable("nJet25FailId", lambda ev: sum([j.pt() > 25 for j in ev.cleanJetsFailIdAll]), int, help="Number of jets after photon-cleaning with pt > 25, |eta|<4.7"),
    NTupleVariable("nJet30FailId", lambda ev: sum([j.pt() > 30 for j in ev.cleanJetsFailIdAll]), int, help="Number of jets after photon-cleaning with pt > 30, |eta|<4.7"),
    NTupleVariable("nJet100FailId", lambda ev: sum([j.pt() > 100 for j in ev.cleanJetsFailIdAll]), int, help="Number of jets after photon-cleaning with pt > 100, |eta|<4.7"),

    NTupleVariable("nBJet40", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 40]), int, help="Number of jets with pt > 40 passing CSV medium"),
    NTupleVariable("nBJet30", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 30]), int, help="Number of jets with pt > 25 passing CSV medium"),
    NTupleVariable("nBJet25", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 25]), int, help="Number of jets with pt > 25 passing CSV medium"),
    NTupleVariable("nBJet20", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CSV medium"),

    NTupleVariable("nMuons10", lambda ev: sum([l.pt() > 10 and abs(l.pdgId()) == 13 for l in ev.selectedLeptons]), int, help="Number of muons with pt > 10"),
    NTupleVariable("nElectrons10", lambda ev: sum([l.pt() > 10 and abs(l.pdgId()) == 11 for l in ev.selectedLeptons]), int, help="Number of electrons with pt > 10"),
    NTupleVariable("nTaus20", lambda ev: sum([l.pt() > 20 for l in ev.selectedTaus]), int, help="Number of taus with pt > 20"),
    NTupleVariable("nGammas20", lambda ev: sum([l.pt() > 20 for l in ev.selectedPhotons]), int, help="Number of photons with pt > 20"),
    
    NTupleVariable("minMTBMet", lambda ev: ev.minMTBMet, float, help="min Mt(b,met)"),
    NTupleVariable("nPFLep5LowMT", lambda ev: ev.nPFLep5LowMT, int, help="number of PF leptons (e,mu) with pt > 5, reliso < 0.2, MT < 100 "),
    NTupleVariable("nPFHad10LowMT", lambda ev: ev.nPFHad10LowMT, int, help="number of PF hadrons with pt > 10, reliso < 0.1, MT < 100 "),
    NTupleVariable("nLepLowMT", lambda ev: ev.nLepLowMT, int, help="number of leptons (POGID and isoTrack ) with MT < 100 "),

    ##--------------------------------------------------
    # MT2
    ##--------------------------------------------------
    NTupleVariable("mt2", lambda ev: ev.mt2_Xj, float, help="mt2(j1,j2,met) with jets and leptons"),
]

MT2forQCDStudies_globalObjects = susyCore_globalObjects.copy()
MT2forQCDStudies_globalObjects.update({})


MT2forQCDStudies_collections = {}            
