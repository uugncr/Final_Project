#include <TCanvas.h>
#include <TH2F.h>
#include <TColor.h> // Renk paleti için eklenen kütüphane
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <filesystem> // C++17 ile gelen dosya sistemi kütüphanesi

namespace fs = std::filesystem;

void one() {
    // Histogramı oluştur
    TH2F *hist = new TH2F("hist", "tail_integral vs fom HT2F 2D Histogram;tail_integral;fom", 600, 0, 60000, 600, 0.55, 0.90);

    // Final_Project dizinindeki tüm CSV dosyalarını bul
    std::vector<std::string> file_paths;
    std::string base_dir = "../"; // Final_Project dizinine göre ayarla
    for (const auto& entry : fs::recursive_directory_iterator(base_dir)) {
        if (entry.path().extension() == ".csv") {
            file_paths.push_back(entry.path().string());
        }
    }

    // Dosyaları okuyup histograma doldur
    for (const auto& file_path : file_paths) {
        std::ifstream file(file_path);
        if (!file.is_open()) {
            std::cerr << "Dosya açılamadı: " << file_path << std::endl;
            continue;
        }

        std::string line;
        // İlk satırı atla (eğer başlık varsa)
        std::getline(file, line);
        
        while (std::getline(file, line)) {
            std::stringstream ss(line);
            std::string cell;
            float tail_integral, fom;
            
            // N ve fom değerlerini oku (CSV formatına bağlı olarak değişebilir)
            std::getline(ss, cell, ',');// t0
            std::getline(ss, cell, ',');// t1
            std::getline(ss, cell, ',');// t2
            std::getline(ss, cell, ',');// t3
            std::getline(ss, cell, ',');// t4
            std::getline(ss, cell, ',');// s_r
            std::getline(ss, cell, ',');// s_f
            std::getline(ss, cell, ',');// N değeri
            std::getline(ss, cell, ',');//d_r
            std::getline(ss, cell, ',');// d_f
            std::getline(ss, cell, ',');//total_integral
            std::getline(ss, cell, ',');// tail_integral degeri
            tail_integral = std::stof(cell);
            std::getline(ss, cell, ','); // fom değeri
            fom = std::stof(cell);
            
            hist->Fill(tail_integral, fom);
        }
        file.close();
    }

    // Renk paleti oluştur
    const Int_t NRGBs = 3;
    const Int_t NCont = 10;
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


