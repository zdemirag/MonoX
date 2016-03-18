#!/usr/bin/env python

from argparse import ArgumentParser
import os
from subprocess import Popen, PIPE
import shutil
from pprint import pprint
import datetime

parser = ArgumentParser()
parser.add_argument('models', metavar = 'MODEL', nargs='+', help = 'Signal model(s) to compute limits for.')
parser.add_argument('-R', '--root-file', metavar = 'PATH', action = 'store', dest = 'rootFile', help = 'Histogram ROOT file.')
parser.add_argument('--variable', '-v', action = 'store', dest = 'variable', default = 'phoPtHighMet', help = 'Discriminating variable.')

opts = parser.parse_args()

mandatories = ['models', 'rootFile']
for m in mandatories:
    if not opts.__dict__[m]:
        print "\nMandatory option is missing\n"
        parser.print_help()
        exit(-1)

###======================================================================================
### Function to Run Higgs Tool and Get Expected Limit for a DataCard
###======================================================================================

def RunHiggsTool(DataCardPath,LimitToolDir):
    TextPath = DataCardPath
    HiggsTool = Popen(['combine','-M','Asymptotic',TextPath],
                      stdout=PIPE,stderr=PIPE,cwd=LimitToolDir)    
    """ For debugging, will cause grep step to crash
    (hout, herr) = HiggsTool.communicate()
    print hout, '\n'
    print herr, '\n'
    """


    find = Popen(['egrep','Observed|50.0%'],stdin=HiggsTool.stdout,stdout=PIPE,stderr=PIPE)
    """ for debugging, will cause next step to crash
    (fout, ferr) = find.communicate()
    print fout, '\n'
    print ferr, '\n'
    """

    lines = [line for line in find.stdout]
    # print lines

    obs = -1.
    exp = -1.

    for line in lines:
        # print line
        tmp = line.split()
        # print tmp
        if tmp:
            if 'Observed' in tmp[0]:
                obs = float(tmp[4])
            elif "Expected" in tmp[0]:
                exp = float(tmp[4])

    return (obs, exp)


###======================================================================================
### Make Datacards and compute limits
###======================================================================================


modelList = opts.models

classes = {} # "dmv" : ( [mMed], [mDM] ) 
for model in sorted(modelList): # sorted(limits):
   (name, xval, yval) = model.split('-')
   if not name in classes.keys():
       classes[name] = ( [], [] )
   if not xval in classes[name][0]:
       classes[name][0].append(xval)
   if not yval in classes[name][1]:
       classes[name][1].append(yval)

pprint(classes)

LimitToolDir = os.path.join(os.environ['CMSSW_BASE'], 'src/HiggsAnalysis/CombinedLimit')
cardDir = os.path.join(LimitToolDir, 'data/monoph')
if not os.path.exists(cardDir):
    os.makedirs(cardDir)

rootFilePath = os.path.join(cardDir, opts.rootFile)
shutil.copy(opts.rootFile, rootFilePath)

print datetime.datetime.now(), '\n'

limits = {} # "dmv-500-150" : ( Obs, Exp )
print "%16s %10s %10s" % ('model', 'Observed', 'Expected')
for iM, model in enumerate(modelList):
    if iM % 10 == 0:
        print datetime.datetime.now()
    
    '''./datacard.py dma-500-1 limitsfile.root -o test.txt -O -v phoPtHighMet'''
    cardPath = os.path.join(cardDir, model+'_'+opts.variable+'.txt')
    argList = ['./datacard.py', model, opts.rootFile, '-v', opts.variable, '-o', cardPath]
    MakeDataCard = Popen(argList, stdout=PIPE, stderr=PIPE)
    
    (out, err) = MakeDataCard.communicate()
    # print out, '\n'
    # print err, '\n'
        
    limits[model] = RunHiggsTool(cardPath,LimitToolDir)

    print "%16s %10.2f %10.2f" % (model, limits[model][0], limits[model][1])

