import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_paths = [
    '/Users/uuu/Final_Project/parameters25.csv',
    '/Users/uuu/Final_Project/parameters50.csv',
    '/Users/uuu/Final_Project/parameters100.csv',
]

# Dosyaları okuyup birleştir
dfs = [pd.read_csv(file_path) for file_path in file_paths]
combined_df = pd.concat([df[['N', 'fom']] for df in dfs], ignore_index=True)

# Verileri tanımla
x = combined_df['N']
y = combined_df['fom']

# HT2F 2D histogram grafiğini oluştur
plt.figure(figsize=(10, 6))
plt.hexbin(x, y, gridsize=50, cmap='viridis', mincnt=1)
plt.colorbar(label='Frekans')
plt.xlabel('N')
plt.ylabel('fom')
plt.title('N vs fom HT2F 2D Histogram')
plt.show()


