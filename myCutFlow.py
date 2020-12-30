from ROOT import *
from array import *
import os
import math
from pprint import pprint


#take the file root for the signal
myfile = TFile('allTrees_signal_NoSys.root')

#study three different hypothesis for the masses of supersymmetric particles produced
mytree1 = myfile.Get('C1N2_WZ_300_0_NoSys')
mytree2 = myfile.Get('C1N2_WZ_500_200_NoSys')
mytree3 = myfile.Get('C1N2_WZ_1200_200_NoSys')

#total number of events in each trees
entries1 = mytree1.GetEntries()
entries2 = mytree2.GetEntries()
entries3 = mytree3.GetEntries()

print(entries1)
print(entries2)
print(entries3)

signal_PS_counter = [[0],[0],[0]]
signal_counter = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
signal_PS_counter_weighed = [[0],[0],[0]]
signal_counter_weighed = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

#start analysis of first tree
#set to zero the value of the counters
cutPS = 0 #counter for preselection cut without a weight, so each events count 1
cutPSweighed = 0 #counter for preselection cut with the weight of each events
cut1 = 0
cut1weighed = 0
cut2 = 0
cut2weighed = 0
cut3 = 0
cut3weighed = 0
cut4 = 0
cut4weighed = 0
cut5 = 0
cut5weighed = 0
cut6 = 0
cut6weighed = 0
cut7 = 0
cut7weighed = 0
cut8 = 0
cut8weighed = 0
cut9 = 0
cut9weighed = 0
cut10 = 0
cut10weighed = 0

for j_entry in range(entries1):
 mytree1.GetEvent(j_entry)
 weight = getattr(mytree1, "genWeight")*getattr(mytree1, "pileupWeight")*getattr(mytree1, "eventWeight")*getattr(mytree1, "leptonWeight")*getattr(mytree1, "bTagWeight")
 if (getattr(mytree1, "met")>200 and getattr(mytree1, "nJet30")>=1 and getattr(mytree1, "nLep_base")==1 and getattr(mytree1, "nLep_signal")==1 and getattr(mytree1, "mjj")<200 and getattr(mytree1, "mjj")>50 getattr(mytree1, "mt")>50):
  cutPS = cutPS + 1
  cutPSweighed = cutPSweighed + weight
 else: continue
 if getattr(mytree1, "nLep_base")==1 and getattr(mytree1, "nLep_signal")==1:
  cut1 = cut1 + 1
  cut1weighed = cut1weighed + weight
 else: continue
 if getattr(mytree1, "lep1Pt")>25:
  cut2 = cut2 + 1
  cut2weighed = cut2weighed + weight
 else: continue
 if getattr(mytree1, "nJet30")==2 or getattr(mytree1, "nJet30")==3:
  cut3 = cut3 + 1
  cut3weighed = cut3weighed + weight
 else: continue 
 if getattr(mytree1, "nBJet30_DL1")==0:
  cut4 = cut4 + 1
  cut4weighed = cut4weighed + weight
 else: continue
 if getattr(mytree1, "met")>200:
  cut5 = cut5 + 1
  cut5weighed = cut5weighed + weight
 else: continue
 if getattr(mytree1, "met_phi")<2.8:
  cut6 = cut6 + 1
  cut6weighed = cut6weighed + weight
 else: continue
 if getattr(mytree1, "mjj")<105 and getattr(mytree1, "mjj")>70:
  cut7 = cut7 + 1
  cut7weighed = cut7weighed + weight
 else: continue
 if getattr(mytree1, "Nfatjets")==0:
  cut8 = cut8 + 1
  cut8weighed = cut8weighed + weight
 else: continue            
 if getattr(mytree1, "mt")>200 and getattr(mytree1, "mt")<380:
  cut9 = cut9 + 1
  cut9weighed = cut9weighed + weight
 if getattr(mytree1, "mt")>380:
  cut10 = cut10 + 1
  cut10weighed = cut10weighed + weight
 else: continue
            
#end analysis of first tree

#start analysis of second tree
            
#set to zero the value of the counters
cutPS = 0 #counter for preselection cut without a weight, so each events count 1
cutPSweighed = 0 #counter for preselection cut with the weight of each events
cut1 = 0
cut1weighed = 0
cut2 = 0
cut2weighed = 0
cut3 = 0
cut3weighed = 0
cut4 = 0
cut4weighed = 0
cut5 = 0
cut5weighed = 0
cut6 = 0
cut6weighed = 0
cut7 = 0
cut7weighed = 0
cut8 = 0
cut8weighed = 0
cut9 = 0
cut9weighed = 0
cut10 = 0
cut10weighed = 0
            
