export CrombieFilesPerJob=2
export CrombieNBatchProcs=1
export CrombieQueue=1nh
#export CrombieQueue=8nh

export CrombieNLocalProcs=5

export CrombieFileBase=monojet
export CrombieEosDir=/store/group/phys_exotica/monojet/zdemirag/setup80x/Nero/zey_base/
export CrombieRegDir=/afs/cern.ch/work/z/zdemirag/eos/cms/$CrombieEosDir

export CrombieTempDir=/afs/cern.ch/work/z/zdemirag/public/ichep/setup80x/Temp_v6
export CrombieFullDir=/afs/cern.ch/work/z/zdemirag/public/ichep/setup80x/Full_v6
export CrombieSkimDir=/afs/cern.ch/work/z/zdemirag/public/ichep/setup80x/Skim_v6

export CrombieDirList=TestDirs.txt

export CrombieSlimmerScript=runSlimmer.py
export CrombieJobScriptList=CrombieScriptList.txt
export CrombieCheckerScript=$CROMBIEPATH/scripts/CrombieTreeFinder.py

export CrombieGoodRuns=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt
#/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276097_13TeV_PromptReco_Collisions16_JSON_NoL1T_v2.txt
#/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-274443_13TeV_PromptReco_Collisions16_JSON.txt    
#/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-274240_13TeV_PromptReco_Collisions16_JSON.txt
#/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Reprocessing/Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_v2.txt
#/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt