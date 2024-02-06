import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Dosya yolları

file_paths = [
    '/Users/uuu/Final_Project/parameters25.csv',
    '/Users/uuu/Final_Project/parameters50.csv',
    '/Users/uuu/Final_Project/parameters100.csv',
]

# Veri setlerini okuma
dataframes = [pd.read_csv(file_path) for file_path in file_paths]

# Yoğunluk grafiği için geniş bir figür oluşturma
plt.figure(figsize=(10, 8))

# Her veri seti için yoğunluk grafiği çizme ve mappable nesnesini tutma
cbar_ax = None
for i, df in enumerate(dataframes):
    ax = sns.kdeplot(data=df, x="total_integral", y="tail_integral", cmap="viridis", fill=True, alpha=0.5, label=f'File {i+1}')
    if cbar_ax is None:
        cbar_ax = ax

# Color bar eklemek için mappable nesnesini kullanma
plt.colorbar(cbar_ax.collections[0], ax=ax, label='Density')

plt.title('Combined Density Plots for All Files')
plt.xlabel('total_integral')
plt.ylabel('tail_integral')
plt.legend()
plt.show()