for i_entry in range(entries2):
 mytree2.GetEvent(i_entry)
 weight = getattr(mytree2, "genWeight")*getattr(mytree2, "pileupWeight")*getattr(mytree2, "eventWeight")*getattr(mytree2, "leptonWeight")*getattr(mytree2, "bTagWeight")
 if (getattr(mytree2, "met")>200 and getattr(mytree2, "nJet30")>=1 and getattr(mytree2, "nLep_base")==1 and getattr(mytree2, "nLep_signal")==1 and getattr(mytree1, "mjj")<200 and getattr(mytree2, "mjj")>50 getattr(mytree2, "mt")>50):
  cutPS = cutPS + 1
  cutPSweighed = cutPSweighed + weight
 else: continue
 if getattr(mytree2, "nLep_base")==1 and getattr(mytree2, "nLep_signal")==1:
  cut1 = cut1 + 1
  cut1weighed = cut1weighed + weight
 else: continue 
 if getattr(mytree2, "lep1Pt")>25:
  cut2 = cut2 + 1
  cut2weighed = cut2weighed + weight
 else: continue
 if getattr(mytree2, "nJet30")==2 or getattr(mytree2, "nJet30")==3:
  cut3 = cut3 + 1
  cut3weighed = cut3weighed + weight
 else: continue 
 if getattr(mytree2, "nBJet30_DL1")==0:
  cut4 = cut4 + 1
  cut4weighed = cut4weighed + weight
 else: continue
 if getattr(mytree2, "met")>200:
  cut5 = cut5 + 1
  cut5weighed = cut5weighed + weight
 else: continue
 if getattr(mytree2, "met_phi")<2.8:
  cut6 = cut6 + 1
  cut6weighed = cut6weighed + weight
 else: continue
 if getattr(mytree2, "mjj")<105 and getattr(mytree2, "mjj")>70:
  cut7 = cut7 + 1
  cut7weighed = cut7weighed + weight
 else: continue
 if getattr(mytree2, "Nfatjets")==0:
  cut8 = cut8 + 1
  cut8weighed = cut8weighed + weight
 else: continue
 if getattr(mytree2, "mt")>200 and getattr(mytree2, "mt")<380:
  cut9 = cut9 + 1
  cut9weighed = cut9weighed + weight
 if getattr(mytree2, "mt")>380:
  cut10 = cut10 + 1
  cut10weighed = cut10weighed + weight
 else: continue

      
#start analysis of third tree
            
#set to zero the value of the counters
cutPS = 0 #counter for preselection cut without a weight, so each events count 1
cutPSweighed = 0 #counter for preselection cut with the weight of each events
cut1 = 0
cut1weighed = 0
cut2 = 0
cut2weighed = 0
cut3 = 0
cut3weighed = 0
cut4 = 0
cut4weighed = 0
cut5 = 0
cut5weighed = 0
cut6 = 0
cut6weighed = 0
cut7 = 0
cut7weighed = 0
cut8 = 0
cut8weighed = 0
cut9 = 0
cut9weighed = 0
cut10 = 0
cut10weighed = 0

