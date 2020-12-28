from ROOT import *
import re
import os
import math
import logging
import re
import glob
from pprint import pprint

myfile = TFile('allTrees_signal_NoSys.root')
mytree1 = myfile.Get('C1N2_WZ_300_0_NoSys')
mytree2 = myfile.Get('C1N2_WZ_500_200_NoSys')
mytree3 = myfile.Get('C1N2_WZ_1200_200_NoSys')

entries1 = mytree1.GetEntriesFast()
entries2 = mytree2.GetEntriesFast()
entries3 = mytree3.GetEntriesFast()

print(entries1)
print(entries2)
print(entries3)

count1 = 0
count2 = 0
count3 = 0

for j_entry in range(entries1):
 mytree1.GetEvent(j_entry)
 if (mytree1.GetLeaf("met").GetValue()>150.0 and mytree1.GetLeaf("nJet30").GetValue()>=2 and mytree1.GetLeaf("nJet30").GetValue()<4 and mytree1.GetLeaf("nLep_base").GetValue()==1 and mytree1.GetLeaf("nLep_signal").GetValue()==1 and mytree1.GetLeaf("mt").GetValue()>50):
  count1 = count1 +1
  if mytree1.GetLeaf("nBJet30_MV2c10").GetValue()==2:
      if mytree1.GetLeaf("mbb").GetValue()>50:
          if mytree1.GetLeaf("mbb").GetValue()>105 and mytree1.GetLeaf("mbb").GetValue()<135 :
              if mytree1.GetLeaf("mct2").GetValue()>160 :
                  if mytree1.GetLeaf("met").GetValue()>200 :
                      count2 = count2 + 1
                      if mytree1.GetLeaf("mt").GetValue()>100 and mytree1.GetLeaf("mt").GetValue()<140 and mytree1.GetLeaf("met").GetValue()>200 and mytree1.GetLeaf("nJet30").GetValue()>=2 and mytree1.GetLeaf("nJet30").GetValue()<4 and mytree1.GetLeaf("mct2").GetValue()>160 and mytree1.GetLeaf("nLep_base").GetValue()==1 and mytree1.GetLeaf("nLep_signal").GetValue()==1 and mytree1.GetLeaf("mt").GetValue()>50 and mytree1.GetLeaf("nBJet30_MV2c10").GetValue()==2 and mytree1.GetLeaf("mbb").GetValue()>105 and mytree1.GetLeaf("mbb").GetValue()<135:
                       count3 = count3 + 1
                      else: continue
                  else: continue
              else: continue
          else: continue
      else: continue
  else: continue
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
 
 
