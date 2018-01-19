from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
import itertools

class MT2Skimmer( Analyzer ):
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(MT2Skimmer,self).__init__(cfg_ana,cfg_comp,looperName)
        #self.ptCuts = cfg_ana.ptCuts if hasattr(cfg_ana, 'ptCuts') else []
        #self.ptCuts += 10*[-1.]

        #self.idCut = cfg_ana.idCut if (getattr(cfg_ana, 'idCut', '') != '') else "True"
        #self.idFunc = eval("lambda lepton : "+self.idCut);

        #self.requireSameSignPair = getattr(cfg_ana,"requireSameSignPair",False)

    def declareHandles(self):
        super(MT2Skimmer, self).declareHandles()

    def beginLoop(self, setup):
        super(MT2Skimmer,self).beginLoop(setup)
        self.counters.addCounter('events')
        count = self.counters.counter('events')
        count.register('all events')
        count.register('vetoed events')
        count.register('accepted events')


    def process(self, event):
        self.readCollections( event.input )
        self.counters.counter('events').inc('all events')

        
        nElectrons10 = sum([l.pt() > 10 and abs(l.pdgId()) == 11 for l in event.selectedLeptons])
        nMuons10 = sum([l.pt() > 10 and abs(l.pdgId()) == 13 for l in event.selectedLeptons])
        nPFLep5LowMT = event.nPFLep5LowMT
        nPFHad10LowMT = event.nPFHad10LowMT
        nLep = nElectrons10 + nMuons10 + nPFLep5LowMT + nPFHad10LowMT
        ht = event.htJetXj10l5t
        nJet30 = sum([j.pt() > 30 for j in event.cleanJets])
        mt2= event.mt2_Xj
        met_pt = event.met.pt()
        diffMetMht = event.diffMetMht_Xj
        deltaPhiMin = event.deltaPhiMin_Xj

        gamma_ht = event.gamma_htJetXj
        gamma_nJet30 = sum([j.pt() > 30 for j in event.gamma_cleanJets])
        gamma_mt2 = event.mt2_Xj_gamma
        gamma_met_pt = event.gamma_met.pt()

        zll_ht = event.zll_ht_Xj
        zll_mt2 = event.mt2_Xj_zll
        zll_met_pt = event.zll_met_pt

        ngamma = sum( [g.pt()>=20 for g in event.selectedPhotons])

        GGsignalSkim = ( ngamma>1 )

        signalSkim = ( (ht > 200 and nJet30 >= 1 and ( (nJet30>=2 and mt2>200.) or nJet30==1 ) ) 
                          and ((ht<1000. and met_pt>200.) or (ht>1000 and  met_pt>30)) )

        gammaSkim = (gamma_ht > 200 and gamma_nJet30 >= 1 
                     and ((gamma_nJet30>=2 and gamma_mt2>200.) or (gamma_nJet30==1 and gamma_ht>200.)) 
                     and ((gamma_ht<1000. and gamma_met_pt>200.)or(gamma_ht>1000 and  gamma_met_pt>30)) ) 

        zllSkim = (zll_ht > 200. and nJet30 >= 1 and ((nJet30==1 and zll_ht>200.) or (nJet30>1  and zll_mt2>200.)) 
                   and ((zll_ht<1000. and zll_met_pt>200.) or (zll_ht>1000 and  zll_met_pt>30)) )

        qcdSkim = ( (nJet30>1 and nLep==0 and met_pt > 30. and  (diffMetMht < 0.5*met_pt) and mt2>50. ) 
                    or 
                    (nJet30==2 and met_pt>200. and ht>200. and nLep==0 and diffMetMht < 0.5*met_pt and deltaPhiMin<0.3) 
                    )

        ret = ( signalSkim or gammaSkim or zllSkim or qcdSkim or GGsignalSkim )


        if ret: self.counters.counter('events').inc('accepted events')
        return ret
