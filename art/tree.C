#include <TCanvas.h>
#include <TH2F.h>
#include <TColor.h> // Renk paleti için eklenen kütüphane
#include <fstream>
#include <sstream>
#include <string>

void tree() {
    // Histogramı oluştur
    TH2F *hist = new TH2F("hist", "N vs fom HT2F 2D Histogram;N;fom", 100, 0, 600, 100, 0.5, 1);

    // Dosya yolları
    const char* file_paths[] = {
        "/Users/uuu/Final_Project/par25.csv",
        "/Users/uuu/Final_Project/par50.csv",
        "/Users/uuu/Final_Project/par100.csv"
    };
    

    // Dosyaları okuyup histograma doldur
    for (auto &file_path : file_paths) {
        std::ifstream file(file_path);
        std::string line;
        
        // İlk satırı atla (eğer başlık varsa)
        std::getline(file, line);
        
        while (std::getline(file, line)) {
            std::stringstream ss(line);
            std::string cell;
            float N, fom;
            
            // N ve fom değerlerini oku (CSV formatına bağlı olarak değişebilir)
            std::getline(ss, cell, ',');// İlk sütunları atla veya okuma
            
            // ... Sütun atlamak için daha fazla std::getline(ss, cell, ',') kullanılabilir
            std::getline(ss, cell, ',');
            std::getline(ss, cell, ',');
            std::getline(ss, cell, ',');
            std::getline(ss, cell, ',');
            std::getline(ss, cell, ',');
            std::getline(ss, cell, ',');
            std::getline(ss, cell, ',');// N değeri
            N = std::stof(cell);
            std::getline(ss, cell, ',');
            std::getline(ss, cell, ',');
            std::getline(ss, cell, ',');
            std::getline(ss, cell, ',');
            std::getline(ss, cell, ','); // fom değeri
            fom = std::stof(cell);
            
            hist->Fill(N, fom);
        }
        file.close();
    }
    
    // Renk paleti oluştur
    const Int_t NRGBs = 3;
    const Int_t NCont = 255;
    Double_t stops[NRGBs] = { 0.00, 0.50, 1.00 };
    Double_t red[NRGBs]   = { 0.00, 1.00, 1.00 };
    Double_t green[NRGBs] = { 0.00, 1.00, 0.00 };
    Double_t blue[NRGBs]  = { 1.00, 1.00, 0.00 };
    TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
    gStyle->SetNumberContours(NCont);


    // Çizimi yap
    TCanvas *canvas = new TCanvas("canvas", "Canvas", 800, 600);
    hist->Draw("COLZ");
}

