#! /usr/bin/env python
import sys, os, string, re, time, datetime
from multiprocessing import Process
from array import *

from LoadData import *
#from LoadElectron import *
#from LoadGJets import *

channel_list  = ['signal','Wmn','Zmm']
#channel_list  = ['Wen','Zee']
#channel_list  = ['gjets']

vbf = True
vtag = False
shapelimits = False

from ROOT import *
from math import *
from tdrStyle import *
from selection import build_selection
from datacard import dump_datacard
from pretty import plot_ratio, plot_cms

import numpy as n

setTDRStyle()

gROOT.LoadMacro("functions.C+");

if vtag:
    metcut = 250.0
else:
    metcut = 200.0

print "Starting Plotting Be Patient!"

lumi = 2245.
lumi_str = 2.3

def plot_stack(channel, name,var, bin, low, high, ylabel, xlabel, setLog = False):

    folder = '/afs/cern.ch/user/z/zdemirag/www/Monojet/ichep_76x/'
    if not os.path.exists(folder):
        os.mkdir(folder)

    yield_dic = {}    

    stack = THStack('a', 'a')
    if var is 'met':
        if vtag:
            binLowE = [250,300,350,400,500,600,1000]
        elif vbf:
            binLowE = [200,230,260,290,320,350,400,450,500,600,1000]            
        else:
            binLowE = [200., 230., 260.0, 290.0, 320.0, 350.0, 390.0, 430.0, 470.0, 510.0, 550.0, 590.0, 640.0, 690.0, 740.0, 790.0, 840.0, 900.0, 960.0, 1020.0, 1090.0, 1160.0, 1250.0]

            
        nb = len(binLowE)-1
        added = TH1D('added','added',nb,array('d',binLowE))
    else:
        added = TH1D('added', 'added',bin,low,high)

    added.Sumw2()

    f  = {}
    h1 = {}

    Variables = {}
    cut_standard= build_selection(channel,metcut)

    if var is 'met':
        if channel is not 'signal': 
            xlabel = 'U [GeV]'

    print "INFO Channel is: ", channel, " variable is: ", var, " Selection is: ", cut_standard,"\n"
    print 'INFO time is:', datetime.datetime.fromtimestamp( time.time())

    reordered_physics_processes = []
    if channel == 'Zmm' or channel == 'Zee': 
        reordered_physics_processes = reversed(ordered_physics_processes)
    else: 
        reordered_physics_processes = ordered_physics_processes

    for Type in ordered_physics_processes:
        yield_dic[physics_processes[Type]['datacard']] = 0

    for Type in reordered_physics_processes:
        # Create the Histograms
        histName = Type+'_'+name+'_'+channel

        if var is 'met':
            if vtag :
                binLowE = [250,300,350,400,500,600,1000]
            elif vbf:
                binLowE = [200,230,260,290,320,350,400,450,500,600,1000]
            else:
                binLowE = [200., 230., 260.0, 290.0, 320.0, 350.0, 390.0, 430.0, 470.0, 510.0, 550.0, 590.0, 640.0, 690.0, 740.0, 790.0, 840.0, 900.0, 960.0, 1020.0, 1090.0, 1160.0, 1250.0]

            n2 = len(binLowE)-1
            Variables[Type] = TH1F(histName,histName,n2,array('d',binLowE))
        else:
            Variables[Type] = TH1F(histName, histName, bin, low, high)

        Variables[Type].Sumw2()
        Variables[Type].StatOverflows(kTRUE)

        if Type is not 'data':
            f[Type] = ROOT.TFile(physics_processes[Type]['files'][0],"read")
            h1[Type] = f[Type].Get("htotal")
            total = h1[Type].GetBinContent(1)
            f[Type].Close()
        else:
            total = 1.0

        input_tree   = makeTrees(Type,"events",channel)
        n_entries = input_tree.GetEntries()

        w_trig = '(1.0)'

        # this is the scale using the total number of effective events
        scale = 1.0;
        scale = float(lumi)*physics_processes[Type]['xsec']/total
        
        #print '\n'
        print "type: ", Type,  "scale", scale, "lumi", lumi, physics_processes[Type]['xsec'], total

        if Type is not 'data' and Type is not 'signal_ggf' and Type is not 'signal_vbf':

            Variables[Type].SetFillColor(physics_processes[Type]['color'])
            Variables[Type].SetLineColor(physics_processes[Type]['color'])

            if Type.startswith('GJets') :
                makeTrees(Type,'events',channel).Draw(var + " >> " + histName,"(" + cut_standard + ")*mcWeight*ewk_a*akfactor*puWeight","goff")
            elif (Type.startswith('Zvv') or Type.startswith('Zll')) :                                  
                makeTrees(Type,'events',channel).Draw(var + " >> " + histName,"(" + cut_standard + ")*mcWeight*ewk_z*puWeight*lepton_SF*zkfactor","goff") 
            elif Type.startswith('Wlv'):
                makeTrees(Type,'events',channel).Draw(var + " >> " + histName,"(" + cut_standard + ")*mcWeight*ewk_w*puWeight*lepton_SF*wkfactor","goff")
            elif Type.startswith('QCD') and channel is 'signal':
                makeTrees(Type,'events',channel).Draw(var + " >> " + histName,"(" + cut_standard + ") *mcWeight*puWeight","goff")

            else:
                if Type.startswith('QCD') and channel is 'gjets':
                    # qcd is from the purity study
                    purity = "((0.04802 * (photonPt >= 175 && photonPt < 200 )) + \
                               (0.04241 * (photonPt >= 200 && photonPt < 250 )) + \
                               (0.0364  * (photonPt >= 250 && photonPt < 300 )) + \
                               (0.0333  * (photonPt >= 300 && photonPt < 350 )) + \
                               (0.02544 * (photonPt >= 350)))"
                    makeTrees(Type,'events',channel).Draw(var + " >> " + histName,"(" + cut_standard + ")*mcWeight*ewk_a*akfactor*puWeight* "+str(purity),"goff")                   
                else:
                    makeTrees(Type,'events',channel).Draw(var + " >> " + histName,"(" + cut_standard + ") *mcWeight*puWeight","goff")              

            Variables[Type].Scale(scale,"width")
            stack.Add(Variables[Type],"hist")
            added.Add(Variables[Type])

        if Type.startswith('signal'):
            #Variables[Type].SetLineColor(1)
            #Variables[Type].SetLineWidth(3)
            #Variables[Type].SetLineStyle(8)
            makeTrees(Type,"events",channel).Draw(var + " >> " + histName,"(" + cut_standard + ")*mcWeight*puWeight","goff")
            Variables[Type].Scale(scale,"width")
            
        if Type.startswith('data'):
            Variables[Type].SetMarkerStyle(20)
            makeTrees(Type,"events",channel).Draw(var + " >> " + histName, "(" + cut_standard +" )", "goff") 
            Variables[Type].Scale(1,"width")

        yield_dic[physics_processes[Type]['datacard']] += round(Variables[Type].Integral("width"),3)
        print Type, round(Variables[Type].Integral(),3), "total in: ", physics_processes[Type]['datacard'],  yield_dic[physics_processes[Type]['datacard']], round(Variables[Type].Integral("width"),3)        

    dump_datacard(channel,yield_dic)
            
    print 'INFO - Drawing the Legend', datetime.datetime.fromtimestamp( time.time())

    if channel is 'Zmm' or channel is 'Zee':
        legend = TLegend(.60,.65,.92,.92)
    elif channel is 'gjets':
        legend = TLegend(.60,.65,.82,.92)
    else:
        legend = TLegend(.60,.55,.92,.92)

    lastAdded = ''
    for process in  ordered_physics_processes:
        #print process
        Variables[process].SetTitle(process)
        if physics_processes[process]['label'] != lastAdded:
            lastAdded = physics_processes[process]['label']
            if process is not 'data' and process is not 'signal_vbf' and process is not 'signal_ggf':
                legend . AddEntry(Variables[process],physics_processes[process]['label'] , "f")
            if process is 'data':
                legend . AddEntry(Variables[process],physics_processes[process]['label'] , "p")


    c4 = TCanvas("c4","c4", 900, 1000)
    c4.SetBottomMargin(0.3)
    c4.SetRightMargin(0.06)

    stack.SetMinimum(0.01)

    if setLog:
        c4.SetLogy()
        stack.SetMaximum( stack.GetMaximum()  +  1e1*stack.GetMaximum() )
    else:
        stack.SetMaximum( stack.GetMaximum()  +  0.5*stack.GetMaximum() )
    
    stack.Draw()
    stack.GetYaxis().SetTitle(ylabel)
    stack.GetYaxis().CenterTitle()
    stack.GetYaxis().SetTitleOffset(1.2)
    stack.GetXaxis().SetTitle(xlabel)
    stack.GetXaxis().SetLabelSize(0)
    stack.GetXaxis().SetTitle('')

    Variables['data'].Draw("Esame")  
    Variables['signal_vbf'].SetLineWidth(2)
    Variables['signal_ggf'].SetLineWidth(2)
    Variables['signal_vbf'].SetLineColor(2)
    Variables['signal_ggf'].SetLineColor(4)
    Variables['signal_vbf'].Draw("samehist")
    Variables['signal_ggf'].Draw("samehist")


    legend . AddEntry(Variables['signal_vbf'],physics_processes['signal_vbf']['label'] , "l")
    legend . AddEntry(Variables['signal_ggf'],physics_processes['signal_ggf']['label'] , "l")


    legend.SetShadowColor(0);
    legend.SetFillColor(0);
    legend.SetLineColor(0);

    legend.Draw("same")
    plot_cms(True,lumi_str)


    Pad = TPad("pad", "pad", 0.0, 0.0, 1.0, 0.9)
    Pad.SetTopMargin(0.7)
    Pad.SetRightMargin(0.06)
    Pad.SetFillColor(0)
    Pad.SetGridy(1)
    Pad.SetFillStyle(0)
    Pad.Draw()
    Pad.cd(0)

    #Pad = TPad("pad", "pad", 0.0, 0.0, 1.0, 1.0)
    #Pad.SetTopMargin(0.7)
    #Pad.SetFillColor(0)
    #Pad.SetGridy(1)
    #Pad.SetFillStyle(0)
    #Pad.Draw()
    #Pad.cd(0)
    #Pad.SetRightMargin(0.06)
    
    data = Variables['data'].Clone()

    if vtag is True:
        plot_ratio(False,data,added,bin,xlabel,0.25,1.75,5)     
    else:

        if channel is 'Zmm' and var is 'met':
            plot_ratio(False,data,added,bin,xlabel,0.5,1.5,5)
        else:
            plot_ratio(False,data,added,bin,xlabel,0.5,1.5,5)

    f1 = TF1("f1","1",-5000,5000);
    f1.SetLineColor(4);
    f1.SetLineStyle(2);
    f1.SetLineWidth(2);
    f1.Draw("same")

    Pad.Update()
    Pad.RedrawAxis()

    if vtag is True:
        c4.SaveAs(folder+'/Histo_vtag_' + name + '_'+channel+'.pdf')
        c4.SaveAs(folder+'/Histo_vtag_' + name + '_'+channel+'.png')
        c4.SaveAs(folder+'/Histo_vtag_' + name + '_'+channel+'.C')
    elif vbf is True:
        c4.SaveAs(folder+'/Histo_vbf_' + name + '_'+channel+'.pdf')
        c4.SaveAs(folder+'/Histo_vbf_' + name + '_'+channel+'.png')
        c4.SaveAs(folder+'/Histo_vbf_' + name + '_'+channel+'.C')
    else: 
        c4.SaveAs(folder+'/Histo_monojet_' + name + '_'+channel+'.pdf')
        c4.SaveAs(folder+'/Histo_monojet_' + name + '_'+channel+'.png')
        c4.SaveAs(folder+'/Histo_monojet_' + name + '_'+channel+'.C')
   
    del Variables
    del var
    del f
    del h1
    c4.IsA().Destructor( c4 )
    stack.IsA().Destructor( stack )

