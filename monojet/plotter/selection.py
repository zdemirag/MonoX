def build_selection(selection,bin0):

    selections = ['signal','Zmm','Wmn','gjets','Zee','Wen']
    
    snippets = {
        
        #monojet        
        #'leading jet pT' :['jet1Pt>100.',selections],
        #'leading jet eta':['abs(jet1Eta)<2.5',selections],        
        #'jet cleaning'   :['jet1isMonoJetIdNew==1',selections],      
        #'deltaPhi'       :['abs(minJetMetDPhi_withendcap) > 0.5',['signal','Zmm','Wmn','gjets','Wen']],
        #'inversemonov'   :['(fatjet1Pt<250. || fatjet1tau21 > 0.6 || fatjet1PrunedM < 65 || met < 250. || fatjet1PrunedM>105)',selections],
        
        #monoV
        #'leading jet pT'   :['fatjet1Pt>250.',selections],
        #'leading jet eta'  :['abs(fatjet1Eta)<2.4',selections],                                                      
        #'jet substrcuture' :['fatjet1tau21 < 0.6 ',selections], 
        #'mass'             :['fatjet1PrunedM > 65 && fatjet1PrunedM < 105',selections],
        
        #vbf
        'deltaPhi' :['abs(minJetMetDPhi) > 2.3',['signal','Zmm','Wmn','gjets','Wen']],
        #'deltaPhi' :['abs(minJetMetDPhi_withendcap) > 2.3',['signal','Zmm','Wmn','gjets','Wen']],
        'jet pT'   :['jot1Pt>80. && jot2Pt > 40. && abs(jot1Eta)<4.7 && abs(jot2Eta)<4.7',selections],
        'jet eta'  :['jot1Eta*jot2Eta < 0',selections],
        'detajj'   :['abs(jjDEta) > 3.5',selections],
        'mjj'      :['mjj>600.',selections],
        #'isVBF'    :['IsVBF==1',selections],
        

        ##########
        
        'tau veto'       :['n_tau==0',selections], 
        'btag veto'      :['n_bjetsMedium==0',selections],
        'lepton veto'    :['n_looselep==0',['signal','gjets']],
        'pho veto'       :['n_loosepho==0',['signal','Zmm','Wmn','Zee','Wen']],
                
        #** Control Regions
        'triggerE'  : ['((triggerFired[0]==1))',['Zee','Wen']],    
        'triggerG'  : ['((triggerFired[14]==1 || triggerFired[13]==1))',['gjets']],
        #'trigger'   : ['((triggerFired[4]==1) || (triggerFired[5]==1) || (triggerFired[6]==1))',['Zmm','Wmn','signal']],
        'leading lep ID': ['n_tightlep > 0',['Wmn','Zmm','Wen','Zee']], 
        'Zmm'  : ['n_looselep == 2 && abs(dilep_m - 91) < 30 && (lep1PdgId*lep2PdgId == -169)',['Zmm']],
        'Zee'  : ['n_looselep == 2 && abs(dilep_m - 91) < 30 && (lep1PdgId*lep2PdgId == -121)',['Zee']],
        'Wmn'  : ['n_looselep == 1 && abs(lep1PdgId)==13 ',['Wmn']],
        'Wen'  : ['n_looselep == 1 && abs(lep1PdgId)==11 && trueMet>50.',['Wen']],
        'gjets': ['photonPt > 175 && abs(photonEta) < 1.4442 && n_mediumpho == 1 && n_loosepho == 1',['gjets']],                
        
        }

    selectionString = ''
    for cut in snippets:
        if selection in snippets[cut][1]: 
            selectionString += snippets[cut][0]+'&&'

    met  = 'met'

    analysis_bin = {}
    analysis_bin[0] = bin0

    selectionString+=met+'>'+str(analysis_bin[0])

    return selectionString