for w_entry in range(entries3):
 mytree3.GetEvent(w_entry)
 weight = getattr(mytree3, "genWeight")*getattr(mytree3, "pileupWeight")*getattr(mytree3, "eventWeight")*getattr(mytree3, "leptonWeight")*getattr(mytree3, "bTagWeight")
 if (getattr(mytree3, "met")>200 and getattr(mytree3, "nJet30")>=1 and getattr(mytree3, "nLep_base")==1 and getattr(mytree3, "nLep_signal")==1 and getattr(mytree3, "mjj")<200 and getattr(mytree3, "mjj")>50 getattr(mytree3, "mt")>50):
  cutPS = cutPS + 1
  cutPSweighed = cutPSweighed + weight
 else: continue
 if getattr(mytree3, "nLep_base")==1 and getattr(mytree3, "nLep_signal")==1:
  cut1 = cut1 + 1
  cut1weighed = cut1weighed + weight
 else: continue 
 if getattr(mytree3, "lep1Pt")>25:
  cut2 = cut2 + 1
  cut2weighed = cut2weighed + weight
 else: continue
 if getattr(mytree3, "nJet30")==2 or getattr(mytree3, "nJet30")==3:
  cut3 = cut3 + 1
  cut3weighed = cut3weighed + weight
 else: continue 
 if getattr(mytree3, "nBJet30_DL1")==0:
  cut4 = cut4 + 1
  cut4weighed = cut4weighed + weight
 else: continue
 if getattr(mytree3, "met")>200:
  cut5 = cut5 + 1
  cut5weighed = cut5weighed + weight
 else: continue
 if getattr(mytree3, "met_phi")<2.8:
  cut6 = cut6 + 1
  cut6weighed = cut6weighed + weight
 else: continue
 if getattr(mytree3, "mjj")<105 and getattr(mytree3, "mjj")>70:
  cut7 = cut7 + 1
  cut7weighed = cut7weighed + weight
 else: continue
 if getattr(mytree3, "Nfatjets")==0:
  cut8 = cut8 + 1
  cut8weighed = cut8weighed + weight
 else: continue
 if getattr(mytree3, "mt")>200 and getattr(mytree3, "mt")<380:
  cut9 = cut9 + 1
  cut9weighed = cut9weighed + weight
 if getattr(mytree3, "mt")>380:
  cut10 = cut10 + 1
  cut10weighed = cut10weighed + weight
 else: continue
            
print("preselection cut")
for r in signal_PS_counter:
            print()
print("cut flow")
for t in signal_counter:
            for c in r:
             print(c, end = " ")
            print()
#end analysis of the signal

#start analysis of the background            

myfile2 = TFile('allTrees_bkg_NoSys.root')
mytree1bkg = myfile2.Get('diboson_NoSys')
mytree2bkg = myfile2.Get('multiboson_NoSys')
mytree3bkg = myfile2.Get('singletop_NoSys')
mytree4bkg = myfile2.Get('ttbar_NoSys')
mytree5bkg = myfile2.Get('tth_NoSys')
mytree6bkg = myfile2.Get('ttv_NoSys')
mytree7bkg = myfile2.Get('vh_NoSys')
mytree8bkg = myfile2.Get('wjets_NoSys')
mytree9bkg = myfile2.Get('zjets_NoSys')

entries1bkg = mytree1bkg.GetEntriesFast()
entries2bkg = mytree2bkg.GetEntriesFast()
entries3bkg = mytree3bkg.GetEntriesFast()
entries4bkg = mytree4bkg.GetEntriesFast()
entries5bkg = mytree5bkg.GetEntriesFast()
entries6bkg = mytree6bkg.GetEntriesFast()
entries7bkg = mytree7bkg.GetEntriesFast()
entries8bkg = mytree8bkg.GetEntriesFast()
entries9bkg = mytree9bkg.GetEntriesFast()



for a_entry in range(entries1bkg):
 mytree1bkg.GetEvent(a_entry)
 weight = getattr(mytree1bkg, "genWeight")*getattr(mytree1bkg, "pileupWeight")*getattr(mytree1bkg, "eventWeight")*getattr(mytree1bkg, "leptonWeight")*getattr(mytree1bkg, "bTagWeight")
 if (getattr(mytree1bkg, "met")>200 and getattr(mytree1bkg, "nJet30")>=1 and getattr(mytree1bkg, "nLep_base")==1 and getattr(mytree1bkg, "nLep_signal")==1 and getattr(mytree1bkg, "mjj")<200 and getattr(mytree1bkg, "mjj")>50 getattr(mytree1bkg, "mt")>50):
  cutPS = cutPS + 1
  cutPSweighed = cutPSweighed + weight
 else: continue
 if getattr(mytree1bkg, "nLep_base")==1 and getattr(mytree1bkg, "nLep_signal")==1:
  cut1 = cut1 + 1
  cut1weighed = cut1weighed + weight
 else: continue
 if getattr(mytree1bkg, "lep1Pt")>25:
  cut2 = cut2 + 1
  cut2weighed = cut2weighed + weight
 else: continue
 if getattr(mytree1bkg, "nJet30")==2 or getattr(mytree1bkg, "nJet30")==3:
  cut3 = cut3 + 1
  cut3weighed = cut3weighed + weight
 else: continue 
 if getattr(mytree1bkg, "nBJet30_DL1")==0:
  cut4 = cut4 + 1
  cut4weighed = cut4weighed + weight
 else: continue
 if getattr(mytree1bkg, "met")>200:
  cut5 = cut5 + 1
  cut5weighed = cut5weighed + weight
 else: continue
 if getattr(mytree1bkg, "met_phi")<2.8:
  cut6 = cut6 + 1
  cut6weighed = cut6weighed + weight
 else: continue
 if getattr(mytree1bkg, "mjj")<105 and getattr(mytree1bkg, "mjj")>70:
  cut7 = cut7 + 1
  cut7weighed = cut7weighed + weight
 else: continue
 if getattr(mytree1bkg, "Nfatjets")==0:
  cut8 = cut8 + 1
  cut8weighed = cut8weighed + weight
 else: continue            
 if getattr(mytree1bkg, "mt")>200 and getattr(mytree1bkg, "mt")<380:
  cut9 = cut9 + 1
  cut9weighed = cut9weighed + weight
 if getattr(mytree1bkg, "mt")>380:
  cut10 = cut10 + 1
  cut10weighed = cut10weighed + weight
 else: continue
            
