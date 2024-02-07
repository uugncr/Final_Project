#include <TCanvas.h>
#include <TH2F.h>
#include <fstream>
#include <sstream>
#include <string>

void tree() {
    // Histogramı oluştur
    TH2F *hist = new TH2F("hist", "N vs fom HT2F 2D Histogram;N;fom", 100, 0, 600, 120000, 0.5, 1);

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

    // Çizimi yap
    TCanvas *canvas = new TCanvas("canvas", "Canvas", 800, 600);
    hist->Draw("COLZ");
}

