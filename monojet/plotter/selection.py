def build_selection(selection,bin0):

    selections = ['signal','Zmm','Wmn','gjets','Zee','Wen']
    
    snippets = {

        # Generic selections:
        #'runnumber'      :['runNum<=276811',selections], #ichep dataset 12.9
        'noisecleaning'  :['metfilter==1 && filterbadChCandidate==1 && filterbadPFMuon==1',selections],
        
        #monojet        
        'noisecleaning'  :['metfilter==1 ',selections],
        'leading jet pT' :['jet1Pt>100. ',selections],
        'leading jet eta':['abs(jet1Eta)<2.5',selections],        
        'jet cleaning'   :['jet1isMonoJetIdNew==1',selections],      
        'deltaPhi'       :['abs(minJetMetDPhi_withendcap) > 0.5',['signal','Zmm','Wmn','gjets','Wen','Zee']],
        'jetoutaccp'     :['leadingJet_outaccp==0',selections],
        'monoveto'       :['!(fatjet1Pt>250. && fatjet1tau21 < 0.6 && fatjet1PrunedM > 65 && met > 250. && fatjet1PrunedM < 105 && abs(fatjet1Eta)<2.4)',selections],
        
        #monoV
        #'leading jet pT'   :['fatjet1Pt>250.',selections],
        #'jet cleaning'     :['jet1isMonoJetIdNew==1',selections],      
        #'leading jet eta'  :['abs(fatjet1Eta)<2.4',selections],                                                      
        #'jet substrcuture' :['fatjet1tau21 < 0.6 ',selections], 
        #'mass'             :['fatjet1PrunedM > 65 && fatjet1PrunedM < 105',selections],
        #'deltaPhi'         :['abs(minJetMetDPhi_withendcap) > 0.5',['signal','Zmm','Wmn','gjets','Wen','Zee']],
        #'jetoutaccp'       :['leadingJet_outaccp==0',selections],
        
        #vbf
        #'jet eta'        :['jot1Eta*jot2Eta < 0',selections],
        #'deltaPhi'       :['abs(minJetMetDPhi_withendcap) > 0.5',selections],
        #'jet pT'         :['jot1Pt>80. && jot2Pt > 40. && abs(jot1Eta)<4.7 && abs(jot2Eta)<4.7',selections],
        #'detajj'         :['abs(jjDEta) > 4.5',selections],       
        #'horns'          :['(abs(jot1Eta)<3.1 ||  abs(jot1Eta)>3.3)',selections],
        #'new'            :['jot1Pt>80 && jot2Pt>40 && jjDEta>3.5 && abs(minJetMetDPhi_withendcap)>0.5 && mjj>1000 && (abs(jot1Eta)<3||abs(jot1Eta)>3.2) && TMath::Abs(deltaPhi(jot1Phi,jot2Phi)) < 1.5',selections],
        
        #'jet cleaning'   :['jet1isMonoJetIdNew==1',selections],      
        #'jetoutaccp'     :['leadingJet_outaccp==0',selections],
        
        # vbf baseline analysis
        #'jet eta'        :['jot1Eta*jot2Eta < 0',selections],
        #'jet pT'         :['jot1Pt>80. && jot2Pt > 70. && abs(jot1Eta)<4.7 && abs(jot2Eta)<4.7',selections],
        #'deltaPhi'       :['abs(minJetMetDPhi_withendcap) > 2.3',selections],
        #'detajj'         :['abs(jjDEta) > 3.6 && mjj>1100',selections],        
        #'horns'          :['(abs(jot1Eta)<3.0 ||  abs(jot1Eta)>3.2)',selections],

        #'jet cleaning'   :['jet1isMonoJetIdNew==1',selections],                                                                                                                                                   

        
        ####
        #'mjj'        :['mjj>500.',selections],
        #'isVBF'      :['IsVBF==1',selections],        
        
        ##########
        
        'track cleaning' :['(abs(caloMet-trueMet)/met) < 0.5',selection],
        'tau veto'       :['n_tau==0',selections], 
        'btag veto'      :['n_bjetsMedium==0',selections],
        'lepton veto'    :['n_looselep==0',['signal','gjets']],
        'pho veto'       :['n_loosepho==0',['signal','Zmm','Wmn','Zee','Wen']],
                
        #** Control Regions
        'leading lep ID': ['n_tightlep > 0',['Wmn','Zmm','Wen','Zee']], 

        #'Zmm'  : ['n_looselep == 2 && abs(dilep_m - 91) < 30 && (lep1PdgId*lep2PdgId == -169) && lep2Pt > 20. && lep1Pt>25.',['Zmm']],
        #'Zmm'  : ['n_looselep == 2 && abs(dilep_m - 91) < 30 && (lep1PdgId*lep2PdgId == -169) ',['Zmm']],
        #'Zmm'  : ['n_tightlep == 2 && abs(dilep_m - 91) < 30 && (lep1PdgId*lep2PdgId == -169) &&lep2Pt>20 && lep1Pt>20',['Zmm']],

        'Zmm'  : ['n_looselep == 2 && abs(dilep_m - 91) < 30 && (lep1PdgId*lep2PdgId == -169) ',['Zmm']],
        'Zee'  : ['n_looselep == 2 && abs(dilep_m - 91) < 30 && (lep1PdgId*lep2PdgId == -121)',['Zee']],
        #'Zee'  : ['n_looselep == 2 && abs(dilep_m - 91) < 30 && (lep1PdgId*lep2PdgId == -121) && lep2Pt>20 && lep1Pt>40',['Zee']],
        'Wmn'  : ['n_looselep == 1 && abs(lep1PdgId)==13 && mt<160',['Wmn']],
        'Wen'  : ['n_looselep == 1 && abs(lep1PdgId)==11 && trueMet>50. && mt<160.',['Wen']], 
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


# [0] HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v,
# [1] HLT_Ele23_WPLoose_Gsf_v,
# [2] HLT_Ele27_WPLoose_Gsf_v,
# [3] HLT_IsoTkMu20_v,
# [4] HLT_IsoMu24_v,
# [5] HLT_Mu50_v,
# [6] HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v,
# [7] HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v,
# [8] HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v,
# [9] HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v,
#[10] HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v,
#[11] HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v,
#[12] HLT_PFMET120_NoiseCleaned_BtagCSV0p72,
#[13] HLT_PFMET170_NoiseCleaned_v,
#[14] HLT_PFMET170_NotCleaned_v,
#[15] HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v,
#[16] HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_v,
#[17] HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v,
#[18] HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v,
#[19] HLT_Photon175_v,
#[20] HLT_Photon165_HE10_v,
#[21] HLT_PFHT400_SixJet30_BTagCSV0p55_2PFBTagCSV0p72_v,
#[22] HLT_PFHT450_SixJet40_PFBTagCSV0p72_v,
#[23] HLT_PFHT750_4JetPt50_v,HLT_PFHT650_v, --> Bug HERE!
#[24] HLT_PFHT800_v,
#[25] HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p45_v,
#[26] HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV0p45_v
