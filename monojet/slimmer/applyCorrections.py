#! /usr/bin/python

from CrombieTools.SkimmingTools import Corrector
import os,sys

directory = sys.argv[1]

applicator = Corrector.MakeApplicator('mcFactors',True,'events','events',100000)

def addCorr(name,expr,cut,fileName,histName):
    applicator.AddCorrector(Corrector.MakeCorrector(name,expr,cut,fileName,histName))
##

addCorr('puWeight','npv','1','files/puWeight_13invfb.root','hPU')

#####################
## Loose electron
addCorr('lepton_SF1',['abs(lep1Eta)','lep1Pt'],'!(lep1IsMedium || lep1IsTight) && lep1Pt > 0 && abs(lep1PdgId) == 11',
        'files/scaleFactor_electron_vetoid_12p9.root','scaleFactor_electron_vetoid_RooCMSShape')
addCorr('lepton_SF2',['abs(lep2Eta)','lep2Pt'],'!(lep2IsMedium || lep2IsTight) && lep2Pt > 0 && abs(lep2PdgId) == 11',
        'files/scaleFactor_electron_vetoid_12p9.root','scaleFactor_electron_vetoid_RooCMSShape')
## Tight electron
addCorr('lepton_SF1',['abs(lep1Eta)','lep1Pt'],'lep1IsTight && lep1Pt > 0 && abs(lep1PdgId) == 11',
        'files/scaleFactor_electron_tightid_12p9.root','scaleFactor_electron_tightid_RooCMSShape')
addCorr('lepton_SF2',['abs(lep2Eta)','lep2Pt'],'lep2IsTight && lep2Pt > 0 && abs(lep2PdgId) == 11',
        'files/scaleFactor_electron_tightid_12p9.root','scaleFactor_electron_tightid_RooCMSShape')

#######################
## Loose muon
addCorr('lepton_SF1',['abs(lep1Eta)','lep1Pt'],'!(lep1IsMedium || lep1IsTight) && lep1Pt > 0 && abs(lep1PdgId) == 13',
        'files/scaleFactor_muon_looseid_12p9.root','scaleFactor_muon_looseid_RooCMSShape')
addCorr('lepton_SF2',['abs(lep2Eta)','lep2Pt'],'!(lep2IsMedium || lep2IsTight) && lep2Pt > 0 && abs(lep2PdgId) == 13',
        'files/scaleFactor_muon_looseid_12p9.root','scaleFactor_muon_looseid_RooCMSShape')

## Tight Muon
addCorr('lepton_SF1',['abs(lep1Eta)','lep1Pt'],'lep1IsTight && lep1Pt > 0 && abs(lep1PdgId) == 13',
        'files/scaleFactor_muon_tightid_12p9.root','scaleFactor_muon_tightid_RooCMSShape')
addCorr('lepton_SF2',['abs(lep2Eta)','lep2Pt'],'lep2IsTight && lep2Pt > 0 && abs(lep2PdgId) == 13',
        'files/scaleFactor_muon_tightid_12p9.root','scaleFactor_muon_tightid_RooCMSShape')

########################
##Photon SF
addCorr('photon_SF',['abs(photonEta)','photonPt'],'n_mediumpho==1 && photonPt > 0 && abs(photonEta) <= 1.4442','files/scaleFactor_photon_mediumid_12p9.root','scaleFactor_photon_mediumid_RooCMSShape')

#######################
##Tracking eff

addCorr('tracking_SF1',['npv'],'lep1Pt > 0 && abs(lep1PdgId) == 13','files/Tracking_12p9.root','htrack2')
addCorr('tracking_SF2',['npv'],'lep2Pt > 0 && abs(lep2PdgId) == 13','files/Tracking_12p9.root','htrack2')

addCorr('gsfTracking_SF1',['lep1Eta','npv'],'lep1Pt > 0 && abs(lep1PdgId) == 11','files/egammaEffi_nVtx_SF2D.root','EGamma_SF2D')
addCorr('gsfTracking_SF2',['lep2Eta','npv'],'lep2Pt > 0 && abs(lep2PdgId) == 11','files/egammaEffi_nVtx_SF2D.root','EGamma_SF2D')

#######################
## Triggers
addCorr('METTrigger','met','1','files/METTrigger_12p9.root','numer')

