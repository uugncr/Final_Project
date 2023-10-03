import numpy as np
import matplotlib.pyplot as plt

# Fonksiyonlar
def gauss(t, t0, s_r):
    expo = np.exp(-(t - t0)**2 / (2 * (s_r ** 2)))
    return expo

def expo(t, t0, tf, s_f):
    exp = np.exp(-((t - t0) / s_f))
    mask = (t >= t0) & (t <= tf)
    return exp * mask

# Parametreler
tr = 0  # Başlangıç zamanı
t0 = 2  # Gauss fonksiyonunun merkezi
tf = 5  # Bitiş zamanı
s_r = 1  # Gauss fonksiyonunun standart sapması
s_f = 0.5  # Expo fonksiyonunun hız parametresi

# Zaman aralığı ve adım sayısı
t = np.linspace(tr, tf, num=100)
# Fonksiyonları hesapla
gauss_values = gauss(t, t0, s_r)
expo_values = expo(t, t0, tf, s_f)

# Cizdirme
plt.plot(t, gauss_values, label='Gauss')
plt.plot(t, expo_values, label='Expo')
plt.axvline(x=t0, color='r', linestyle='--', label='t0')
plt.axvline(x=tf, color='g', linestyle='--', label='tf')
plt.legend()
plt.xlabel('t')
plt.ylabel('Değer')
plt.title('Gauss ve Expo Fonksiyonları')
plt.show()

# Gauss fonksiyonu tamamlama süresi
gauss_completion_time = t0 - tr
# Expo fonksiyonu tamamlama süresi
expo_completion_time = tf - t0

print('Gauss fonksiyonu', gauss_completion_time, 'saniyede tamamlandı.')
print('Expo fonksiyonu', expo_completion_time, 'saniyede tamamlandı.')