for b_entry in range(entries2bkg):
 mytree2bkg.GetEvent(b_entry)
 weight = getattr(mytree2bkg, "genWeight")*getattr(mytree2bkg, "pileupWeight")*getattr(mytree2bkg, "eventWeight")*getattr(mytree2bkg, "leptonWeight")*getattr(mytree2bkg, "bTagWeight")
 if (getattr(mytree2bkg, "met")>200 and getattr(mytree2bkg, "nJet30")>=1 and getattr(mytree2bkg, "nLep_base")==1 and getattr(mytree2bkg, "nLep_signal")==1 and getattr(mytree2bkg, "mjj")<200 and getattr(mytree2bkg, "mjj")>50 getattr(mytree2bkg, "mt")>50):
  cutPS = cutPS + 1
  cutPSweighed = cutPSweighed + weight
 else: continue
 if getattr(mytree2bkg, "nLep_base")==1 and getattr(mytree2bkg, "nLep_signal")==1:
  cut1 = cut1 + 1
  cut1weighed = cut1weighed + weight
 else: continue
 if getattr(mytree2bkg, "lep1Pt")>25:
  cut2 = cut2 + 1
  cut2weighed = cut2weighed + weight
 else: continue
 if getattr(mytree2bkg, "nJet30")==2 or getattr(mytree2bkg, "nJet30")==3:
  cut3 = cut3 + 1
  cut3weighed = cut3weighed + weight
 else: continue 
 if getattr(mytree2bkg, "nBJet30_DL1")==0:
  cut4 = cut4 + 1
  cut4weighed = cut4weighed + weight
 else: continue
 if getattr(mytree2bkg, "met")>200:
  cut5 = cut5 + 1
  cut5weighed = cut5weighed + weight
 else: continue
 if getattr(mytree2bkg, "met_phi")<2.8:
  cut6 = cut6 + 1
  cut6weighed = cut6weighed + weight
 else: continue
 if getattr(mytree2bkg, "mjj")<105 and getattr(mytree2bkg, "mjj")>70:
  cut7 = cut7 + 1
  cut7weighed = cut7weighed + weight
 else: continue
 if getattr(mytree2bkg, "Nfatjets")==0:
  cut8 = cut8 + 1
  cut8weighed = cut8weighed + weight
 else: continue            
 if getattr(mytree2bkg, "mt")>200 and getattr(mytree2bkg, "mt")<380:
  cut9 = cut9 + 1
  cut9weighed = cut9weighed + weight
 if getattr(mytree2bkg, "mt")>380:
  cut10 = cut10 + 1
  cut10weighed = cut10weighed + weight
 else: continue
           
