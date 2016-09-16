#! /bin/bash

fresh=$1

source CrombieSlimmingConfig.sh

if [ "$fresh" = "fresh" ]
then
    rm $CrombieSkimDir/*.root 2> /dev/null
    rm $CrombieSkimDir/*/*.root 2> /dev/null
fi

CrombieFlatSkimmer  --cut 'met > 200' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 1000000 --numproc $CrombieNLocalProcs --indir $CrombieFullDir --outdir $CrombieSkimDir --json $CrombieGoodRuns 

if [ ! -d $CrombieSkimDir/Purity ]
then
    mkdir $CrombieSkimDir/Purity
fi

./applyCorrections.py $CrombieSkimDir

#cp $CrombieSkimDir/monojet_GJets* $CrombieSkimDir/Purity/.
#./applyPurity.py $CrombieSkimDir/Purity
