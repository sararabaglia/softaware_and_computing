from ROOT import *
from array import *
import os
import math
from pprint import pprint


#take the file root for the signal
myfile = TFile('allTrees_signal_NoSys.root')

#study three different hypothesis for the masses of supersymmetric particles produced
signal_tree = [myfile.Get('C1N2_WZ_300_0_NoSys'), myfile.Get('C1N2_WZ_500_200_NoSys'), myfile.Get('C1N2_WZ_500_200_NoSys')]

#total number of events in each trees
signal_entries = [0,0,0]
signal_entries[0] = signal_tree[0].GetEntries()
signal_entries[1] = signal_tree[1].GetEntries()
signal_entries[2] = signal_tree[2].GetEntries()

signal_counter = [["Preselection Cut",0,0,0],["Cut 1 (Nlep=1)",0,0,0],
                  ["Cut 2 (pT>25)",0,0,0],
                  ["Cut 3 (Njet(pT>30)=2-3)",0,0,0],
                  ["Cut 4 (Nb-jet(pT>30)=0)",0,0,0],
                  ["Cut 5 (MET>200)",0,0,0],
                  ["Cut 6 (Delta_phi(l,met)<2.8)",0,0,0],
                  ["Cut 7 (70<mjj<105)",0,0,0],
                  ["Cut 8 (Nlarge-Rjet=0)",0,0,0],
                  ["Cut 9a (200<mT<380)",0,0,0],
                  ["Cut 9b (mT>380)",0,0,0]]
signal_counter_weighed = [["Preselection Cut",0,0,0],["Cut 1 (Nlep=1)",0,0,0],
                  ["Cut 2 (pT>25)",0,0,0],
                  ["Cut 3 (Njet(pT>30)=2-3)",0,0,0],
                  ["Cut 4 (Nb-jet(pT>30)=0)",0,0,0],
                  ["Cut 5 (MET>200)",0,0,0],
                  ["Cut 6 (Delta_phi(l,met)<2.8)",0,0,0],
                  ["Cut 7 (70<mjj<105)",0,0,0],
                  ["Cut 8 (Nlarge-Rjet=0)",0,0,0],
                  ["Cut 9a (200<mT<380)",0,0,0],
                  ["Cut 9b (mT>380)",0,0,0]]
bkg_counter = [["Preselection Cut",0,0,0,0,0,0,0,0,0,0,0],["Cut 1 (Nlep=1)",0,0,0,0,0,0,0,0,0],
                  ["Cut 2 (pT>25)",0,0,0,0,0,0,0,0,0],
                  ["Cut 3 (Njet(pT>30)=2-3)",0,0,0,0,0,0,0,0,0],
                  ["Cut 4 (Nb-jet(pT>30)=0)",0,0,0,0,0,0,0,0,0],
                  ["Cut 5 (MET>200)",0,0,0,0,0,0,0,0,0],
                  ["Cut 6 (Delta_phi(l,met)<2.8)",0,0,0,0,0,0,0,0,0],
                  ["Cut 7 (70<mjj<105)",0,0,0,0,0,0,0,0,0],
                  ["Cut 8 (Nlarge-Rjet=0)",0,0,0,0,0,0,0,0,0],
                  ["Cut 9a (200<mT<380)",0,0,0,0,0,0,0,0,0],
                  ["Cut 9b (mT>380)",0,0,0,0,0,0,0,0]]

