import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde

# Dosya yolları
file_paths = [
    '/Users/uuu/Final_Project/parameters25.csv',
    '/Users/uuu/Final_Project/parameters50.csv',
    '/Users/uuu/Final_Project/parameters100.csv']

# Veri setlerini okuma
dataframes = [pd.read_csv(file_path) for file_path in file_paths]

# Geniş bir figür oluşturma
plt.figure(figsize=(16, 8))

# Yoğunluk grafiğini sol tarafta gösterme
plt.subplot(121)
"""
for i, df in enumerate(dataframes):
    sns.kdeplot(data=df, x="tail_integral", y="fom", cmap="viridis", fill=True, alpha=0.5, label=f'File {i+1}')

plt.title('Density Plot for tail_integral vs fom')
plt.xlabel('tail_integral')
plt.ylabel('fom')
"""
# Dağılım grafiğini sağ tarafta gösterme
plt.subplot(122)

# Combining the ratios and tail_integral values for density calculation
ratios = np.concatenate([df['total_integral'] / df['tail_integral'] for df in dataframes])
tail_integrals = np.concatenate([df['tail_integral'] for df in dataframes])

# Calculate the point density
xy = np.vstack([tail_integrals, ratios])
z = gaussian_kde(xy)(xy)

# Sort the points by density, so that the densest points are plotted last
idx = z.argsort()
x, y, z = tail_integrals[idx], ratios[idx], z[idx]

plt.scatter(x, y, c=z, s=50, edgecolor='', cmap='viridis')
plt.colorbar(label='Density')

plt.title('Tail Integral vs Ratio of Total to Tail Integral with Density Coloring')
plt.xlabel('Tail Integral')
plt.ylabel('Total Integral / Tail Integral')

plt.tight_layout()
plt.show()