arguments = {}
#                   = [var, bin, low, high, yaxis, xaxis, setLog]
if vtag:
    arguments['met']    = ['met','met',16,250,1500,'Events/GeV','E_{T}^{miss} [GeV]',True]
else:
    arguments['met']    = ['met','met',16,200,1500,'Events/GeV','E_{T}^{miss} [GeV]',True]

arguments['jetpt']  = ['jetpt','jet1Pt',20,100,1500,'Events/GeV','Leading Jet P_{T} [GeV]',True]

arguments['npv']  = ['npv','npv',50,0,50,'Events','npv',True]

arguments['fatjet1Pt']       = ['fatjet1Pt','fatjet1Pt',20,100,1500,'Events/GeV','Leading Fat Jet P_{T} [GeV]',True]
arguments['fatjet1PrunedM']  = ['fatjet1PrunedM','fatjet1PrunedM',20,0,500,'Events/GeV','Pruned FatJet Mass [GeV]',True]
arguments['fatjet1tau21']    = ['fatjet1tau21','fatjet1tau21',50,0,2,'Events/GeV','Tau2/Tau1',True]

arguments['n_looselep']     = ['n_looselep','n_looselep',6,0,6,'Events','Number of Loose Leptons',True]
arguments['n_loosepho']     = ['n_loosepho','n_loosepho',6,0,6,'Events','Number of Loose Photons',True]
arguments['n_tau']          = ['n_tau','n_tau',6,0,6,'Events','Number of Loose Taus',True]
arguments['n_bjetsMedium']  = ['n_bjetsMedium','n_bjetsMedium',6,0,6,'Events','Number of Medium b-Jets',True]
arguments['njetsclean']  = ['njetsclean','n_cleanedjets',8,0,8,'Events','Number of Jets',False]

