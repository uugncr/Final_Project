import matplotlib.pyplot as plt
import pandas as pd

file_paths = [
    '/Users/uuu/Final_Project/parameters25.csv',
    '/Users/uuu/Final_Project/parameters50.csv',
    '/Users/uuu/Final_Project/parameters100.csv',
]

# Dosyaları yükleyip birleştirin
data_frames = [pd.read_csv(file_path) for file_path in file_paths]
combined_data = pd.concat(data_frames)

# Grafik çizimi
plt.figure(figsize=(10, 6))  # Grafiğin boyutunu ayarla
sc = plt.scatter(combined_data['N'], combined_data['fom'], c=combined_data['momentum'], cmap='viridis')  # N, fom ve momentum sütunlarına göre saçılım grafiği oluştur

# Renk çubuğu ekle
plt.colorbar(sc, label='Momentum')

# X ve Y eksenlerinin sınırlarını ayarla
plt.xlim(0, 600)
plt.ylim(0.5, 1)

# Eksen başlıklarını ve grafiğin başlığını ekle
plt.xlabel('N')
plt.ylabel('FOM')
plt.title('Momentum ve Renk Skalası ile Görselleştirme')

# Grafiği göster
plt.show()

