#! /bin/bash

fresh=$1

source CrombieSlimmingConfig.sh

if [ "$fresh" = "fresh" ]
then
    rm $CrombieSkimDir/*.root 2> /dev/null
    rm $CrombieSkimDir/*/*.root 2> /dev/null
fi

CrombieFlatSkimmer  --cut 'met > 200' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 1000000 --numproc $CrombieNLocalProcs --indir $CrombieFullDir --outdir $CrombieSkimDir --json $CrombieGoodRuns --filters 'files/csc2015_Dec01.txt' 'files/ecalscn1043093_Dec01.txt' 'files/MET_hbheiso.txt' 'files/MET_hbher2l.txt'

./applyCorrections.py $CrombieSkimDir
./applyTriggers.py $CrombieSkimDir
#./applyPurity.py $CrombieSkimDir/Purity
