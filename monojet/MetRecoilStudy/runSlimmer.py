#! /usr/bin/python

import sys
import ROOT

ROOT.gROOT.LoadMacro('NeroTree.C+')
ROOT.gROOT.LoadMacro('MonoJetTree.cc+')
ROOT.gROOT.LoadMacro('NeroSlimmer.cc+')

if sys.argv[1] == "test":
    ROOT.NeroSlimmer(
        "root://eoscms//store/user/yiiyama/transfer/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3+AODSIM/nero_0001.root",
        "testDY.root")
    ROOT.NeroSlimmer(
        "root://eoscms//store/user/yiiyama/transfer/DYJetsToNuNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM/nero_0002.root",
        "testZnn.root")
    ROOT.NeroSlimmer(
        "root://eoscms//store/user/yiiyama/transfer/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM/nero_0001.root",
        "testGJets.root")
    ROOT.NeroSlimmer(
        "root://eoscms//store/user/yiiyama/transfer/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM/nero_0001.root",
        "testWJets.root")
    ROOT.NeroSlimmer(
        "root://eoscms//store/user/yiiyama/transfer/MET+Run2015D-PromptReco-v3+AOD/nero_0001.root",
        "testData.root")

else:
    ROOT.NeroSlimmer(sys.argv[1],
                     sys.argv[2])
