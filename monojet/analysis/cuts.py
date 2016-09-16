categories = ['monoJet_inc','monoV','monoJet','vbf']
regions    = ['signal','Zmm','Zee','Wmn','Wen','gjets']

metfilter_real = 'metfilter==1 && filterbadChCandidate==1 && filterbadPFMuon==1'
metfilter = 'metfilter==1 && filterbadChCandidate==1 && filterbadPFMuon==1'
#metfilter      = '(1.0)'

balance = '(abs(caloMet-trueMet)/met) < 0.5'

#monojet
met           = 'met>200'        
leadingjetpT  = 'jet1Pt>100.'
leadingjeteta = 'abs(jet1Eta)<2.5'
jetcleaning   = 'jet1isMonoJetIdNew==1'
deltaPhi      = 'abs(minJetMetDPhi_withendcap) > 0.5'
inversemonov  = '(fatjet1Pt<250. || fatjet1tau21 > 0.6 || fatjet1PrunedM < 65 || met < 250. || fatjet1PrunedM>105)'
jetoutofaccp  = 'leadingJet_outaccp==0'

monojet = str(balance+'&&'+met+'&&'+leadingjetpT+'&&'+leadingjeteta+'&&'+jetcleaning+'&&'+deltaPhi+'&&'+metfilter+'&&'+jetoutofaccp)

############

#monoV
metv              = 'met>250'        
leadingfatjetpT   = 'fatjet1Pt>250.'
leadingfatjeteta  = 'abs(fatjet1Eta)<2.4'
jetsubstructure   = 'fatjet1tau21 < 0.6 '
prunedmass        = 'fatjet1PrunedM > 65 && fatjet1PrunedM < 105'
        
monov    = str(balance+'&&'+metv+'&&'+leadingfatjetpT+'&&'+leadingfatjeteta+'&&'+jetsubstructure+'&&'+prunedmass+'&&'+deltaPhi+'&&'+jetcleaning+'&&'+metfilter+'&&'+jetoutofaccp)
monoveto = str(metv+'&&'+leadingfatjetpT+'&&'+leadingfatjeteta+'&&'+jetsubstructure+'&&'+prunedmass)

############
#vbf
vbfjetpT   = 'jot1Pt>100. && jot2Pt > 40. && abs(jot1Eta)<4.7 && abs(jot2Eta)<4.7'
vbfjeteta  = 'jot1Eta*jot2Eta < 0'
detajj     = 'abs(jjDEta) > 3.0'

vbf = str(balance+'&&'+met+'&&'+vbfjetpT+'&&'+vbfjeteta+'&&'+detajj+'&&'+deltaPhi+'&&'+metfilter+'&&'+jetoutofaccp)

############
tauveto    = 'n_tau==0'
btagveto   = 'n_bjetsMedium==0'
leptonveto = 'n_looselep==0'
phoveto    = 'n_loosepho==0'


#** Control Regions
leadinglepID = 'n_tightlep > 0'
Zmm_r   = '((n_looselep == 2 && abs(dilep_m - 91) < 30 && (lep1PdgId*lep2PdgId == -169)))'
Zee_r   = '((n_looselep == 2 && abs(dilep_m - 91) < 30 && (lep1PdgId*lep2PdgId == -121)))'
Wmn_r   = '((n_looselep == 1 && abs(lep1PdgId)==13 && mt<160))'
Wen_r   = '((n_looselep == 1 && abs(lep1PdgId)==11 && trueMet>50. && mt<160))'
gjets_r = '((photonPt > 175 && abs(photonEta) < 1.4442 && n_mediumpho == 1 && n_loosepho == 1))'

Zee  = str(Zee_r         + ' && ' + 
           phoveto       + ' && ' + 
           tauveto       + ' && ' + 
           btagveto      + ' && ' + 
           leadinglepID   
           )

Zmm  = str(Zmm_r         + ' && ' + 
           phoveto       + ' && ' + 
           tauveto       + ' && ' + 
           btagveto      + ' && ' + 
           leadinglepID  
           )

Wen  = str(Wen_r         + ' && ' + 
           phoveto       + ' && ' + 
           tauveto       + ' && ' + 
           btagveto      + ' && ' + 
           leadinglepID  
           )

Wmn  = str(Wmn_r         + ' && ' + 
           phoveto       + ' && ' + 
           tauveto       + ' && ' + 
           btagveto      + ' && ' + 
           leadinglepID  
           )

gjet = str(gjets_r       + ' && ' + 
           leptonveto    + ' && ' + 
           tauveto       + ' && ' + 
           btagveto      
           )

signal = str(phoveto       + ' && ' + 
             tauveto       + ' && ' + 
             btagveto      + ' && ' + 
             leptonveto   
             )


categoryCuts = {
    'monoJet_inc' : monojet,
    'monoV' : monov,
    'vbf'   : vbf,
    'monoJet' : monojet + ' && !(' + monoveto + ')',
    }

regionCuts = {
    'signal' : signal,
    'Zmm'    : Zmm,
    'Zee'    : Zee,
    'Wmn'    : Wmn,
    'Wen'    : Wen,
    'gjets'  : gjet
    }

defaultMCWeight = 'mcWeight'

#first one is the cut, second one is the SF

#additionKeys = ['default']
additionKeys = []
#additionKeys = ['signal','Zmm','Wmn','Zee','Wen','gjets']
additions    = { # key : [Data,MC]
    #'signal' :  [metfilter_real,defaultMCWeight],
    #'Zmm' :     [metfilter_real,defaultMCWeight],
    #'Wmn' :     [metfilter_real,defaultMCWeight],
    #'Zee' :     [metfilter_real,defaultMCWeight],
    #'Wen' :     [metfilter_real,defaultMCWeight],
    #'gjets':    [metfilter_real,defaultMCWeight]
    #'default' : [metfilter_real,defaultMCWeight]
    'default' : ['',defaultMCWeight]
    }

def cut(category, region):
    print category, region, '((' + categoryCuts[category] + ') && (' + regionCuts[region] + '))'
    return '((' + categoryCuts[category] + ') && (' + regionCuts[region] + '))'

def dataMCCuts(region, isData):
    key = 'default'
    index = 1
    if region in additionKeys:
        key = region

    if isData:
        index = 0

    if key == 'default' or index == 0:
        return '(' + additions[key][index] + ')'
    else:
        return '((' + additions[key][index] + ')*(' + defaultMCWeight + '))'
