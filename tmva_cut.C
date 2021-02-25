
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


void tmva_cut() {
    cout << "Do you want run the whole programm or only a demonstration? (Push 1 for whole programm or 2 for demonstration)" << endl;
    char run;
    cin >> run;
    while (run != '1' && run != '2'){
     cout << "Push 1 for whole programm or 2 for demonstration" << endl;
     cin >> run;
    }
    
if (run == '1')
{
    auto inputFile_signal_1 = TFile::Open("/home/ATLAS-T3/student-26/software_and_computing/allTrees_signal_NoSys.root");
    auto inputFile_bkg = TFile::Open("/home/ATLAS-T3/student-26/software_and_computing/allTrees_bkg_NoSys.root");
    
    auto outputFile_1 = TFile::Open( "TMVAOutput_1.root", "RECREATE" );
    auto outputFile_2 = TFile::Open( "TMVAOutput_2.root", "RECREATE" );
    auto outputFile_3 = TFile::Open( "TMVAOutput_3.root", "RECREATE" );
    
    TMVA::Factory factory_1("TMVAClassification", outputFile_1, "!V:ROC:!Correlations:!Silent:Color:!DrawProgressBar:AnalysisType=Classification");
    TMVA::Factory factory_2("TMVAClassification", outputFile_2, "!V:ROC:!Correlations:!Silent:Color:!DrawProgressBar:AnalysisType=Classification");
    TMVA::Factory factory_3("TMVAClassification", outputFile_3, "!V:ROC:!Correlations:!Silent:Color:!DrawProgressBar:AnalysisType=Classification");
    
    TMVA::DataLoader loader_1("dataset_1");
    TMVA::DataLoader loader_2("dataset_2");
    TMVA::DataLoader loader_3("dataset_3");
    
    loader_1.AddVariable("nLep_base");
    loader_1.AddVariable("nLep_signal");
    loader_1.AddVariable("lep1Pt");
    loader_1.AddVariable("nJet30");
    loader_1.AddVariable("nBJet30_DL1");
    loader_1.AddVariable("met");
    loader_1.AddVariable("met_Phi");
    loader_1.AddVariable("nFatjets");
    loader_1.AddVariable("mt");
    
    loader_2.AddVariable("nLep_base");
    loader_2.AddVariable("nLep_signal");
    loader_2.AddVariable("lep1Pt");
    loader_2.AddVariable("nJet30");
    loader_2.AddVariable("nBJet30_DL1");
    loader_2.AddVariable("met");
    loader_2.AddVariable("met_Phi");
    loader_2.AddVariable("nFatjets");
    loader_2.AddVariable("mt");
    
    loader_3.AddVariable("nLep_base");
    loader_3.AddVariable("nLep_signal");
    loader_3.AddVariable("lep1Pt");
    loader_3.AddVariable("nJet30");
    loader_3.AddVariable("nBJet30_DL1");
    loader_3.AddVariable("met");
    loader_3.AddVariable("met_Phi");
    loader_3.AddVariable("nFatjets");
    loader_3.AddVariable("mt");
    
    TTree* tsignal_1;
    TTree* tsignal_2;
    TTree* tsignal_3;
    TTree* tbackground_1;
    TTree* tbackground_2;
    TTree* tbackground_3;
    TTree* tbackground_4;
    TTree* tbackground_5;
    TTree* tbackground_6;
    TTree* tbackground_7;
    TTree* tbackground_8;
    TTree* tbackground_9;
    
    inputFile_signal->GetObject("C1N2_WZ_300_0_NoSys", tsignal_1);
    inputFile_signal->GetObject("C1N2_WZ_500_100_NoSys", tsignal_2);
    inputFile_signal->GetObject("C1N2_WZ_1200_200_NoSys", tsignal_3);
    inputFile_bkg->GetObject("diboson_NoSys", tbackground_1);
    inputFile_bkg->GetObject("multiboson_NoSys", tbackground_2);
    inputFile_bkg->GetObject("singletop_NoSys", tbackground_3);
    inputFile_bkg->GetObject("ttbar_NoSys", tbackground_4);
    inputFile_bkg->GetObject("tth_NoSys", tbackground_5);
    inputFile_bkg->GetObject("ttv_NoSys", tbackground_6);
    inputFile_bkg->GetObject("vh_NoSys", tbackground_7);
    inputFile_bkg->GetObject("wjets_NoSys", tbackground_8);
    inputFile_bkg->GetObject("zjets_NoSys", tbackground_9);
    
    loader_1.AddSignalTree(tsignal_1, 1.0);
    loader_1.AddBackgroundTree(tbackground_1, 1.0);
    loader_1.AddBackgroundTree(tbackground_2, 1.0);
    loader_1.AddBackgroundTree(tbackground_3, 1.0);
    loader_1.AddBackgroundTree(tbackground_4, 1.0);
    loader_1.AddBackgroundTree(tbackground_5, 1.0);
    loader_1.AddBackgroundTree(tbackground_6, 1.0);
    loader_1.AddBackgroundTree(tbackground_7, 1.0);
    loader_1.AddBackgroundTree(tbackground_8, 1.0);
    loader_1.AddBackgroundTree(tbackground_9, 1.0);
    
    loader_2.AddSignalTree(tsignal_2, 1.0);
    loader_2.AddBackgroundTree(tbackground_1, 1.0);
    loader_2.AddBackgroundTree(tbackground_2, 1.0);
    loader_2.AddBackgroundTree(tbackground_3, 1.0);
    loader_2.AddBackgroundTree(tbackground_4, 1.0);
    loader_2.AddBackgroundTree(tbackground_5, 1.0);
    loader_2.AddBackgroundTree(tbackground_6, 1.0);
    loader_2.AddBackgroundTree(tbackground_7, 1.0);
    loader_2.AddBackgroundTree(tbackground_8, 1.0);
    loader_2.AddBackgroundTree(tbackground_9, 1.0);
    
    loader_3.AddSignalTree(tsignal_3, 1.0);
    loader_3.AddBackgroundTree(tbackground_1, 1.0);
    loader_3.AddBackgroundTree(tbackground_2, 1.0);
    loader_3.AddBackgroundTree(tbackground_3, 1.0);
    loader_3.AddBackgroundTree(tbackground_4, 1.0);
    loader_3.AddBackgroundTree(tbackground_5, 1.0);
    loader_3.AddBackgroundTree(tbackground_6, 1.0);
    loader_3.AddBackgroundTree(tbackground_7, 1.0);
    loader_3.AddBackgroundTree(tbackground_8, 1.0);
    loader_3.AddBackgroundTree(tbackground_9, 1.0);
    
     // Apply preselection cuts on the signal and background samples
    TCut mycuts = "met>200 && nJet30>=1 && nLep_base==1 && nLep_signal==1 && mt>50"; 
    TCut mycutb = "met>200 && nJet30>=1 && nLep_base==1 && nLep_signal==1 && mt>50"; 
    
    // Tell the dataloader how to use the training and testing events
    loader_1.PrepareTrainingAndTestTree(mycuts, mycutb, "NTrain_Signal=0:NTrain_Background=0:NTest_Signal=0:NTest_Background=0");
    loader_2.PrepareTrainingAndTestTree(mycuts, mycutb, "NTrain_Signal=0:NTrain_Background=0:NTest_Signal=0:NTest_Background=0");
    loader_3.PrepareTrainingAndTestTree(mycuts, mycutb, "NTrain_Signal=0:NTrain_Background=0:NTest_Signal=0:NTest_Background=0");
    
    // Adaptive Boost
    factory_1.BookMethod( &loader_1, TMVA::Types::kBDT, "BDT","NTrees=200:BoostType=AdaBoost");
    factory_2.BookMethod( &loader_2, TMVA::Types::kBDT, "BDT","NTrees=200:BoostType=AdaBoost");
    factory_3.BookMethod( &loader_3, TMVA::Types::kBDT, "BDT","NTrees=200:BoostType=AdaBoost");
    
    // Tell the factory to train, test, and evaluate the MVAs
    // Train MVAs using the set of training events
    factory_1.TrainAllMethods();
    factory_2.TrainAllMethods();
    factory_3.TrainAllMethods();
    
    // Evaluate all MVAs using the set of test events
    factory_1.TestAllMethods();
    factory_2.TestAllMethods();
    factory_3.TestAllMethods();
    
    // Evaluate and compare performance of all configured MVAs
    factory_1.EvaluateAllMethods();
    factory_2.EvaluateAllMethods();
    factory_3.EvaluateAllMethods();
    
    //plot ROC curve
    auto c_1 = factory_1.GetROCCurve(&loader_1);
    c_1->Draw("AL");
    auto c_2 = factory_2.GetROCCurve(&loader_2);
    c_2->Draw("AL");
    auto c_3 = factory_3.GetROCCurve(&loader_3);
    c_3->Draw("AL");
    
    // Save the output
    outputFile_1->Close();
    outputFile_1->Close();
    outputFile_1->Close();
} 

if (run == '2')
{
    auto inputFile_signal = TFile::Open("signal_Demo.root");
    auto inputFile_bkg = TFile::Open("bkg_Demo.root");
    
    auto outputFile = TFile::Open( "TMVAOutput_Demo.root", "RECREATE" );

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
    
    TTree* tsignal;
    TTree* tbackground;
    
    inputFile_signal->GetObject("C1N2_WZ_300_0_NoSys", tsignal);
    inputFile_bkg->GetObject("tth_NoSys", tbackground);
    loader.AddSignalTree(tsignal, 1.0);
    loader.AddBackgroundTree(tbackground, 1.0);
    
    TCut mycuts = "met>200 && nJet30>=1 && nLep_base==1 && nLep_signal==1 && mt>50";
    TCut mycutb = "met>200 && nJet30>=1 && nLep_base==1 && nLep_signal==1 && mt>50";
    
    loader.PrepareTrainingAndTestTree(mycuts, mycutb, "NTrain_Signal=0:NTrain_Background=0:NTest_Signal=0:NTest_Background=0");
    
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
    auto c2 = factory.GetROCCurve(&loader);
    c2->Draw("AL");
    
    // Save the output
    outputFile->Close();
}

}