for c_entry in range(entries3bkg):
 mytree3bkg.GetEvent(c_entry)
 weight = getattr(mytree3bkg, "genWeight")*getattr(mytree3bkg, "pileupWeight")*getattr(mytree3bkg, "eventWeight")*getattr(mytree3bkg, "leptonWeight")*getattr(mytree3bkg, "bTagWeight")
 if (getattr(mytree3bkg, "met")>200 and getattr(mytree3bkg, "nJet30")>=1 and getattr(mytree3bkg, "nLep_base")==1 and getattr(mytree3bkg, "nLep_signal")==1 and getattr(mytree3bkg, "mjj")<200 and getattr(mytree3bkg, "mjj")>50 getattr(mytree3bkg, "mt")>50):
  cutPS = cutPS + 1
  cutPSweighed = cutPSweighed + weight
 else: continue
 if getattr(mytree3bkg, "nLep_base")==1 and getattr(mytree3bkg, "nLep_signal")==1:
  cut1 = cut1 + 1
  cut1weighed = cut1weighed + weight
 else: continue
 if getattr(mytree3bkg, "lep1Pt")>25:
  cut2 = cut2 + 1
  cut2weighed = cut2weighed + weight
 else: continue
 if getattr(mytree3bkg, "nJet30")==2 or getattr(mytree3bkg, "nJet30")==3:
  cut3 = cut3 + 1
  cut3weighed = cut3weighed + weight
 else: continue 
 if getattr(mytree3bkg, "nBJet30_DL1")==0:
  cut4 = cut4 + 1
  cut4weighed = cut4weighed + weight
 else: continue
 if getattr(mytree3bkg, "met")>200:
  cut5 = cut5 + 1
  cut5weighed = cut5weighed + weight
 else: continue
 if getattr(mytree3bkg, "met_phi")<2.8:
  cut6 = cut6 + 1
  cut6weighed = cut6weighed + weight
 else: continue
 if getattr(mytree3bkg, "mjj")<105 and getattr(mytree3bkg, "mjj")>70:
  cut7 = cut7 + 1
  cut7weighed = cut7weighed + weight
 else: continue
 if getattr(mytree3bkg, "Nfatjets")==0:
  cut8 = cut8 + 1
  cut8weighed = cut8weighed + weight
 else: continue            
 if getattr(mytree3bkg, "mt")>200 and getattr(mytree3bkg, "mt")<380:
  cut9 = cut9 + 1
  cut9weighed = cut9weighed + weight
 if getattr(mytree3bkg, "mt")>380:
  cut10 = cut10 + 1
  cut10weighed = cut10weighed + weight
 else: continue
            
for d_entry in range(entries4bkg):
 mytree4bkg.GetEvent(d_entry)
 weight = getattr(mytree4bkg, "genWeight")*getattr(mytree4bkg, "pileupWeight")*getattr(mytree4bkg, "eventWeight")*getattr(mytree4bkg, "leptonWeight")*getattr(mytree4bkg, "bTagWeight")
 if (getattr(mytree4bkg, "met")>200 and getattr(mytree4bkg, "nJet30")>=1 and getattr(mytree4bkg, "nLep_base")==1 and getattr(mytree4bkg, "nLep_signal")==1 and getattr(mytree4bkg, "mjj")<200 and getattr(mytree4bkg, "mjj")>50 getattr(mytree4bkg, "mt")>50):
  cutPS = cutPS + 1
  cutPSweighed = cutPSweighed + weight
 else: continue
 if getattr(mytree4bkg, "nLep_base")==1 and getattr(mytree4bkg, "nLep_signal")==1:
  cut1 = cut1 + 1
  cut1weighed = cut1weighed + weight
 else: continue
 if getattr(mytree4bkg, "lep1Pt")>25:
  cut2 = cut2 + 1
  cut2weighed = cut2weighed + weight
 else: continue
 if getattr(mytree4bkg, "nJet30")==2 or getattr(mytree4bkg, "nJet30")==3:
  cut3 = cut3 + 1
  cut3weighed = cut3weighed + weight
 else: continue 
 if getattr(mytree4bkg, "nBJet30_DL1")==0:
  cut4 = cut4 + 1
  cut4weighed = cut4weighed + weight
 else: continue
 if getattr(mytree4bkg, "met")>200:
  cut5 = cut5 + 1
  cut5weighed = cut5weighed + weight
 else: continue
 if getattr(mytree4bkg, "met_phi")<2.8:
  cut6 = cut6 + 1
  cut6weighed = cut6weighed + weight
 else: continue
 if getattr(mytree4bkg, "mjj")<105 and getattr(mytree4bkg, "mjj")>70:
  cut7 = cut7 + 1
  cut7weighed = cut7weighed + weight
 else: continue
 if getattr(mytree4bkg, "Nfatjets")==0:
  cut8 = cut8 + 1
  cut8weighed = cut8weighed + weight
 else: continue            
 if getattr(mytree4bkg, "mt")>200 and getattr(mytree4bkg, "mt")<380:
  cut9 = cut9 + 1
  cut9weighed = cut9weighed + weight
 if getattr(mytree4bkg, "mt")>380:
  cut10 = cut10 + 1
  cut10weighed = cut10weighed + weight
 else: continue
            
