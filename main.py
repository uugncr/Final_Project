import numpy as np
import matplotlib.pyplot as plt

def gauss(t, t0, sigma_r):
    A = 1
    exp = np.exp(-1/2 * ((t - t0)/sigma_r)**2)
    return A * exp

def mix(t, lamda):
    A = 1
    lamda = 00.1
    exp = np.exp(-lamda * t)
    return A * exp

tr = 0
t0 = 50
tf = 200

def fonksiyon_ara(t, tr, t0, tf, sigma_r, sigma_f):

    if tr <= t <= t0:
        return gauss(t, t0, sigma_r)
    elif t0 < t <= tf :
        return mix(t, sigma_f)
    else:
        return None
    
sigma_r = 100
sigma_f = 600

x_degerleri = []
y_degerleri = []

for t in np.linspace(tr, tf,):
    sonuc = fonksiyon_ara(t, tr, t0, tf, sigma_r, sigma_f)
    if sonuc is not None:
        x_degerleri.append(t)
        y_degerleri.append(sonuc)

plt.plot(x_degerleri, y_degerleri)
plt.xlabel("t")
plt.ylabel("Sonuç")
plt.title("Grafik")
plt.show()
