from ROOT import *
from array import *
import os
from math import *
from pprint import pprint


#take the file root for the signal
myfile = TFile('allTrees_signal_NoSys.root')

#study three different hypothesis for the masses of supersymmetric particles produced
signal_tree = [myfile.Get('C1N2_WZ_300_0_NoSys'), myfile.Get('C1N2_WZ_500_100_NoSys'), myfile.Get('C1N2_WZ_1200_200_NoSys')]

#total number of events in each trees
signal_entries = [0,0,0]
signal_entries[0] = signal_tree[0].GetEntries()
signal_entries[1] = signal_tree[1].GetEntries()
signal_entries[2] = signal_tree[2].GetEntries()

signal_name = ["WZ (300,0)", "WZ (500,100)", "WZ (1200,200)"]

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

bkg_counter_weighed = [["Preselection Cut",0,0,0,0,0,0,0,0,0,0,0],["Cut 1 (Nlep=1)",0,0,0,0,0,0,0,0,0],
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
for tree_number in range(0,3):
 for j_entry in range(signal_entries[tree_number]):
  signal_tree[tree_number].GetEvent(j_entry)
  weight = getattr(signal_tree[tree_number], "genWeight")*getattr(signal_tree[tree_number], "pileupWeight")*getattr(signal_tree[tree_number], "eventWeight")*getattr(signal_tree[tree_number], "leptonWeight")*getattr(signal_tree[tree_number], "bTagWeight")
  if (getattr(signal_tree[tree_number], "met")>200
      and getattr(signal_tree[tree_number], "nJet30")>=1
      and getattr(signal_tree[tree_number], "nLep_base")==1
      and getattr(signal_tree[tree_number], "nLep_signal")==1
      and getattr(signal_tree[tree_number], "mt")>50):
   signal_counter[0][tree_number+1] = signal_counter[0][tree_number+1] + 1
   signal_counter_weighed[0][tree_number+1] = signal_counter_weighed[0][tree_number+1] + weight
  else: continue
    
  if (getattr(signal_tree[tree_number], "nLep_base")==1
      and getattr(signal_tree[tree_number], "nLep_signal")==1):
   signal_counter[1][tree_number+1] = signal_counter[1][tree_number+1] + 1
   signal_counter_weighed[1][tree_number+1] = signal_counter_weighed[1][tree_number+1] + weight
  else: continue
    
  if getattr(signal_tree[tree_number], "lep1Pt")>25:
   signal_counter[2][tree_number+1] = signal_counter[2][tree_number+1] + 1
   signal_counter_weighed[2][tree_number+1] = signal_counter_weighed[2][tree_number+1] + weight
  else: continue
    
  if (getattr(signal_tree[tree_number], "nJet30")==2
      or getattr(signal_tree[tree_number], "nJet30")==3):
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
    
  if getattr(signal_tree[tree_number], "met_Phi")<2.8:
   signal_counter[6][tree_number+1] = signal_counter[6][tree_number+1] + 1
   signal_counter_weighed[6][tree_number+1] = signal_counter_weighed[6][tree_number+1] + weight
  else: continue
  
  jet1_pt = getattr(signal_tree[tree_number], "jet1Pt")
  jet1_Eta = getattr(signal_tree[tree_number], "jet1Eta")
  jet1_Phi = getattr(signal_tree[tree_number], "jet1Phi")
  jet2_pt = getattr(signal_tree[tree_number], "jet2Pt")
  jet2_Eta = getattr(signal_tree[tree_number], "jet2Eta")
  jet2_Phi = getattr(signal_tree[tree_number], "jet2Phi")
  mjj = sqrt(2*jet1_pt*jet2_pt*(cosh(jet1_Eta-jet2_Eta)-cos(jet1_Phi-jet2_Phi)))
  if (mjj<105
      and mjj>70):
   signal_counter[7][tree_number+1] = signal_counter[7][tree_number+1] + 1
   signal_counter_weighed[7][tree_number+1] = signal_counter_weighed[7][tree_number+1] + weight
  else: continue
  
  if getattr(signal_tree[tree_number], "nFatjets")==0:
   signal_counter[8][tree_number+1] = signal_counter[8][tree_number+1] + 1
   signal_counter_weighed[8][tree_number+1] = signal_counter_weighed[8][tree_number+1] + weight
  else: continue
  
  if (getattr(signal_tree[tree_number], "mt")>200
      and getattr(signal_tree[tree_number], "mt")<380):
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

for i in range(0,8):
 background_entries[i] = background_tree[i].GetEntriesFast()

background_name = ["Diboson", "Multiboson", "Single-top", "ttbar", "ttbarH", "ttbarV", "vh", "Wjets", "Zjets"]

for bkg_type in range(0,9):
 for i_entry in range(background_entries[bkg_type]):
  background_tree[bkg_type].GetEvent(i_entry)
  weight = getattr(background_tree[bkg_type], "genWeight")*getattr(background_tree[bkg_type], "pileupWeight")*getattr(background_tree[bkg_type], "eventWeight")*getattr(background_tree[bkg_type], "leptonWeight")*getattr(background_tree[bkg_type], "bTagWeight")
  if (getattr(background_tree[bkg_type], "met")>200
      and getattr(background_tree[bkg_type], "nJet30")>=1
      and getattr(background_tree[bkg_type], "nLep_base")==1
      and getattr(background_tree[bkg_type], "nLep_signal")==1
      and getattr(background_tree[bkg_type], "mt")>50):
    bkg_counter[0][bkg_type+1] = bkg_counter[0][bkg_type+1] + 1
    bkg_counter_weighed[0][bkg_type+1] = bkg_counter_weighed[0][bkg_type+1] + weight
  else: continue
  if (getattr(background_tree[bkg_type], "nLep_base")==1
      and getattr(background_tree[bkg_type], "nLep_signal")==1):
    bkg_counter[1][bkg_type+1] = bkg_counter[1][bkg_type+1] + 1
    bkg_counter_weighed[1][bkg_type+1] = bkg_counter_weighed[1][bkg_type+1] + weight
  else: continue
    
  if getattr(background_tree[bkg_type], "lep1Pt")>25:
    bkg_counter[2][bkg_type+1] = bkg_counter[2][bkg_type+1] + 1
    bkg_counter_weighed[2][bkg_type+1] = bkg_counter_weighed[2][bkg_type+1] + weight
  else: continue
    
  if (getattr(background_tree[bkg_type], "nJet30")==2
      or getattr(background_tree[bkg_type], "nJet30")==3):
   bkg_counter[3][bkg_type+1] = bkg_counter[3][bkg_type+1] + 1
   bkg_counter_weighed[3][bkg_type+1] = bkg_counter_weighed[3][bkg_type+1] + weight 
  else: continue
    
  if getattr(background_tree[bkg_type], "nBJet30_DL1")==0:
    bkg_counter[4][bkg_type+1] = bkg_counter[4][bkg_type+1] + 1
    bkg_counter_weighed[4][bkg_type+1] = bkg_counter_weighed[4][bkg_type+1] + weight
  else: continue
    
  if getattr(background_tree[bkg_type], "met")>200:
    bkg_counter[5][bkg_type+1] = bkg_counter[5][bkg_type+1] + 1
    bkg_counter_weighed[5][bkg_type+1] = bkg_counter_weighed[5][bkg_type+1] + weight
  else: continue
    
  if getattr(background_tree[bkg_type], "met_Phi")<2.8:
    bkg_counter[6][bkg_type+1] = bkg_counter[6][bkg_type+1] + 1
    bkg_counter_weighed[6][bkg_type+1] = bkg_counter_weighed[6][bkg_type+1] + weight
  else: continue
    
  jet1_pt = getattr(background_tree[bkg_type], "jet1Pt")
  jet1_Eta = getattr(background_tree[bkg_type], "jet1Eta")
  jet1_Phi = getattr(background_tree[bkg_type], "jet1Phi")
  jet2_pt = getattr(background_tree[bkg_type], "jet2Pt")
  jet2_Eta = getattr(background_tree[bkg_type], "jet2Eta")
  jet2_Phi = getattr(background_tree[bkg_type], "jet2Phi")
  mjj = sqrt(2*jet1_pt*jet2_pt*(cosh(jet1_Eta-jet2_Eta)-cos(jet1_Phi-jet2_Phi)))
  if (mjj<105
      and mjj>70):
    bkg_counter[7][bkg_type+1] = bkg_counter[7][bkg_type+1] + 1
    bkg_counter_weighed[7][bkg_type+1] = bkg_counter_weighed[7][bkg_type+1] + weight
  else: continue
    
  if getattr(background_tree[bkg_type], "nFatjets")==0:
    bkg_counter[8][bkg_type+1] = bkg_counter[8][bkg_type+1] + 1
    bkg_counter_weighed[8][bkg_type+1] = bkg_counter_weighed[8][bkg_type+1] + weight
  else: continue
    
  if (getattr(background_tree[bkg_type], "mt")>200
      and getattr(background_tree[bkg_type], "mt")<380):
    bkg_counter[9][bkg_type+1] = bkg_counter[9][bkg_type+1] + 1
    bkg_counter_weighed[9][bkg_type+1] = bkg_counter_weighed[9][bkg_type+1] + weight
    
  if getattr(background_tree[bkg_type], "mt")>380:
    bkg_counter[10][bkg_type+1] = bkg_counter[10][bkg_type+1] + 1
    bkg_counter_weighed[10][bkg_type+1] = bkg_counter_weighed[10][bkg_type+1] + weight
  else: continue

f = open("cut_result", "w", "a")
f.write("               ", signal_name[0], " ", signal_name[1], " ", signal_name[2], '\n')
    
for a in signal_counter:
  for b in a:
    f.write(b, " ")
  f.write('\n')

for c in signal_counter_weighed:
  for d in c:
    f.write(c, " ")
  f.write('\n')

for e in bkg_counter:
  for m in e:
    f.write(m, " ")
  f.write('\n')

for g in bkg_counter_weighed:
  for h in g:
    f.write(h, " ")
  f.write('\n')

f.close()