for e_entry in range(entries5bkg):
 mytree5bkg.GetEvent(e_entry)
 weight = getattr(mytree5bkg, "genWeight")*getattr(mytree5bkg, "pileupWeight")*getattr(mytree5bkg, "eventWeight")*getattr(mytree5bkg, "leptonWeight")*getattr(mytree5bkg, "bTagWeight")
 if (getattr(mytree5bkg, "met")>200 and getattr(mytree5bkg, "nJet30")>=1 and getattr(mytree5bkg, "nLep_base")==1 and getattr(mytree5bkg, "nLep_signal")==1 and getattr(mytree5bkg, "mjj")<200 and getattr(mytree5bkg, "mjj")>50 getattr(mytree5bkg, "mt")>50):
  cutPS = cutPS + 1
  cutPSweighed = cutPSweighed + weight
 else: continue
 if getattr(mytree5bkg, "nLep_base")==1 and getattr(mytree5bkg, "nLep_signal")==1:
  cut1 = cut1 + 1
  cut1weighed = cut1weighed + weight
 else: continue
 if getattr(mytree5bkg, "lep1Pt")>25:
  cut2 = cut2 + 1
  cut2weighed = cut2weighed + weight
 else: continue
 if getattr(mytree5bkg, "nJet30")==2 or getattr(mytree5bkg, "nJet30")==3:
  cut3 = cut3 + 1
  cut3weighed = cut3weighed + weight
 else: continue 
 if getattr(mytree5bkg, "nBJet30_DL1")==0:
  cut4 = cut4 + 1
  cut4weighed = cut4weighed + weight
 else: continue
 if getattr(mytree5bkg, "met")>200:
  cut5 = cut5 + 1
  cut5weighed = cut5weighed + weight
 else: continue
 if getattr(mytree5bkg, "met_phi")<2.8:
  cut6 = cut6 + 1
  cut6weighed = cut6weighed + weight
 else: continue
 if getattr(mytree5bkg, "mjj")<105 and getattr(mytree5bkg, "mjj")>70:
  cut7 = cut7 + 1
  cut7weighed = cut7weighed + weight
 else: continue
 if getattr(mytree5bkg, "Nfatjets")==0:
  cut8 = cut8 + 1
  cut8weighed = cut8weighed + weight
 else: continue            
 if getattr(mytree5bkg, "mt")>200 and getattr(mytree5bkg, "mt")<380:
  cut9 = cut9 + 1
  cut9weighed = cut9weighed + weight
 if getattr(mytree5bkg, "mt")>380:
  cut10 = cut10 + 1
  cut10weighed = cut10weighed + weight
 else: continue
            
for f_entry in range(entries6bkg):
 mytree6bkg.GetEvent(f_entry)
 weight = getattr(mytree6bkg, "genWeight")*getattr(mytree6bkg, "pileupWeight")*getattr(mytree6bkg, "eventWeight")*getattr(mytree6bkg, "leptonWeight")*getattr(mytree6bkg, "bTagWeight")
 if (getattr(mytree6bkg, "met")>200 and getattr(mytree6bkg, "nJet30")>=1 and getattr(mytree6bkg, "nLep_base")==1 and getattr(mytree6bkg, "nLep_signal")==1 and getattr(mytree6bkg, "mjj")<200 and getattr(mytree6bkg, "mjj")>50 getattr(mytree6bkg, "mt")>50):
  cutPS = cutPS + 1
  cutPSweighed = cutPSweighed + weight
 else: continue
 if getattr(mytree6bkg, "nLep_base")==1 and getattr(mytree6bkg, "nLep_signal")==1:
  cut1 = cut1 + 1
  cut1weighed = cut1weighed + weight
 else: continue
 if getattr(mytree6bkg, "lep1Pt")>25:
  cut2 = cut2 + 1
  cut2weighed = cut2weighed + weight
 else: continue
 if getattr(mytree6bkg, "nJet30")==2 or getattr(mytree6bkg, "nJet30")==3:
  cut3 = cut3 + 1
  cut3weighed = cut3weighed + weight
 else: continue 
 if getattr(mytree6bkg, "nBJet30_DL1")==0:
  cut4 = cut4 + 1
  cut4weighed = cut4weighed + weight
 else: continue
 if getattr(mytree6bkg, "met")>200:
  cut5 = cut5 + 1
  cut5weighed = cut5weighed + weight
 else: continue
 if getattr(mytree6bkg, "met_phi")<2.8:
  cut6 = cut6 + 1
  cut6weighed = cut6weighed + weight
 else: continue
 if getattr(mytree6bkg, "mjj")<105 and getattr(mytree6bkg, "mjj")>70:
  cut7 = cut7 + 1
  cut7weighed = cut7weighed + weight
 else: continue
 if getattr(mytree6bkg, "Nfatjets")==0:
  cut8 = cut8 + 1
  cut8weighed = cut8weighed + weight
 else: continue            
 if getattr(mytree6bkg, "mt")>200 and getattr(mytree6bkg, "mt")<380:
  cut9 = cut9 + 1
  cut9weighed = cut9weighed + weight
 if getattr(mytree6bkg, "mt")>380:
  cut10 = cut10 + 1
  cut10weighed = cut10weighed + weight
 else: continue  
            