#start analysis of first tree
#set to zero the value of the counters
for tree_number in range(0,2):
 for j_entry in range(signal_entries[tree_number]):
  signal_tree[tree_number].GetEvent(j_entry)
  weight = getattr(signal_tree[tree_number], "genWeight")*getattr(signal_tree[tree_number], "pileupWeight")*getattr(signal_tree[tree_number], "eventWeight")*getattr(signal_tree[tree_number], "leptonWeight")*getattr(signal_tree[tree_number], "bTagWeight")
  if (getattr(signal_tree[tree_number], "met")>200
      and getattr(signal_tree[tree_number], "nJet30")>=1
      and getattr(signal_tree[tree_number], "nLep_base")==1
      and getattr(signal_tree[tree_number], "nLep_signal")==1
      and getattr(signal_tree[tree_number], "mjj")<200
      and getattr(signal_tree[tree_number], "mjj")>50
      getattr(signal_tree[tree_number], "mt")>50):
   signal_counter[0][tree_number+1] = signal_counter[0][tree_number+1] + 1
   signal_counter_weighed[0][tree_number+1] = signal_counter_weighed[0][tree_number+1] + weight
  else: continue
  if getattr(signal_tree[tree_number], "nLep_base")==1 and getattr(signal_tree[tree_number], "nLep_signal")==1:
   signal_counter[1][tree_number+1] = signal_counter[1][tree_number+1] + 1
   signal_counter_weighed[1][tree_number+1] = signal_counter_weighed[1][tree_number+1] + weight
  else: continue
  if getattr(signal_tree[tree_number], "lep1Pt")>25:
   signal_counter[2][tree_number+1] = signal_counter[2][tree_number+1] + 1
   signal_counter_weighed[2][tree_number+1] = signal_counter_weighed[2][tree_number+1] + weight
  else: continue
  if getattr(signal_tree[tree_number], "nJet30")==2 or getattr(signal_tree[tree_number], "nJet30")==3:
   signal_counter[3][tree_number+1] = signal_counter[3][tree_number+1] + 1
   signal_counter_weighed[3][tree_number+1] = signal_counter_weighed[3][tree_number+1] + weight
  else: continue 
  if getattr(signal_tree[tree_number], "nBJet30_DL1")==0:
   signal_counter[4][tree_number+1] = signal_counter[4][tree_number+1] + 1
   signal_counter_weighed[4][tree_number+1] = signal_counter_weighed[4][tree_number+1] + weight
  else: continue
  if getattr(signal_tree[tree_number], "met")>200:
   signal_counter[5][tree_number+1] = signal_counter[5][tree_number+1] + 1
   signal_counter_weighed[5][tree_number+1] = signal_counter_weighed[5][tree_number+1] + weight
  else: continue
  if getattr(signal_tree[tree_number], "met_phi")<2.8:
   signal_counter[6][tree_number+1] = signal_counter[6][tree_number+1] + 1
   signal_counter_weighed[6][tree_number+1] = signal_counter_weighed[6][tree_number+1] + weight
 else: continue
 if getattr(signal_tree[tree_number], "mjj")<105 and getattr(signal_tree[tree_number], "mjj")>70:
  signal_counter[7][tree_number+1] = signal_counter[7][tree_number+1] + 1
  signal_counter_weighed[7][tree_number+1] = signal_counter_weighed[7][tree_number+1] + weight
 else: continue
 if getattr(signal_tree[tree_number], "")==0:
  signal_counter[8][tree_number+1] = signal_counter[8][tree_number+1] + 1
  signal_counter_weighed[8][tree_number+1] = signal_counter_weighed[8][tree_number+1] + weight
 else: continue            
 if getattr(signal_tree[tree_number], "mt")>200 and getattr(signal_tree[tree_number], "mt")<380:
  signal_counter[9][tree_number+1] = signal_counter[9][tree_number+1] + 1
  signal_counter_weighed[9][tree_number+1] = signal_counter_weighed[9][tree_number+1] + weight
 if getattr(signal_tree[tree_number], "mt")>380:
  signal_counter[10][tree_number+1] = signal_counter[10][tree_number+1] + 1
  signal_counter_weighed[10][tree_number+1] = signal_counter_weighed[10][tree_number+1] + weight
 else: continue

#end analysis of the signal

#start analysis of the background            

myfile2 = TFile('allTrees_bkg_NoSys.root')
background_tree = [myfile2.Get('diboson_NoSys'),
                   myfile2.Get('multiboson_NoSys'),
                   myfile2.Get('singletop_NoSys'),
                   myfile2.Get('ttbar_NoSys'),
                   myfile2.Get('tth_NoSys'),
                   myfile2.Get('ttv_NoSys'),
                   myfile2.Get('vh_NoSys'),
                   myfile2.Get('wjets_NoSys'),
                   myfile2.Get('zjets_NoSys')]

background_entries = [0,0,0,0,0,0,0,0,0]

for i in range(9):
 background_entries[i] = background_tree[i].GetEntriesFast()




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
 if getattr(mytree1bkg, "")==0:
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
 if getattr(mytree2bkg, "nBJet30_DL1)==0:
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
 if getattr(mytree2bkg, "")==0:
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
 if getattr(mytree3bkg, "nBJet30_DL1)==0:
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
 if getattr(mytree3bkg, "")==0:
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
 if getattr(mytree4bkg, "nBJet30_DL1)==0:
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
 if getattr(mytree4bkg, "")==0:
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
 if getattr(mytree5bkg, "nBJet30_DL1)==0:
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
 if getattr(mytree5bkg, "")==0:
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
 if getattr(mytree6bkg, "nBJet30_DL1)==0:
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
 if getattr(mytree6bkg, "")==0:
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
 if getattr(mytree7bkg, "nBJet30_DL1)==0:
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
 if getattr(mytree7bkg, "")==0:
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
 if getattr(mytree8bkg, "nBJet30_DL1)==0:
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
 if getattr(mytree8bkg, "")==0:
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
 if getattr(mytree9bkg, "nBJet30_DL1)==0:
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
 if getattr(mytree9bkg, "")==0:
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
            
            
           
