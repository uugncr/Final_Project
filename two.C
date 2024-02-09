#include <TCanvas.h>
#include <TH2F.h>
#include <fstream>
#include <sstream>
#include <string>

void two() {
    // Histogramı oluştur
    TH2F *hist = new TH2F("hist", "total_integral vs tail_integral HT2F 2D Histogram;total_integral;tail_integral", 5000, 0, 50000, 6000, 0, 60000);

    // Dosya yolları
    const char* file_paths[] = {
        "/Users/uuu/Final_Project/parameters25.csv",
        "/Users/uuu/Final_Project/parameters50.csv",
        "/Users/uuu/Final_Project/parameters100.csv"
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
            float total_integral, tail_integral;
            
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
            total_integral = std::stof(cell);
            std::getline(ss, cell, ',');// tail_integral degeri
            tail_integral = std::stof(cell);
            std::getline(ss, cell, ','); // fom değeri
            
            hist->Fill(total_integral, tail_integral);
        }
        file.close();
    }

    // Çizimi yap
    TCanvas *canvas = new TCanvas("canvas", "Canvas", 800, 600);
    hist->Draw("COLZ");
}



