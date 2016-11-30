void trigeff(){

    TStyle *tdrStyle = new TStyle("tdrStyle","Style for P-TDR");

    // For the canvas:
    tdrStyle->SetCanvasBorderMode(0);
    tdrStyle->SetCanvasColor(kWhite);
    tdrStyle->SetCanvasDefH(600); //Height of canvas
    tdrStyle->SetCanvasDefW(600); //Width of canvas
    tdrStyle->SetCanvasDefX(0);   //POsition on screen
    tdrStyle->SetCanvasDefY(0);

    // For the Pad:
    tdrStyle->SetPadBorderMode(0);
    tdrStyle->SetPadColor(kWhite);
    tdrStyle->SetPadGridX(true);
    tdrStyle->SetPadGridY(true);
    tdrStyle->SetGridColor(0);
    tdrStyle->SetGridStyle(3);
    tdrStyle->SetGridWidth(1);

    // For the frame:
    tdrStyle->SetFrameBorderMode(0);
    tdrStyle->SetFrameBorderSize(1);
    tdrStyle->SetFrameFillColor(0);
    tdrStyle->SetFrameFillStyle(0);
    tdrStyle->SetFrameLineColor(1);
    tdrStyle->SetFrameLineStyle(1);
    tdrStyle->SetFrameLineWidth(1);

    // For the histo:
    tdrStyle->SetHistLineColor(1);
    tdrStyle->SetHistLineStyle(0);
    tdrStyle->SetHistLineWidth(1);

    tdrStyle->SetEndErrorSize(2);
    tdrStyle->SetErrorX(0.);

    tdrStyle->SetMarkerStyle(20);

    //For the fit/function:
    tdrStyle->SetOptFit(1);
    tdrStyle->SetFitFormat("5.4g");
    tdrStyle->SetFuncColor(2);
    tdrStyle->SetFuncStyle(1);
    tdrStyle->SetFuncWidth(1);

    //For the date:
    tdrStyle->SetOptDate(0);

    // For the statistics box:
    tdrStyle->SetOptFile(0);
    tdrStyle->SetOptStat("emr"); // To display the mean and RMS:   SetOptStat("mr");
    tdrStyle->SetStatColor(kWhite);
    tdrStyle->SetStatFont(42);
    tdrStyle->SetStatFontSize(0.025);
    tdrStyle->SetStatTextColor(1);
    tdrStyle->SetStatFormat("6.4g");
    tdrStyle->SetStatBorderSize(1);
    tdrStyle->SetStatH(0.1);
    tdrStyle->SetStatW(0.15);

    // Margins:
    tdrStyle->SetPadTopMargin(0.07);
    tdrStyle->SetPadBottomMargin(0.13);
    tdrStyle->SetPadLeftMargin(0.13);
    tdrStyle->SetPadRightMargin(0.05);

    // For the Global title:
    tdrStyle->SetTitleFont(35);
    tdrStyle->SetTitleColor(1);
    tdrStyle->SetTitleTextColor(1);
    tdrStyle->SetTitleFillColor(10);
    tdrStyle->SetTitleFontSize(0.045);
    tdrStyle->SetTitleX(0.15); // Set the position of the title box
    tdrStyle->SetTitleBorderSize(0);

    // For the axis titles:
    tdrStyle->SetTitleColor(1, "XYZ");
    tdrStyle->SetTitleFont(42, "XYZ");
    tdrStyle->SetTitleSize(0.04, "XYZ");
    tdrStyle->SetTitleXOffset(0.9);
    tdrStyle->SetTitleYOffset(1.05);

    // For the axis labels:
    tdrStyle->SetLabelColor(1, "XYZ");
    tdrStyle->SetLabelFont(42, "XYZ");
    tdrStyle->SetLabelOffset(0.007, "XYZ");
    tdrStyle->SetLabelSize(0.03, "XYZ");

    // For the axis:
    tdrStyle->SetAxisColor(1, "XYZ");
    tdrStyle->SetStripDecimals(kTRUE);
    tdrStyle->SetTickLength(0.03, "XYZ");
    tdrStyle->SetNdivisions(510, "XYZ");
    tdrStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
    tdrStyle->SetPadTickY(1);

    // Change for log plots:
    tdrStyle->SetOptLogx(0);
    tdrStyle->SetOptLogy(0);
    tdrStyle->SetOptLogz(0);

    // Postscript options:
    tdrStyle->SetPaperSize(20.,20.);
    tdrStyle->SetPalette(1);

    gROOT -> ForceStyle();

    tdrStyle->cd();





    //###############################//

    TString directory = "/afs/cern.ch/work/z/zdemirag/public/ichep/setup80x/Skim_v12/";

    TFile *f = new TFile("/afs/cern.ch/work/z/zdemirag/work/ichep/MonoX/monojet/slimmer/new_hvbf125.root","READ");
    double ptbins[17] = {50,60,70,80,90,100,125,150,175,200,250,300,350,400,500,600,1000};

    TH1F *den_mc_met = new TH1F("den_mc_met","den_mc_met",16,ptbins);
    TH1F *num_mc_met = new TH1F("num_mc_met","num_mc_met",16,ptbins);

    eff_mc_met= new TGraphAsymmErrors;
    den_mc_met->Sumw2();
    num_mc_met->Sumw2();

    //TString name = "met";
    TString name = "trueMet";
    //TString name = "mjj";
    //TString name = "abs(jjDEta)";
    
    //TString offline = "trueMet>300 && jot1Eta*jot2Eta < 0 && jot1Pt>80. && jot2Pt > 70. && abs(jot1Eta)<4.7 && abs(jot2Eta)<4.7 && n_looselep == 1 && abs(lep1PdgId)==11 && trueMet>50. && mt<160. && abs(minJetMetDPhi)>0.5 && n_tightlep > 0 ";
    //TString offline = "mjj>500 && abs(jjDEta)>3.0 && jot1Eta*jot2Eta < 0 && jot1Pt>80. && jot2Pt > 70. && abs(jot1Eta)<4.7 && abs(jot2Eta)>3.0 && abs(jot2Eta)<4.7 && n_looselep == 1 && abs(lep1PdgId)==11 && trueMet>50. && mt<160. && abs(minJetMetDPhi)>0.5 && n_tightlep > 0 ";

    TString offline = "jot1Eta*jot2Eta < 0 && jot1Pt>80. && jot2Pt > 70. && abs(jot1Eta)<4.7 && abs(jot2Eta)<4.7 && n_looselep == 1 && abs(lep1PdgId)==11 && trueMet>50. && mt<160. && abs(minJetMetDPhi)>0.5 && n_tightlep > 0 ";

    TString offline_new = "jot1Eta*jot2Eta < 0 && jot1Pt>80. && jot2Pt > 70. && abs(jot1Eta)<4.7 && abs(jot2Eta)<4.7 && n_looselep == 0 && abs(minJetMetDPhi)>0.5";

    TString cut_den_new = offline_new;
    TString cut_num_new = offline_new + " && triggerFired[21]";
    //TString cut_num_new = offline_new ;
    //TString cut_num_new = "(triggerFired[11] || triggerFired[12] || triggerFired[13] || triggerFired[14] || triggerFired[15] || triggerFired[16] || triggerFired[17] || triggerFired[18]) && "+offline_new;

    TString cut_den = "(triggerFired[0] || triggerFired[1] || triggerFired[2] || triggerFired[3] ) && "+offline;
    TString cut_num = "(triggerFired[0] || triggerFired[1] || triggerFired[2] || triggerFired[3] ) && (triggerFired[9] || triggerFired[10] || triggerFired[11] || triggerFired[12] || triggerFired[13] || triggerFired[14]) && "+offline;
    
    events->Draw(name+">>den_mc_met",cut_den_new,"");
    events->Draw(name+">>num_mc_met",cut_num_new,"");

    eff_mc_met->BayesDivide(num_mc_met,den_mc_met,"");    
    eff_mc_met->Draw("ap");
    std::cout << "drawing" << std::endl;
    eff_mc_met->GetYaxis()->SetTitle("Efficiency");
    eff_mc_met->GetXaxis()->SetTitle("Offline PF MET [GeV]");
    eff_mc_met->GetYaxis()->SetRangeUser(0.0,1.19);

    /*
    TF1 *f1 = new TF1("f1","1",0,1000);
    f1->SetLineColor(4);
    f1->SetLineStyle(2);
    f1->SetLineWidth(2);
    //f1->Draw("same");

    //TF1 *erf1 = new TF1("erf1", "0.5*[2]*(1+TMath::Erf( (x-[0]) / ([1]*sqrt(2)) ) )",0.0,1000.0);
    TF1 *erf1 = new TF1("erf1", ErfCB,0.0,1000.0,5);
    erf1->SetParameter(0,100);
    erf1->SetParameter(1,2);
    erf1->SetParameter(2,0.5);
    erf1->SetParameter(3,3);
    erf1->SetParameter(4,0.9);
    //erf1->SetParLimits(2,0.0,1.0);
    erf1->SetLineColor(2);
    erf1->SetLineWidth(2);
    //eff_mc_met->Fit("erf1","RMB");

    //TFile *f2 = new TFile(directory_data+"monojet_SingleMuon+Run2015D.root","READ");
    TFile *f2 = new TFile(directory+"/monojet_SingleElectron.root","READ");

    TH1F *den_data_met = new TH1F("den_data_met","den_data_met",16,ptbins);
    TH1F *num_data_met = new TH1F("num_data_met","num_data_met",16,ptbins);
    eff_data_met= new TGraphAsymmErrors;
    den_data_met->Sumw2();
    num_data_met->Sumw2();

    events->Draw(name+">>den_data_met",cut_den,"");
    events->Draw(name+">>num_data_met",cut_num,"");

    eff_data_met->BayesDivide(num_data_met,den_data_met,"");
    eff_data_met->SetLineColor(4);
    //eff_data_met->Draw("apsame");
    eff_data_met->GetYaxis()->SetTitle("Efficiency");
    eff_data_met->GetXaxis()->SetTitle("Offline PF MET [GeV]");
    eff_data_met->GetYaxis()->SetRangeUser(0.0,1.19);

    erf1->SetLineColor(4);
    erf1->SetLineWidth(2);
    //eff_data_met->Fit("erf1","RMBsame");

    TLatex *latex1 = new TLatex;
    latex1->SetNDC();
    latex1->SetTextSize(0.025);
    latex1->SetTextAlign(31);

    

    */
}

