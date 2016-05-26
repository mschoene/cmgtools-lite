from CMGTools.TTHAnalysis.analyzers.treeProducerSusyCore import *
from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *

zgamma_globalVariables = [

    NTupleVariable("rho",  lambda ev: ev.rho, float, help="kt6PFJets rho"),
    NTupleVariable("rhoCN",  lambda ev: ev.rhoCN, float, help="fixed grid rho central neutral"),
    NTupleVariable("nVert",  lambda ev: len(ev.goodVertices), int, help="Number of good vertices"), 

##    NTupleVariable("genQScale", lambda ev : ev.genQScale, help="Generator level binning quantity, QScale"),
    NTupleVariable("LHEweight_original", lambda ev: ev.LHE_originalWeight if  hasattr(ev,'LHE_originalWeight') else  0, mcOnly=True, help="original LHE weight"),

#
    NTupleVariable("nMuons10", lambda ev: sum([l.pt() > 10 and abs(l.pdgId()) == 13 for l in ev.selectedLeptons]), int, help="Number of muons with pt > 10"),
    NTupleVariable("nElectrons10", lambda ev: sum([l.pt() > 10 and abs(l.pdgId()) == 11 for l in ev.selectedLeptons]), int, help="Number of electrons with pt > 10"),
    #NTupleVariable("nTaus20", lambda ev: sum([l.pt() > 20 for l in ev.selectedTaus]), int, help="Number of taus with pt > 20"),
    NTupleVariable("nGammas20", lambda ev: sum([l.pt() > 20 for l in ev.selectedPhotons]), int, help="Number of photons with pt > 20"),


]


zgamma_globalObjects = susyCore_globalObjects.copy()

#zgamma_collections = susyCore_collections.copy()
#zgamma_collections.update({
zgamma_collections = {
        "genleps"         : NTupleCollection("genLep",     genParticleWithLinksType, 10, help="Generated leptons (e/mu) from W/Z decays", filter=lambda l : l.motherId>=22 and l.motherId<=25 and (l.status()==1 or l.status()==23)),
        #"gentauleps"      : NTupleCollection("genLepFromTau", genParticleWithLinksType, 10, help="Generated leptons (e/mu) from decays of taus from W/Z/h decays"),
        #"gentaus"         : NTupleCollection("genTau",     genParticleWithLinksType, 10, help="Generated leptons (tau) from W/Z decays"),
        "generatorSummary" : NTupleCollection("GenPart", genParticleWithLinksType, 100 , help="Hard scattering particles, with ancestry and links"),
        # put more here
##        "gennus"         : NTupleCollection("genNu",     genParticleWithSourceType, 10, help="Generated neutrinos (nue/numu/nutau) from W/Z decays"),
#        "selectedLeptons" : NTupleCollection("lep", leptonType, 50, help="Leptons after the preselection", filter=lambda l : l.pt()>10 ),
        "selectedLeptons" : NTupleCollection("lep", leptonTypeSusy, 50, help="Leptons after the preselection", filter=lambda l : l.pt()>10 ),
        #"selectedTaus"    : NTupleCollection("tau", tauTypeSusy, 50, help="Taus after the preselection"),
        "cleanJetsAll"       : NTupleCollection("jet", jetTypeSusyExtra, 100, help="all jets (w/ x-cleaning, w/ ID applied w/o PUID applied pt>20 |eta|<5.2) , sorted by pt", filter=lambda l : l.pt()>20  ),
        "cleanJetsFailIdAll"       : NTupleCollection("jetFailId", jetTypeSusyExtra, 100, help="all jets (w/ x-cleaning, w/o ID applied w/o PUID applied pt>20 |eta|<5.2) , sorted by pt", filter=lambda l : l.pt()>20 ),
##        "cleanJetsAll"       : NTupleCollection("jet",   jetTypeExtra, 100, help="all jets (w/ x-cleaning, w/ ID applied w/o PUID applied pt>10 |eta|<5.2) , sorted by pt", filter=lambda l : l.pt()>25  ),
        "selectedPhotons"    : NTupleCollection("gamma", photonTypeSusy, 50, help="photons with pt>20 and loose cut based ID"),
        "genParticles" : NTupleCollection("genPart", genParticleWithMotherId, 300, help="all pruned genparticles"),
##        "ivf"       : NTupleCollection("SV",     svType, 20, help="SVs from IVF", filter=lambda l : l.pt()>5),
        "LHE_weights"    : NTupleCollection("LHEweight",  weightsInfoType, 1000, help="LHE weight info"),
}            
