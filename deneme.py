import numpy as np
import matplotlib.pyplot as plt

def gauss(t, t0, sigma):
    expo = np.exp(-np.power(t - t0 , 2) / (2 * np.power(sigma, 2)))
    return expo

def f(t):
    lamda = 0.1
    mix = np.exp(- lamda * t)
    return mix

def combined_function():
    t = np.linspace(0, 200, 1000)  # 0 ile 200 arasında 1000 nokta oluştur
    t0 = np.random.randint(50, 150)  # 50 ile 150 arasında rastgele bir t0 değeri seç

    gauss_values = gauss(t, t0, 10)  # Gauss fonksiyonunu hesapla
    f_values = f(t[t > t0])  # t > t0 olan noktalarda f(t) fonksiyonunu hesapla

    return np.concatenate((gauss_values, f_values))  # Gauss ve f fonksiyonlarının birleşimini döndür

# Örnek kullanım
result = combined_function()
data = np.array(result)

mean = np.mean(data)
maximum = np.max(data)
minimum = np.min(data)

print(mean, maximum, minimum)

plt.plot(data, marker='.')
plt.show()
