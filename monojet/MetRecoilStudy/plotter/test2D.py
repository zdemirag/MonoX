#! /usr/bin/python

import ROOT
import tdrStyle
from array import array

ROOT.gROOT.LoadMacro('PlotBase.cc+')
#ROOT.gROOT.LoadMacro('PlotHists.cc+')
ROOT.gROOT.LoadMacro('Plot2D.cc+')

tdrStyle.setTDRStyle()

ROOT.gROOT.SetBatch(True)

#sampledir = "/afs/cern.ch/work/d/dabercro/public/Winter15/flatTreesSkimmedV3/"
#goodRuns  = "/afs/cern.ch/work/d/dabercro/public/Winter15/GoodRunsV3/"
sampledir = "/Users/dabercro/GradSchool/Winter15/flatTreesSkimmedV3/"
goodRuns  = "/Users/dabercro/GradSchool/Winter15/GoodRunsV3/"

MuonFile       = ROOT.TFile(goodRuns + "monojet_SingleMuon.root")
SingleElecFile = ROOT.TFile(goodRuns + "monojet_SingleElectron.root")
SinglePhoFile  = ROOT.TFile(goodRuns + "monojet_SinglePhoton.root")
DYFile         = ROOT.TFile(sampledir + "monojet_DYJetsToLL_M-50.root")
GJetsFile      = ROOT.TFile(sampledir + "monojet_GJets.root")

MuonTree       = MuonFile.Get("events")
SingleElecTree = SingleElecFile.Get("events")
SinglePhoTree  = SinglePhoFile.Get("events")
DYTree         = DYFile.Get("events")
GJetsTree      = GJetsFile.Get("events")

plotter = ROOT.Plot2D()

#####################################

fitBin = 150.0

allSelections = "(jet1isMonoJetId == 1 && jet1Pt > 100) && "

#####################################

plotter.SetIncludeErrorBars(True)

plotter.AddTree(MuonTree)
plotter.AddTree(DYTree)
plotter.AddTree(SingleElecTree)
plotter.AddTree(DYTree)
plotter.AddTree(SinglePhoTree)
plotter.AddTree(GJetsTree)

plotter.AddLegendEntry("Z#mu#mu Data",1)
plotter.AddLegendEntry("Z#mu#mu",2)
plotter.AddLegendEntry("Zee Data",3)
plotter.AddLegendEntry("Zee",4)
plotter.AddLegendEntry("#gamma+jets Data",3)
plotter.AddLegendEntry("#gamma+jets",4)

plotter.AddName("Zmm_Data")
plotter.AddName("Zmm_MC")
plotter.AddName("Zee_Data")
plotter.AddName("Zee_MC")
plotter.AddName("gjets_Data")
plotter.AddName("gjets_MC")

lepSelection  = "(n_looselep == 2 && n_tightlep > 0 && n_loosepho == 0 && n_tau == 0 && lep2Pt > 20) && abs(dilep_m - 91) < 30 && n_bjetsMedium == 0 && "

muonSelection = allSelections + lepSelection + "(lep1PdgId*lep2PdgId == -169)"
elecSelection = allSelections + lepSelection + "(lep1PdgId*lep2PdgId == -121)"
phoSelection  = allSelections + "(photonIsTight == 1 && n_looselep == 0 && n_tau == 0)"

plotter.AddWeight(muonSelection)
plotter.AddWeight(muonSelection + " && (genBos_PdgId == 23) * leptonSF * mcWeight * npvWeight")
plotter.AddWeight(elecSelection)
plotter.AddWeight(elecSelection + " && (genBos_PdgId == 23) * leptonSF * mcWeight * npvWeight")
plotter.AddWeight(phoSelection)
plotter.AddWeight(phoSelection + " && (genBos_PdgId == 22) * kfactor * XSecWeight * npvWeight")

plotter.AddExprX("dilep_pt")
plotter.AddExprX("genBos_pt")
plotter.AddExprX("dilep_pt")
plotter.AddExprX("genBos_pt")
plotter.AddExprX("photonPt")
plotter.AddExprX("genBos_pt")

plotter.AddExpr("u_paraZ + dilep_pt")
plotter.AddExpr("u_paraZ + dilep_pt")
plotter.AddExpr("u_paraZ + dilep_pt")
plotter.AddExpr("u_paraZ + dilep_pt")
plotter.AddExpr("u_paraPho + photonPt")
plotter.AddExpr("u_paraPho + photonPt")

plotter.MakeFitGraphs(100,10,1010,300,-1*fitBin,fitBin)

plotter.ResetExpr()
plotter.AddExpr("u_perpZ")
plotter.AddExpr("u_perpZ")
plotter.AddExpr("u_perpZ")
plotter.AddExpr("u_perpZ")
plotter.AddExpr("u_perpPho")
plotter.AddExpr("u_perpPho")

plotter.MakeFitGraphs(100,10,1010,300,-1*fitBin,fitBin)

del plotter

MuonFile.Close()
SingleElecFile.Close()
SinglePhoFile.Close()
DYFile.Close()
GJetsFile.Close()
