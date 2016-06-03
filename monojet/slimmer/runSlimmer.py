#! /usr/bin/python

import sys,os
import ROOT
import os.path

OutTreeName = 'MonoJetTree'

os.system(os.environ['CROMBIEPATH'] + '/scripts/MakeTree.sh ' + OutTreeName)
ROOT.gROOT.LoadMacro(OutTreeName + '.cc+')

#ROOT.gROOT.LoadMacro('NeroTree76.C+')
#ROOT.gROOT.LoadMacro('testZeynep.C+')
ROOT.gROOT.LoadMacro('Nero_80x.C+')
ROOT.gROOT.LoadMacro('NeroSlimmer.cc+')

if sys.argv[1] == "test":
    ROOT.NeroSlimmer(
        #"/afs/cern.ch/work/z/zdemirag/work/ichep/CMSSW_7_6_4/src/NeroProducer/Nero/test/NeroNtuples_withsmear.root",
        #"/afs/cern.ch/work/z/zdemirag/work/ichep/CMSSW_7_6_4/src/NeroProducer/Nero/test/NeroNtuples_withoutsmear.root",
        "/afs/cern.ch/user/z/zdemirag/lnwork/ichep/MonoX/monojet/slimmer/ttbar_80x_full.root",
        "ttbar_sync80x_miniaod.root")

elif sys.argv[1] == "compile":
    exit()

else:
    if not os.path.isfile(sys.argv[2]):
        try:
            testFile = ROOT.TFile.Open(sys.argv[1])
            if not 'nero' in testFile.GetListOfKeys():
                testFile.Close()
                exit(0)

            testFile.Close()
            isSig = False
            if (((('DMS' in sys.argv[1]) or ('DMV' in sys.argv[1])) and 
                 ('NNPDF' in sys.argv[1]) and ('powheg' in sys.argv[1])) or 
                (('MonoW' in sys.argv[1]) or ('MonoZ' in sys.argv[1])) or
                ('JHUGen_Higgs' in sys.argv[1]) or
                ('proc-80' in sys.argv[1])):
                isSig = True
                print 'Running on signal!'

            ROOT.NeroSlimmer(sys.argv[1],
                         sys.argv[2],
                         isSig)
        except:
            print " Something didn't open right ... "
    else:
        print sys.argv[2] + " already exists!! Skipping..."
    
exit(0)
