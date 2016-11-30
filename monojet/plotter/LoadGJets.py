#! /usr/bin/env python

from ROOT import *
from colors import *
colors = defineColors()

lumi = 1.0

######################################################

#dataDir = "eos/cms/store/user/zdemirag/setup80x/Skim_v9/monojet_"
#dataDir = "/afs/cern.ch/work/z/zdemirag/public/ichep/setup80x/Skim_v2/monojet_"
#dataDir = "/afs/cern.ch/work/z/zdemirag/public/ichep/setup80x/Skim_v3/monojet_"
dataDir = "/afs/cern.ch/work/z/zdemirag/public/ichep/setup80x/Skim_v12/monojet_"

physics_processes = {
        #'QCD': { 'label':'QCD',
        #          'datacard':'qcd',
        #          'color':  "#F1F1F2",
        #          'ordering': 1,    
        #          'xsec' : 1.0,
        #          #'files':[dataDir+'SinglePhoton_JetHT.root',],
        #          'files':[dataDir+'SinglePhoton.root',],
        #          },


        #'QCD_200To300': { 'label':'QCD',
        #                  'datacard':'qcd',
        #                  'color' : colors.keys()[1],
        #                  'ordering': 1,
        #                  'xsec' : 23080.0,
        #                  'files':[dataDir+'GJets_HT-40To100.root'],
        #                  },


        'QCD_300To500': { 'label':'QCD',
                          'datacard':'qcd',
                          'color' : "#F1F1F2", #colors.keys()[2],
                          'ordering': 1,
                          'xsec' : 9235.0,
                          'files':[dataDir+'GJets_HT-100To200.root'],
                          },
        'QCD_500To700': { 'label':'QCD',
                          'datacard':'qcd',
                          'color' : "#F1F1F2", #colors.keys()[2],
                          'ordering': 1,
                          'xsec' : 2298.0,
                          'files':[dataDir+'GJets_HT-200To400.root'],
                          },
        'QCD_700To1000': { 'label':'QCD',
                           'datacard':'qcd',
                           'color' : "#F1F1F2", #colors.keys()[2],
                           'ordering': 1,
                           'xsec' : 277.6,
                           'files':[dataDir+'GJets_HT-400To600.root'],
                           },
        'QCD_1000To1500': { 'label':'QCD',
                            'datacard':'qcd',
                            'color' : "#F1F1F2", #colors.keys()[2],
                            'ordering': 1,
                            'xsec' : 93.47,
                            'files':[dataDir+'GJets_HT-600ToInf.root'],
                            },

        #'GJets_40To100': { 'label':'#gamma + jets',
        #                   'datacard': 'gjets',
        #                   'color' :  colors.keys()[6],
        #                   'ordering': 2,
        #                   'xsec' : 23080.0,
        #                   'files':[dataDir+'GJets_HT-40To100.root'],
        #                   },
        'GJets_100To200': { 'label':'#gamma + jets',
                            'datacard': 'gjets',
                            'color' :  "#db4dff", #"#9A9EAB", #colors.keys()[1],
                            'ordering': 2,
                            'xsec' : 9235.0,
                            'files':[dataDir+'GJets_HT-100To200.root'],
                            },
        'GJets_200To400': { 'label':'#gamma + jets',
                            'datacard': 'gjets',
                            'color' :  "#db4dff", #"#9A9EAB", #colors.keys()[1],
                            'ordering': 2,
                            'xsec' : 2298.0,
                            'files':[dataDir+'GJets_HT-200To400.root'],
                           },
        'GJets_400To600': { 'label':'#gamma + jets',
                            'datacard': 'gjets',
                            'color' :  "#db4dff", #"#9A9EAB", #colors.keys()[1],
                            'ordering': 2,
                            'xsec' : 277.6,
                            'files':[dataDir+'GJets_HT-400To600.root'],
                            },
        'GJets_600ToInf': { 'label':'#gamma + jets',
                            'datacard': 'gjets',
                            'color' :  "#db4dff", #"#9A9EAB", #colors.keys()[1],
                            'ordering': 2,
                            'xsec' : 93.47,
                            'files':[dataDir+'GJets_HT-600ToInf.root'],
                            },
        'signal_vbf': {'label':'qqH 125',
                       'datacard':'signal',
                       'color':1,
                       'ordering': 7,
                       'xsec' : 0,
                       'files':[dataDir+'WW.root'],#'VBF_HToInvisible_M125_13TeV_powheg_pythia8.root',],
                       },        
#        'signal_ggf': {'label':'ggH 125',
#                       'datacard':'signal',
#                       'color':1,
#                       'ordering': 7,
#                       'xsec' : 43.92,
#                       'files':[dataDir+'GluGlu_HToInvisible_M125_13TeV_powheg_pythia8.root',],                
#                       },
        'data': { 'label':'Data',
                  'datacard':'data',
                  'color': 1,
                  'ordering': 6,    
                  'xsec' : 1.0,
                  #'files':[dataDir+'SinglePhoton_JetHT.root',],
                  #'files':[dataDir+'SinglePhoton.root',],
                  'files':['/afs/cern.ch/work/z/zdemirag/public/ichep/setup80x/Skim_v15/monojet_SinglePhoton.root',],
                  }
        }

tmp = {}
for p in physics_processes: 
	if physics_processes[p]['ordering']>-1: tmp[p] = physics_processes[p]['ordering']
ordered_physics_processes = []

for key, value in sorted(tmp.iteritems(), key=lambda (k,v): (v,k)):
	ordered_physics_processes.append(key)

def makeTrees(process,tree,channel):
	Trees={}
	Trees[process] = TChain(tree)
	for sample in  physics_processes[process]['files']:
		Trees[process].Add(sample)
	return Trees[process]

######################################################
