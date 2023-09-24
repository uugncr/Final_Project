import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def profile(f, f0, gamma, offset):  #frekansa bagli bir egriyi gosteren Loorentz fonksiyonu
    return 1 / ((f - f0) / gamma)**2 * offset # merkezi = f0, genisligi = gamma, 0'dan yuksekligi = offset

N = 500
f = np.linspace(-10, 10, N) #fonksiyon araligim
y = profile(f, 1, 0.5, 0.5) #degerler

y_data = y * np.random.uniform(0.3, 0.3, N) #"y" mukkemmel data'nin ustune random gurultu ekledik.

popt, pcov = curve_fit(profile, f, y_data, p0 = [0.5 ,1, -0.1 ]) #1. degerim fonksiyon, 2. degerim aralik, 3. ddegerim fit ederken baslangic sartlarini vererek islemi hizlandirmak 
#print(popt) # popt ise ooptimizasyonun sonucunda profilin parametlerini verir 

plt.figure(figsize = (10,8))
plt.plot(f, y_data, 'k-')
plt.plot(f, profile(f, *popt), '-r')
plt.plot(f, profile(f, 1, 0.5, 0.5), '-b')

plt.plot(f, y_data, '.')
plt.show()
