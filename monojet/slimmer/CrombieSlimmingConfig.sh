export CrombieFilesPerJob=2
export CrombieNBatchProcs=1
export CrombieQueue=1nh
#export CrombieQueue=8nh

export CrombieNLocalProcs=5

export CrombieFileBase=monojet
export CrombieEosDir=/store/user/zdemirag/Nero/v1.3/
export CrombieRegDir=/afs/cern.ch/work/z/zdemirag/eos/cms/$CrombieEosDir
export CrombieTempDir=/afs/cern.ch/work/z/zdemirag/public/ichep/TempOut
export CrombieFullDir=/afs/cern.ch/work/z/zdemirag/public/ichep/FullOut
export CrombieSkimDir=/afs/cern.ch/work/z/zdemirag/public/ichep/SkimOut

export CrombieDirList=TestDirs.txt

export CrombieSlimmerScript=runSlimmer.py
export CrombieJobScriptList=CrombieScriptList.txt
export CrombieCheckerScript=$CROMBIEPATH/scripts/CrombieTreeFinder.py

export CrombieGoodRuns=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Reprocessing/Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_v2.txt
#/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt