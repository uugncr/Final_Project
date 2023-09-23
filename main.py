import numpy as np
import matplotlib.pyplot as plt

def gauss(t, t0, sigma_r):
    A = 1
    exp = np.exp(-1/2 * ((t - t0)/sigma_r)**2)
    return A * exp

def mix(t, sigma_f):
    A = 1
    exp = np.exp(-sigma_f * t)
    return A * exp

def fonksiyon_ara(t, tr, t0, tf, sigma_r, sigma_f):
    if tr <= t <= t0:
        return gauss(t, t0, sigma_r)
    elif t0 < t <= tf:
        return mix(t, sigma_f)
    else:
        return None

tr = 2
t0 = 5
tf = 8
sigma_r = 1
sigma_f = 0.5

# Grafik için x ve y değerlerini saklayacak listeler oluşturalım
x_degerleri = []
y_degerleri = []

# t değerlerini belirleyerek fonksiyon sonuçlarını hesaplayıp listelere ekleyelim
for t in np.linspace(0, 10, 1000):
    sonuc = fonksiyon_ara(t, tr, t0, tf, sigma_r, sigma_f)
    if sonuc is not None:
        x_degerleri.append(t)
        y_degerleri.append(sonuc)

# Grafik çizdirme
plt.plot(x_degerleri, y_degerleri)
plt.xlabel("t")
plt.ylabel("Sonuç")
plt.title("Grafik")
plt.show()