arguments['jet1isMonoJetIdNew'] = ['jet1isMonoJetIdNew','jet1isMonoJetIdNew',2,0,2,'Events','jet1isMonoJetIdNew',True]
arguments['deltaPhi'] = ['minJetMetDPhi_clean','minJetMetDPhi_clean',30,0,3.0,'Events','min deltaPhi(jet,met)',False]
#arguments['deltaPhi'] = ['minJetMetDPhi_clean','minJetMetDPhi_clean',30,0,0.5,'Events','deltaPhi',False]
arguments['dPhi_j1j2'] = ['dPhi_j1j2','dPhi_j1j2',30,0,3.0,'Events','deltaPhi(j,j)',False]
#arguments['dPhi_j1met'] = ['deltaPhi_jet1met','TMath::Abs(deltaPhi(jet1Phi,metPhi))',30,0,3.0,'Events','deltaPhi(j1,met)',True]
arguments['dPhi_j1met'] = ['deltaPhi_jet1met','TMath::Abs(deltaPhi(jet1Phi,metPhi))',30,0,3.0,'Events','deltaPhi(j1,met)',False]
#arguments['dPhi_j1j2'] = ['dPhi_j1j2','dPhi_j1j2',30,0,1.0,'Events','deltaPhi(j,j)',False]
arguments['mass'] = ['mass','vectormass(photonPt,photonPhi,photonEta,fatjet1Pt,fatjet1Phi,fatjet1Phi)',100,400,2400,'Events','M_{j#gamma} [GeV]',True]

