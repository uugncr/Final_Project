import numpy as np
import matplotlib.pyplot as plt

def gauss(t, t0, s_r):
    expo = np.exp(-(t - t0)**2 / (2 * (s_r ** 2)))
    return expo

def expo(t, s_f):
    mix = np.exp(- (t/2) * (1 / s_f ** 2))
    return mix


def combined_function(tr, t0, tf):
    t = np.linspace(tr, tf, 1024)
    t_gauss = t[np.logical_and(t >= tr, t <= t0)]
    t_f = t[np.logical_and(t >= t0, t <= tf)]
    
    gauss_values = gauss(t_gauss, t0, 50)
    f_values = expo(t_f, 50)
    
    return np.concatenate((gauss_values, f_values))

tr = 0  # Başlangıç zamanı
t0 = np.random.uniform(0, 1024) # Gauss fonksiyonunun merkezi
tf = 1024 # Bitiş zamanı

x = np.linspace(tr, tf, 1024)
y = combined_function(tr, t0, tf)

plt.plot(x, y)
plt.xlabel('t')
plt.ylabel('Değer')

plt.title('Kombine Fonksiyon')
plt.grid(True)
plt.show()