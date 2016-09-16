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
        "eos/cms/store/group/phys_exotica/monojet/zdemirag/setup80x/Nero/zey_base/SingleElectron/SingleElectron-Run2016B-v2_Missing/160713_150938/0000/NeroNtuples_19.root",
        #"eos/cms/store/group/phys_exotica/monojet/zdemirag/setup80x/Nero/zey_base/DMV_NNPDF30_Axial_Mphi-1500_Mchi-10_gSM-0p25_gDM-1p0_v2_13TeV-powheg/DMV_NNPDF30_Axial_Mphi-1500_Mchi-10_gSM-0p25_gDM-1p0/160710_100053/0000/NeroNtuples_1.root",
        #"eos/cms/store/group/phys_exotica/monojet/zdemirag/setup80x/Nero/zey_base/MET/MET-Run2016B-v2/160709_170419/0000/NeroNtuples_1.root",
        "new_test.root"
        #"eos/cms/store/user/zdemirag/setup80x/Nero/zey_base/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DYJetsToLL_M-50_HT-600toInf/160606_230225/0000/NeroNtuples_7.root",
        #"dy_test.root"
        #"eos/cms/store/user/zdemirag/setup80x/Nero/Data/zey_base/SingleElectron/SingleElectron-Run2016B-v2/160620_201710/0000/NeroNtuples_Photon_278.root",
        #"missing_ele_6.root"
        )

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
