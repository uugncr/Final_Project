import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, x0, std_dev):
    exp = np.exp(-((x - x0) ** 2) / (2 * std_dev ** 2))
    coefficient = 1 / (std_dev * np.sqrt(2 * np.pi))
    return coefficient * exp


x0 = 3
std_dev = 100









x = np.linspace(0, 1024, 20)  # x değerleri: 1024 kanal 20 ns 
y = gaussian(x, x0, std_dev)  # x değerlerine karşılık gelen yoğunluk değerlerini hesaplar


plt.plot(x, y)
plt.title('Gauss')
plt.xlabel('t')
plt.ylabel('V')
plt.grid(True)
plt.show()
