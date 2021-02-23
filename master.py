import os

os.system ("python myCutFlow.py")

print("do you want analyze the data also with TMVA using the BDT?[y/n]")

tmva = input()

if (tmva == 'y'):
 os.system ("root")
 os.system (".L tmva_cut.C")
 os.system ("tmva_cut()")

