import os

os.system ("python myCutFlow.py")

print("Do you want analyze the data also with TMVA using the BDT?[y/n]")

tmva = raw_input()

while (tmva != 'y' and tmva != 'n')
 print("Do you want analyze the data also with TMVA using the BDT?[y/n]")
 tmva = raw_input()


if (tmva == 'y'):
 os.system ("root tmva_cut.C")

