import numpy as np
import matplotlib.pyplot as plt

def gauss(t, t0, sigma):
    expo = np.exp(-np.power(t - t0 , 2) / (2 * np.power(sigma, 2)))
    return expo


def f(t):
    lamda = 0.1
    mix = np.exp(- lamda * t)
    return mix
#####################################################################

def combined_function(tr, t0, tf):
    t = np.linspace(tr, tf, 100)
    t_gauss = t[np.logical_and(t >= tr, t <= t0)]  # tr ile t0 arasındaki değerler
    t_f = t[np.logical_and(t >= t0, t <= tf)]  # t0 ile tf arasındaki değerler
    
    gauss_values = gauss(t_gauss, t0, 1)  # Gauss fonksiyonunu tr ile t0 arasında hesapla
    f_values = f(t_f)  # f fonksiyonunu t0 ile tf arasında hesapla
    
    return np.concatenate((gauss_values, f_values))

# Örnek kullanım
tr = 0
t0 = 30
tf = 100
result = combined_function(tr, t0, tf)
print(result)
data = np.array(result)

plt.plot(data)
plt.show()