for g_entry in range(entries7bkg):
 mytree7bkg.GetEvent(g_entry)
 weight = getattr(mytree7bkg, "genWeight")*getattr(mytree7bkg, "pileupWeight")*getattr(mytree7bkg, "eventWeight")*getattr(mytree7bkg, "leptonWeight")*getattr(mytree7bkg, "bTagWeight")
 if (getattr(mytree7bkg, "met")>200 and getattr(mytree7bkg, "nJet30")>=1 and getattr(mytree7bkg, "nLep_base")==1 and getattr(mytree7bkg, "nLep_signal")==1 and getattr(mytree7bkg, "mjj")<200 and getattr(mytree7bkg, "mjj")>50 getattr(mytree7bkg, "mt")>50):
  cutPS = cutPS + 1
  cutPSweighed = cutPSweighed + weight
 else: continue
 if getattr(mytree7bkg, "nLep_base")==1 and getattr(mytree7bkg, "nLep_signal")==1:
  cut1 = cut1 + 1
  cut1weighed = cut1weighed + weight
 else: continue
 if getattr(mytree7bkg, "lep1Pt")>25:
  cut2 = cut2 + 1
  cut2weighed = cut2weighed + weight
 else: continue
 if getattr(mytree7bkg, "nJet30")==2 or getattr(mytree7bkg, "nJet30")==3:
  cut3 = cut3 + 1
  cut3weighed = cut3weighed + weight
 else: continue 
 if getattr(mytree7bkg, "nBJet30_DL1")==0:
  cut4 = cut4 + 1
  cut4weighed = cut4weighed + weight
 else: continue
 if getattr(mytree7bkg, "met")>200:
  cut5 = cut5 + 1
  cut5weighed = cut5weighed + weight
 else: continue
 if getattr(mytree7bkg, "met_phi")<2.8:
  cut6 = cut6 + 1
  cut6weighed = cut6weighed + weight
 else: continue
 if getattr(mytree7bkg, "mjj")<105 and getattr(mytree7bkg, "mjj")>70:
  cut7 = cut7 + 1
  cut7weighed = cut7weighed + weight
 else: continue
 if getattr(mytree7bkg, "Nfatjets")==0:
  cut8 = cut8 + 1
  cut8weighed = cut8weighed + weight
 else: continue            
 if getattr(mytree7bkg, "mt")>200 and getattr(mytree7bkg, "mt")<380:
  cut9 = cut9 + 1
  cut9weighed = cut9weighed + weight
 if getattr(mytree7bkg, "mt")>380:
  cut10 = cut10 + 1
  cut10weighed = cut10weighed + weight
 else: continue
            
