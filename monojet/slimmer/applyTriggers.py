#! /usr/bin/python

from CrombieTools.SkimmingTools import Corrector
import os,sys

directory = sys.argv[1]

applicator = Corrector.MakeApplicator('',True,'events','events',100000)

def addCorr(name,expr,cut,fileName,histName):
    applicator.AddCorrector(Corrector.MakeCorrector(name,expr,cut,fileName,histName))
##

addCorr('METTrigger','met','1','files/triggerEffs.root','MET_trigger')
addCorr('EleTrigger',['abs(lep1Eta)','lep1Pt'],'lep1IsTight && lep1Pt > 0 && abs(lep1PdgId) == 11','files/eleTrig.root','hEffEtaPt')

for fileName in os.listdir(directory):
    if not '.root' in fileName:
        continue
    ##

    applicator.ApplyCorrections(directory + "/" + fileName)
##
