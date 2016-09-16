#! /usr/bin/python

from CrombieTools.AnalysisTools.LimitTreeMaker import *

ltm = newLimitTreeMaker()

SetupFromEnv(ltm)

ltm.SetTreeName('events')
ltm.AddKeepBranch('met')
ltm.AddKeepBranch('genBos_pt')

ltm.SetAllHistName('htotal')

ltm.AddWeightBranch('puWeight')
ltm.AddWeightBranch('topPtReweighting')
ltm.AddWeightBranch('ewk_z')
ltm.AddWeightBranch('ewk_a')
ltm.AddWeightBranch('ewk_w')

ltm.AddWeightBranch('akfactor')
ltm.AddWeightBranch('zkfactor')

ltm.AddExceptionWeightBranch('Wen','lepton_SF1')
ltm.AddExceptionWeightBranch('Wmn','lepton_SF1')

ltm.AddExceptionWeightBranch('Zee','lepton_SF1')
ltm.AddExceptionWeightBranch('Zmm','lepton_SF1')
ltm.AddExceptionWeightBranch('Zee','lepton_SF2')
ltm.AddExceptionWeightBranch('Zmm','lepton_SF2')

ltm.AddExceptionWeightBranch('Wmn','tracking_SF1')
ltm.AddExceptionWeightBranch('Zmm','tracking_SF1')
ltm.AddExceptionWeightBranch('Zmm','tracking_SF2')

ltm.AddExceptionWeightBranch('Wen','gsfTracking_SF1')
ltm.AddExceptionWeightBranch('Zee','gsfTracking_SF1')
ltm.AddExceptionWeightBranch('Zee','gsfTracking_SF2')

ltm.AddExceptionWeightBranch('Wen','EleTrigger_w1')
ltm.AddExceptionWeightBranch('Wen','EleTrigger_w2')
#ltm.AddExceptionWeightBranch('Wen','EleTrigger_w3')

ltm.AddExceptionWeightBranch('gjets','PhoTrigger')
ltm.AddExceptionWeightBranch('gjets','photon_SF')

ltm.AddExceptionWeightBranch('Wmn','METTrigger')
ltm.AddExceptionWeightBranch('Zmm','METTrigger')
ltm.AddExceptionWeightBranch('signal','METTrigger')


#ltm.AddExceptionWeightBranch('signal','zvv_scale2')
#ltm.AddExceptionWeightBranch('Wmn','wmn_scale2')
#ltm.AddExceptionWeightBranch('Wen','wen_scale2')
#ltm.AddExceptionWeightBranch('Zmm','zmm_scale2')
#ltm.AddExceptionWeightBranch('Zee','zee_scale2')
#ltm.AddExceptionWeightBranch('gjets','pho_scale2')

ltm.ExceptionSkip('gjets','data')
ltm.ExceptionSkip('Zmm','data')
ltm.ExceptionSkip('Zee','data')
ltm.ExceptionSkip('Wen','data')
ltm.ExceptionSkip('Wmn','data')
ltm.ExceptionSkip('signal','data')

ltm.ExceptionAdd('gjets' ,str(ltm.GetInDirectory()) + 'monojet_SinglePhoton.root','data',-1)  
ltm.ExceptionAdd('Zee'   ,str(ltm.GetInDirectory()) + 'monojet_SingleElectron.root','data',-1)  
ltm.ExceptionAdd('Wen'   ,str(ltm.GetInDirectory()) + 'monojet_SingleElectron.root','data',-1)  
ltm.ExceptionAdd('Zmm'   ,str(ltm.GetInDirectory()) + 'monojet_MET.root','data',-1)  
ltm.ExceptionAdd('Wmn'   ,str(ltm.GetInDirectory()) + 'monojet_MET.root','data',-1)  
ltm.ExceptionAdd('signal',str(ltm.GetInDirectory()) + 'monojet_MET.root','data',-1)  

ltm.AddExceptionDataCut('signal',"metfilter==1 && (triggerFired[10]==1 || triggerFired[11] == 1 || triggerFired[12] || triggerFired[13] == 1)")
ltm.AddExceptionDataCut('gjets',"metfilter==1  && (triggerFired[18] || triggerFired[19] || triggerFired[17] || triggerFired[5] || triggerFired[15] || triggerFired[16] || triggerFired[26])")
ltm.AddExceptionDataCut('Zee',"metfilter==1 && (triggerFired[0] || triggerFired[1] || triggerFired[2] || triggerFired[3] || triggerFired[4] || triggerFired[5] || triggerFired[26])")
ltm.AddExceptionDataCut('Wen',"metfilter==1 && (triggerFired[0] || triggerFired[1] || triggerFired[2] || triggerFired[3] || triggerFired[4] || triggerFired[5] || triggerFired[26])")
ltm.AddExceptionDataCut('Zmm',"metfilter==1 && (triggerFired[10]==1 || triggerFired[11] == 1 || triggerFired[12] || triggerFired[13] == 1)")
ltm.AddExceptionDataCut('Wmn',"metfilter==1 && (triggerFired[10]==1 || triggerFired[11] == 1 || triggerFired[12] || triggerFired[13] == 1)")

ltm.SetOutputWeightBranch('scaleMC_w')
ltm.SetReportFrequency(20)



#ltm.AddFile('data',str(ltm.GetInDirectory()) + 'monojet_Data.root',-1)

if __name__ == '__main__':
    ltm.SetOutFileName('MonoJetIncLimitsTrees.root')
    SetCuts(ltm,'monoJet_inc')
    ltm.MakeTrees()