Double_t ErfCB(double *x, double *par)
{ 
    double m = x[0];
    double m0 = par[0];
    double sigma = par[1];
    double alpha = par[2];
    double n = par[3];
    double norm = par[4];
  
    const double sqrtPiOver2 = 1.2533141373; // sqrt(pi/2)
    const double sqrt2 = 1.4142135624;

    Double_t sig = fabs((Double_t) sigma);
    Double_t t = (m - m0)/sig ;
  
    if (alpha < 0)
        t = -t;

    Double_t absAlpha = fabs(alpha / sig);
    Double_t a = TMath::Power(n/absAlpha,n)*exp(-0.5*absAlpha*absAlpha);
    Double_t b = absAlpha - n/absAlpha;

    Double_t leftArea = (1 + ApproxErf( absAlpha / sqrt2 )) * sqrtPiOver2 ;
    Double_t rightArea = ( a * 1/TMath::Power(absAlpha - b,n-1)) / (n - 1);
    Double_t area = leftArea + rightArea ;

    if ( t <= absAlpha ){
        return norm * (1 + ApproxErf( t / sqrt2 )) * sqrtPiOver2 / area ;
    }
    else{
        return norm * (leftArea +  a * (1/TMath::Power(t-b,n-1) - 1/TMath::Power(absAlpha - b,n-1)) / (1 - n)) / area ;
    }
  
} 

Double_t ApproxErf(Double_t arg)
{
    static const double erflim = 5.0;
    if( arg > erflim )
        return 1.0;
    if( arg < -erflim )
        return -1.0;
  
    return TMath::Erf(arg);
}
    
    
    
