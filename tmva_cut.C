
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>

#include "TChain.h"
#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TObjString.h"
#include "TSystem.h"
#include "TROOT.h"

#include "TMVA/Factory.h"
#include "TMVA/DataLoader.h"
#include "TMVA/Tools.h"
#include "TMVA/TMVAGui.h"


void a() {
    
    auto inputFile_signal = TFile::Open("allTrees_signal_NoSys.root");
    auto inputFile_bkg = TFile::Open("allTrees_bkg_NoSys.root");
    
    //Length,Width,Size,Conc,Conc1,Asym,M3Long,M3Trans,Alpha,Dist;
    //TFile* outputFile = TFile::Open("TMVAOutputCV.root", "RECREATE");
    
    auto outputFile = TFile::Open( "TMVAOutputCV.root", "RECREATE" );

    TMVA::Factory factory("TMVAClassification", outputFile, "!V:ROC:!Correlations:!Silent:Color:!DrawProgressBar:AnalysisType=Classification");
    
    TMVA::DataLoader loader("dataset");

    loader.AddVariable("nLep_base");
    loader.AddVariable("nLep_signal");
    loader.AddVariable("lep1Pt");
    loader.AddVariable("nJet30");
    loader.AddVariable("nBJet30_DL1");
    loader.AddVariable("met");
    loader.AddVariable("met_Phi");
    loader.AddVariable("nFatjets");
    loader.AddVariable("mt");
//loader.AddVariable("Dist");
    
    TTree* tsignal;
    TTree* tbackground;
    inputFile_signal->GetObject("C1N2_WZ_300_0_NoSys", tsignal);
    inputFile_bkg->GetObject("diboson_NoSys", tbackground);

    loader.AddSignalTree(tsignal, 1.0);
    loader.AddBackgroundTree(tbackground, 1.0);
    
    // Apply additional cuts on the signal and background samples
    TCut mycuts = "met>200 && nJet30>=1 && nLep_base==1 && nLep_signal==1 && mt>50"; // for example: TCut mycuts = "abs(var1)<0.5 && abs(var2-0.5)<1";
    TCut mycutb = "met>200 && nJet30>=1 && nLep_base==1 && nLep_signal==1 && mt>50"; // for example: TCut mycutb = "abs(var1)<0.5";
    
    // Tell the dataloader how to use the training and testing events
    loader.PrepareTrainingAndTestTree(mycuts, mycutb, "NTrain_Signal=0:NTrain_Background=0:NTest_Signal=0:NTest_Background=0");
    
    //Book MVA methods
    //Cuts
        factory.BookMethod( &loader, TMVA::Types::kCuts, "Cuts", "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart" );
    // Fisher discriminant
//       factory.BookMethod( &loader, TMVA::Types::kFisher, "Fisher", "H:!V:Fisher:VarTransform=None:CreateMVAPdfs:PDFInterpolMVAPdf=Spline2:NbinsMVAPdf=50:NsmoothMVAPdf=10" );
    //MLPBNN
    //factory.BookMethod(TMVA::Types::kMLP, "MLP", "H:!V:HiddenLayers=3");
//      factory.BookMethod( &loader, TMVA::Types::kMLP, "MLPBNN", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=60:HiddenLayers=N+5:TestRate=5:TrainingMethod=BFGS:UseRegulator" );
    // Adaptive Boost
        factory.BookMethod( &loader, TMVA::Types::kBDT, "BDT","NTrees=200:BoostType=AdaBoost");
    
    // Tell the factory to train, test, and evaluate the MVAs
    // Train MVAs using the set of training events
    factory.TrainAllMethods();
    
    // Evaluate all MVAs using the set of test events
    factory.TestAllMethods();
    
    // Evaluate and compare performance of all configured MVAs
    factory.EvaluateAllMethods();
    
    //plot ROC curve
  auto c1 = factory.GetROCCurve(&loader);
  c1->Draw();
    
    // Save the output
  outputFile->Close();
    
    // Launch the GUI for the root macros
    //TMVA::TMVAGui("TMVAOutputCV.root");
   

}
