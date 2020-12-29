from ROOT import *
import re
import os
import math
import logging
import re
import glob
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
 if getattr(mytree1, "lep1Pt") > 25:
  cut2 = cut2 + 1
  cut2weighed = cut2weighed + weight
 else: continue
 if getattr(mytree1, "nJet30")==2 or getattr(mytree1, "nJet30")==3:
  cut3 = cut3 + 1
  cut3weighed = cut3weighed + weight
 else: continue 
 if getattr(mytree1, "nBJet30_DL1)==0:
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
 if getattr(mytree1, "")==0:
  cut8 = cut8 + 1
  cut8weighed = cut8weighed + weight
 else: continue
            
print(count1)
print(count2)
print(count3)

count1b = 0
count2b = 0
count3b = 0

for i_entry in range(entries2):
 mytree2.GetEvent(i_entry)
 if (mytree2.GetLeaf("met").GetValue()>150.0 and mytree2.GetLeaf("nJet30").GetValue()>=2 and mytree2.GetLeaf("nJet30").GetValue()<4 and mytree2.GetLeaf("nLep_base").GetValue()==1 and mytree2.GetLeaf("nLep_signal").GetValue()==1 and mytree2.GetLeaf("mt").GetValue()>50):
  count1b = count1b +1
  if mytree2.GetLeaf("nBJet30_MV2c10").GetValue()==2:
      if mytree2.GetLeaf("mbb").GetValue()>50:
          if mytree2.GetLeaf("mbb").GetValue()>105 and mytree2.GetLeaf("mbb").GetValue()<135 :
              if mytree2.GetLeaf("mct2").GetValue()>160 :
                  if mytree2.GetLeaf("met").GetValue()>200 :
                      count2b = count2b + 1
                      if mytree2.GetLeaf("mt").GetValue()>100 and mytree2.GetLeaf("mt").GetValue()<140 and mytree2.GetLeaf("met").GetValue()>200 and mytree2.GetLeaf("nJet30").GetValue()>=2 and mytree2.GetLeaf("nJet30").GetValue()<4 and mytree2.GetLeaf("mct2").GetValue()>160 and mytree2.GetLeaf("nLep_base").GetValue()==1 and mytree2.GetLeaf("nLep_signal").GetValue()==1 and mytree2.GetLeaf("mt").GetValue()>50 and mytree2.GetLeaf("nBJet30_MV2c10").GetValue()==2 and mytree2.GetLeaf("mbb").GetValue()>105 and mytree2.GetLeaf("mbb").GetValue()<135:
                       count3b = count3b + 1
                      else: continue
                  else: continue
              else: continue
          else: continue
      else: continue
  else: continue
 else: continue
  
print(count1b)
print(count2b)
print(count3b)

count1c = 0
count2c = 0
count3c = 0

for w_entry in range(entries3):
 mytree3.GetEvent(w_entry)
 if (mytree3.GetLeaf("met").GetValue()>150.0 and mytree3.GetLeaf("nJet30").GetValue()>=2 and mytree3.GetLeaf("nJet30").GetValue()<4 and mytree3.GetLeaf("nLep_base").GetValue()==1 and mytree3.GetLeaf("nLep_signal").GetValue()==1 and mytree3.GetLeaf("mt").GetValue()>50):
  count1c = count1c +1
  if mytree3.GetLeaf("nBJet30_MV2c10").GetValue()==2:
      if mytree3.GetLeaf("mbb").GetValue()>50:
          if mytree3.GetLeaf("mbb").GetValue()>105 and mytree3.GetLeaf("mbb").GetValue()<135 :
              if mytree3.GetLeaf("mct2").GetValue()>160 :
                  if mytree3.GetLeaf("met").GetValue()>200 :
                      count2c = count2c + 1
                      if mytree3.GetLeaf("mt").GetValue()>100 and mytree3.GetLeaf("mt").GetValue()<140 and mytree3.GetLeaf("met").GetValue()>200 and mytree3.GetLeaf("nJet30").GetValue()>=2 and mytree3.GetLeaf("nJet30").GetValue()<4 and mytree3.GetLeaf("mct2").GetValue()>160 and mytree3.GetLeaf("nLep_base").GetValue()==1 and mytree3.GetLeaf("nLep_signal").GetValue()==1 and mytree3.GetLeaf("mt").GetValue()>50 and mytree3.GetLeaf("nBJet30_MV2c10").GetValue()==2 and mytree3.GetLeaf("mbb").GetValue()>105 and mytree3.GetLeaf("mbb").GetValue()<135:
                       count3c = count3c + 1
                      else: continue
                  else: continue
              else: continue
          else: continue
      else: continue
  else: continue
 else: continue

print(count1c)
print(count2c)
print(count3c)

myfile2 = TFile('allTrees_bkg_NoSys.root')
mytree1bkg = myfile.Get('diboson_NoSys')
mytree2bkg = myfile.Get('multiboson_NoSys')
mytree3bkg = myfile.Get('singletop_NoSys')
mytree4bkg = myfile.Get('ttbar_NoSys')
mytree5bkg = myfile.Get('tth_NoSys')
mytree6bkg = myfile.Get('ttv_NoSys')
mytree7bkg = myfile.Get('vh_NoSys')
mytree8bkg = myfile.Get('wjets_NoSys')
mytree9bkg = myfile.Get('zjets_NoSys')

entries1bkg = mytree1bkg.GetEntriesFast()
entries2bkg = mytree2bkg.GetEntriesFast()
entries3bkg = mytree3bkg.GetEntriesFast()
entries4bkg = mytree4bkg.GetEntriesFast()
entries5bkg = mytree5bkg.GetEntriesFast()
entries6bkg = mytree6bkg.GetEntriesFast()
entries7bkg = mytree7bkg.GetEntriesFast()
entries8bkg = mytree8bkg.GetEntriesFast()
entries9bkg = mytree9bkg.GetEntriesFast()

countbkg1 = 0
countbkg1b = 0
countbkg2 = 0
countbkg2b = 0
countbkg3 = 0
countbkg3b = 0
countbkg4 = 0
countbkg4b = 0
countbkg5 = 0
countbkg5b = 0
countbkg6 = 0
countbkg6b = 0
countbkg7 = 0
countbkg7b = 0
countbkg8 = 0
countbkg8b = 0
countbkg9 = 0
countbkg9b = 0

for a_entry in range(entries1bkg):
 mytree1bkg.GetEvent(a_entry)
 if (mytree1bkg.GetLeaf("met").GetValue()>200 and mytree1bkg.GetLeaf("nJet30").GetValue()>=2 and mytree1bkg.GetLeaf("met").GetValue()<4 and mytree1bkg.GetLeaf("nLep_base").GetValue()==1 and mytree1bkg.GetLeaf("nLep_signal").GetValue()==1):
  countbkg1 = countbkg1 + 1
  if mytree1bkg.GetLeaf("mt").GetValue()>50:
   if mytree1bkg.GetLeaf("nBJet30_MV2c10").GetValue()==2:
    if mytree1bkg.GetLeaf("mbb").GetValue()>50:
     if mytree1bkg.GetLeaf("mbb").GetValue()>105 and mytree1bkg.GetLeaf("mbb").GetValue()<135:
      if mytree1bkg.GetLeaf("mct2").GetValue()>240:
       if mytree1bkg.GetLeaf("met").GetValue()>240:
        if mytree1bkg.GetLeaf("mt").GetValue()>100:
         countbkg1b = countbkg1b + 1
        else: continue
       else: continue
      else: continue
     else: continue
    else: continue
   else: continue
  else: continue
 else: continue
 
for b_entry in range(entries2bkg):
 mytree2bkg.GetEvent(b_entry)
 if (mytree2bkg.GetLeaf("met").GetValue()>200 and mytree2bkg.GetLeaf("nJet30").GetValue()>=2 and mytree2bkg.GetLeaf("met").GetValue()<4 and mytree2bkg.GetLeaf("nLep_base").GetValue()==1 and mytree2bkg.GetLeaf("nLep_signal").GetValue()==1):
  countbkg2 = countbkg2 + 1
  if mytree2bkg.GetLeaf("mt").GetValue()>50:
   if mytree2bkg.GetLeaf("nBJet30_MV2c10").GetValue()==2:
    if mytree2bkg.GetLeaf("mbb").GetValue()>50:
     if mytree2bkg.GetLeaf("mbb").GetValue()>105 and mytree2bkg.GetLeaf("mbb").GetValue()<135:
      if mytree2bkg.GetLeaf("mct2").GetValue()>240:
       if mytree2bkg.GetLeaf("met").GetValue()>240:
        if mytree2bkg.GetLeaf("mt").GetValue()>100:
         countbkg2b = countbkg2b + 1
        else: continue
       else: continue
      else: continue
     else: continue
    else: continue
   else: continue
  else: continue
 else: continue 

for c_entry in range(entries3bkg):
 mytree3bkg.GetEvent(c_entry)
 if (mytree3bkg.GetLeaf("met").GetValue()>200 and mytree3bkg.GetLeaf("nJet30").GetValue()>=2 and mytree3bkg.GetLeaf("met").GetValue()<4 and mytree3bkg.GetLeaf("nLep_base").GetValue()==1 and mytree3bkg.GetLeaf("nLep_signal").GetValue()==1):
  countbkg3 = countbkg3 + 1
  if mytree3bkg.GetLeaf("mt").GetValue()>50:
   if mytree3bkg.GetLeaf("nBJet30_MV2c10").GetValue()==2:
    if mytree3bkg.GetLeaf("mbb").GetValue()>50:
     if mytree3bkg.GetLeaf("mbb").GetValue()>105 and mytree3bkg.GetLeaf("mbb").GetValue()<135:
      if mytree3bkg.GetLeaf("mct2").GetValue()>240:
       if mytree3bkg.GetLeaf("met").GetValue()>240:
        if mytree3bkg.GetLeaf("mt").GetValue()>100:
         countbkg3b = countbkg3b + 1
        else: continue
       else: continue
      else: continue
     else: continue
    else: continue
   else: continue
  else: continue
 else: continue

for a_entry in range(entries1bkg):
 mytree1bkg.GetEvent(a_entry)
 if (mytree1bkg.GetLeaf("met").GetValue()>200 and mytree1bkg.GetLeaf("nJet30").GetValue()>=2 and mytree1bkg.GetLeaf("met").GetValue()<4 and mytree1bkg.GetLeaf("nLep_base").GetValue()==1 and mytree1bkg.GetLeaf("nLep_signal").GetValue()==1):
  countbkg1 = countbkg1 + 1
  if mytree1bkg.GetLeaf("mt").GetValue()>50:
   if mytree1bkg.GetLeaf("nBJet30_MV2c10").GetValue()==2:
    if mytree1bkg.GetLeaf("mbb").GetValue()>50:
     if mytree1bkg.GetLeaf("mbb").GetValue()>105 and mytree1bkg.GetLeaf("mbb").GetValue()<135:
      if mytree1bkg.GetLeaf("mct2").GetValue()>240:
       if mytree1bkg.GetLeaf("met").GetValue()>240:
        if mytree1bkg.GetLeaf("mt").GetValue()>100:
         countbkg1b = countbkg1b + 1
        else: continue
       else: continue
      else: continue
     else: continue
    else: continue
   else: continue
  else: continue
 else: continue 