addCorr('EleTrigger_w1',['abs(lep1Eta)','lep1Pt'],'lep1IsTight && lep1Pt > 0 && lep1Pt < 100 && abs(lep1PdgId) == 11','files/eleTrig.root','hEffEtaPt')
addCorr('EleTrigger_w2',['lep1Pt'],'lep1IsTight && lep1Pt >= 100 && abs(lep1PdgId) == 11 && abs(lep1Eta)>=1.4442 ','files/ele_trig_endcap.root','h_num_s')
addCorr('EleTrigger_w3',['lep1Pt'],'lep1IsTight && lep1Pt >= 100 && abs(lep1PdgId) == 11 && abs(lep1Eta)<1.4442 ','files/ele_trig_barrel.root','h_num')

addCorr('EleTrigger_w2_Recover',['lep1Pt'],'lep1IsTight && lep1Pt >= 100 && abs(lep1PdgId) == 11 && abs(lep1Eta)>=1.4442 ','files/ele_trig_endcap_recovery.root','h_num_s')
addCorr('EleTrigger_w3_Recover',['lep1Pt'],'lep1IsTight && lep1Pt >= 100 && abs(lep1PdgId) == 11 && abs(lep1Eta)<1.4442 ','files/ele_trig_barrel_recovery.root','h_num')

addCorr('PhoTrigger',['photonPt'],' n_mediumpho==1 && photonPt > 0 && abs(photonEta) < 1.4442 ','files/pho_trig.root','h_num')
addCorr('PhoTrigger_Recover',['photonPt'],' n_mediumpho==1 && photonPt > 0 && abs(photonEta) < 1.4442 ','files/pho_trig_recovery.root','h_num')

########################

applicator.AddFactorToMerge('mcWeight')

ewk_a = Corrector.MakeCorrector('ewk_a','genBos_pt','genBos_PdgId == 22','files/uncertainties_EWK_24bins.root',['EWKcorr/photon','GJets_1j_NLO/nominal_G'])
ewk_z = Corrector.MakeCorrector('ewk_z','genBos_pt','abs(genBos_PdgId) == 23','files/uncertainties_EWK_24bins.root',['EWKcorr/Z','ZJets_012j_NLO/nominal'])
ewk_w = Corrector.MakeCorrector('ewk_w','genBos_pt','abs(genBos_PdgId) == 24','files/uncertainties_EWK_24bins.root',['EWKcorr/W','WJets_012j_NLO/nominal'])

akfactor = Corrector.MakeCorrector('akfactor','genBos_pt','genBos_PdgId == 22','files/uncertainties_EWK_24bins.root',['GJets_1j_NLO/nominal_G','GJets_LO/inv_pt_G'])
zkfactor = Corrector.MakeCorrector('zkfactor','genBos_pt','abs(genBos_PdgId) == 23','files/uncertainties_EWK_24bins.root',['ZJets_012j_NLO/nominal','ZJets_LO/inv_pt'])
wkfactor = Corrector.MakeCorrector('wkfactor','genBos_pt','abs(genBos_PdgId) == 24','files/uncertainties_EWK_24bins.root',['WJets_012j_NLO/nominal','WJets_LO/inv_pt'])

applicator.AddCorrector(ewk_a)
applicator.AddCorrector(ewk_z)
applicator.AddCorrector(ewk_w)
applicator.AddCorrector(akfactor)
applicator.AddCorrector(zkfactor)
applicator.AddCorrector(wkfactor)

a_ = { 'cut'   : 'genBos_PdgId == 22',
       'list'  : ['GJets'],
       'apply' : [ewk_a,akfactor] }
z_1 = { 'cut'   : 'abs(genBos_PdgId) == 23',
       'list'  : ['DYJetsToLL','ZJets'],
       'apply' : [zkfactor] }
z_2 = { 'cut'   : 'abs(genBos_PdgId) == 23',
       'list'  : ['DYJets','ZJets'],
       'apply' : [ewk_z] }
w_ = { 'cut'   : 'abs(genBos_PdgId) == 24',
       'list'  : ['WJets'],
       'apply' : [ewk_w,wkfactor] }

for fileName in os.listdir(directory):
    if not '.root' in fileName:
        continue
    ##

    for corrector in [ewk_a,ewk_z,ewk_w,akfactor,zkfactor,wkfactor]:
        corrector.SetInCut('runNum == 0')
    ##

    for checker in [a_,z_1,z_2,w_]:
        for testName in checker['list']:
            if testName in fileName:
                for corrector in checker['apply']:
                    corrector.SetInCut(checker['cut'])
                ##
            ##
        ##
    ##
    
    applicator.ApplyCorrections(directory + "/" + fileName)
##