for h_entry in range(entries8bkg):
 mytree8bkg.GetEvent(h_entry)
 weight = getattr(mytree8bkg, "genWeight")*getattr(mytree8bkg, "pileupWeight")*getattr(mytree8bkg, "eventWeight")*getattr(mytree8bkg, "leptonWeight")*getattr(mytree8bkg, "bTagWeight")
 if (getattr(mytree8bkg, "met")>200 and getattr(mytree8bkg, "nJet30")>=1 and getattr(mytree8bkg, "nLep_base")==1 and getattr(mytree8bkg, "nLep_signal")==1 and getattr(mytree8bkg, "mjj")<200 and getattr(mytree8bkg, "mjj")>50 getattr(mytree8bkg, "mt")>50):
  cutPS = cutPS + 1
  cutPSweighed = cutPSweighed + weight
 else: continue
 if getattr(mytree8bkg, "nLep_base")==1 and getattr(mytree8bkg, "nLep_signal")==1:
  cut1 = cut1 + 1
  cut1weighed = cut1weighed + weight
 else: continue
 if getattr(mytree8bkg, "lep1Pt")>25:
  cut2 = cut2 + 1
  cut2weighed = cut2weighed + weight
 else: continue
 if getattr(mytree8bkg, "nJet30")==2 or getattr(mytree8bkg, "nJet30")==3:
  cut3 = cut3 + 1
  cut3weighed = cut3weighed + weight
 else: continue 
 if getattr(mytree8bkg, "nBJet30_DL1")==0:
  cut4 = cut4 + 1
  cut4weighed = cut4weighed + weight
 else: continue
 if getattr(mytree8bkg, "met")>200:
  cut5 = cut5 + 1
  cut5weighed = cut5weighed + weight
 else: continue
 if getattr(mytree8bkg, "met_phi")<2.8:
  cut6 = cut6 + 1
  cut6weighed = cut6weighed + weight
 else: continue
 if getattr(mytree8bkg, "mjj")<105 and getattr(mytree8bkg, "mjj")>70:
  cut7 = cut7 + 1
  cut7weighed = cut7weighed + weight
 else: continue
 if getattr(mytree8bkg, "Nfatjets")==0:
  cut8 = cut8 + 1
  cut8weighed = cut8weighed + weight
 else: continue            
 if getattr(mytree8bkg, "mt")>200 and getattr(mytree8bkg, "mt")<380:
  cut9 = cut9 + 1
  cut9weighed = cut9weighed + weight
 if getattr(mytree8bkg, "mt")>380:
  cut10 = cut10 + 1
  cut10weighed = cut10weighed + weight
 else: continue
            
for l_entry in range(entries9bkg):
 mytree9bkg.GetEvent(l_entry)
 weight = getattr(mytree9bkg, "genWeight")*getattr(mytree9bkg, "pileupWeight")*getattr(mytree9bkg, "eventWeight")*getattr(mytree9bkg, "leptonWeight")*getattr(mytree9bkg, "bTagWeight")
 if (getattr(mytree9bkg, "met")>200 and getattr(mytree9bkg, "nJet30")>=1 and getattr(mytree9bkg, "nLep_base")==1 and getattr(mytree9bkg, "nLep_signal")==1 and getattr(mytree9bkg, "mjj")<200 and getattr(mytree9bkg, "mjj")>50 getattr(mytree9bkg, "mt")>50):
  cutPS = cutPS + 1
  cutPSweighed = cutPSweighed + weight
 else: continue
 if getattr(mytree9bkg, "nLep_base")==1 and getattr(mytree9bkg, "nLep_signal")==1:
  cut1 = cut1 + 1
  cut1weighed = cut1weighed + weight
 else: continue
 if getattr(mytree9bkg, "lep1Pt")>25:
  cut2 = cut2 + 1
  cut2weighed = cut2weighed + weight
 else: continue
 if getattr(mytree9bkg, "nJet30")==2 or getattr(mytree9bkg, "nJet30")==3:
  cut3 = cut3 + 1
  cut3weighed = cut3weighed + weight
 else: continue 
 if getattr(mytree9bkg, "nBJet30_DL1")==0:
  cut4 = cut4 + 1
  cut4weighed = cut4weighed + weight
 else: continue
 if getattr(mytree9bkg, "met")>200:
  cut5 = cut5 + 1
  cut5weighed = cut5weighed + weight
 else: continue
 if getattr(mytree9bkg, "met_phi")<2.8:
  cut6 = cut6 + 1
  cut6weighed = cut6weighed + weight
 else: continue
 if getattr(mytree9bkg, "mjj")<105 and getattr(mytree9bkg, "mjj")>70:
  cut7 = cut7 + 1
  cut7weighed = cut7weighed + weight
 else: continue
 if getattr(mytree9bkg, "Nfatjets")==0:
  cut8 = cut8 + 1
  cut8weighed = cut8weighed + weight
 else: continue            
 if getattr(mytree9bkg, "mt")>200 and getattr(mytree9bkg, "mt")<380:
  cut9 = cut9 + 1
  cut9weighed = cut9weighed + weight
 if getattr(mytree9bkg, "mt")>380:
  cut10 = cut10 + 1
  cut10weighed = cut10weighed + weight
 else: continue
            
            
           
