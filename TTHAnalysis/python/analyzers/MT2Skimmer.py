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

        
        ret = False 
        
        ht = event.htJetXj10l5t
        nJet30 = sum([j.pt() > 30 for j in event.cleanJets])
        mt2= event.mt2_Xj
        met_pt = event.met.pt()

        gamma_ht = event.gamma_htJetXj
        gamma_nJet30 = sum([j.pt() > 30 for j in event.gamma_cleanJets])
        gamma_mt2 = event.mt2_Xj_gamma
        gamma_met_pt = event.gamma_met.pt()

        zll_ht = event.zll_ht_Xj
        zll_mt2 = event.mt2_zll
        zll_met_pt = event.zll_met_pt

        #QCD skim to be added in OR next time
        #skimmingSelection="isGolden && ((nJet30>1 && nlep==0 && met_pt > 30. &&  (diffMetMht < 0.5*met_pt) && mt2>50. ))"


        test = (
            ( (ht > 200 and nJet30 >= 1 and ( (nJet30>=2 and mt2>200.) or nJet30==1 ) ) and ((ht<1000. and met_pt>200.)
               or (ht>1000 and  met_pt>30)) ) 
            or 
            (gamma_ht > 200 and gamma_nJet30 >= 1 and ((gamma_nJet30>=2 and gamma_mt2>200.) or (gamma_nJet30==1 and gamma_ht>200.)) and ((gamma_ht<1000. and gamma_met_pt>200.)or(gamma_ht>1000 and  gamma_met_pt>30))) 
            or
            (zll_ht > 200. and nJet30 >= 1 and ((nJet30==1 and zll_ht>200.) or (nJet30>1  and zll_mt2>200.)) and ((zll_ht<1000. and zll_met_pt>200.)or(zll_ht>1000 and  zll_met_pt>30)))
        )

        ret = test

        if ret: self.counters.counter('events').inc('accepted events')
        return ret
