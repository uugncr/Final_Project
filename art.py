import matplotlib.pyplot as plt
import pandas as pd



file_paths = [
    '/Users/uuu/Final_Project/parameters25_50000.csv',
    '/Users/uuu/Final_Project/parameters50_50000.csv',
    '/Users/uuu/Final_Project/parameters100_50000.csv',
]

# Dosyaları yükleyip birleştirin
data_frames = [pd.read_csv(file_path) for file_path in file_paths]
combined_data = pd.concat(data_frames)

# İkinci pencerede verilerin yoğunlaştığı alanları gösteren grafik
plt.figure(figsize=(12, 8))
plt.hist2d(combined_data['N'], combined_data['fom'], bins=50, cmap='Reds')
plt.colorbar(label='Yoğunluk')
plt.title("Verilerin Yoğunlaştığı Alanlar")
plt.xlabel("N")
plt.ylabel("FOM")
plt.grid(True)
plt.show()
