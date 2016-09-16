#! /bin/bash

folder=/afs/cern.ch/work/z/zdemirag/public/ichep/setup80x/Skim_v3/

root -q -l -b xsecWeights.cc+\(\"$folder\"\)                      # This is to just make sure the macro is compiled

cat xsecArgs.txt | xargs -n2 -P6 ./xsecRunner.sh $folder