arguments['jot1Pt']  = ['jot1Pt','jot1Pt',20,100,1000,'Events/GeV','Leading Jet P_{T} [GeV]',True]
arguments['jot1Eta'] = ['jot1Eta','jot1Eta',50,0,5.0,'Events','Leading Jet #eta',False]

arguments['jot2Pt']  = ['jot2Pt','jot2Pt',20,40,840,'Events/GeV','Trailing Jet P_{T} [GeV]',True]
arguments['jot2Eta'] = ['jot2Eta','jot2Eta',50,0,5.0,'Events','Trailing Jet #eta',False]

#arguments['mjj']     = ['mjj','mjj',25,500,3500,'Events/GeV','M_{JJ} [GeV]',False]
arguments['mjj']     = ['mjj','mjj',10,500,3500,'Events/GeV','M_{JJ} [GeV]',False]
#arguments['jjDEta']  = ['jjDEta','jjDEta',50,0,5.0,'Events','jjDEta',False]
arguments['jjDEta']  = ['jjDEta','jjDEta',40,3.5,6.0,'Events','#Delta#eta_{JJ}',False]

processes     = []

variable_list = ['met','jot1Pt','jot1Eta','jot2Pt','jot2Eta','mjj','jjDEta']
#variable_list = ['met']
#variable_list = ['met','jetpt','njetsclean']
#variable_list = ['deltaPhi','dPhi_j1j2','dPhi_j1met']
#variable_list = ['met','fatjet1tau21','fatjet1Pt','fatjet1PrunedM']
#variable_list = ['met','n_looselep','n_loosepho','n_tau','n_bjetsMedium','jet1isMonoJetIdNew','jetpt','deltaPhi']
#variable_list = ['met','jetpt','njetsclean','fatjet1PrunedM','fatjet1tau21','fatjet1Pt']

start_time = time.time()

for channel in channel_list:
    for var in variable_list:
        arguments[var].insert(0,channel)
        print  arguments[var]
        process = Process(target = plot_stack, args = arguments[var])
        process.start()
        processes.append(process)
        arguments[var].remove(channel)
for process in processes: 
    process.join()

print("--- %s seconds ---" % (time.time()-start_time))
print datetime.datetime.fromtimestamp(time.time()-start_time)
