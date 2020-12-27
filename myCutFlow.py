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
                      if mytree1.GetLeaf("mt").GetValue()>100 and mytree1.GetLeaf("mt").GetValue()<140 and mytree1.GetLeaf("met").GetValue()>200 and mytree1.GetLeaf("nJet30").GetValue()>=2 and mytree1.GetLeaf("nJet30").GetValue()<4 and mytree1.GetLeaf("mct2").GetValue()>160 and mytree1.GetLeaf("nLep_base").GetValue()==1 andmytree1.GetLeaf("nLep_signal").GetValue()==1 and mytree1.GetLeaf("mt").GetValue()>50 and mytree1.GetLeaf("nBJet30_MV2c10").GetValue()==2 and mytree1.GetLeaf("mbb").GetValue()>105 and mytree1.GetLeaf("mbb").GetValue()<135:
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
