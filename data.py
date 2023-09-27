import numpy as np
import matplotlib.pyplot as plt

def gauss(t, t0, sigma):
    expo = np.exp(-np.power(t - t0 , 2) / (2 * np.power(sigma, 2)))
    return expo

def f(t):
    lamda = 100
    mix = np.exp(- lamda * t)
    return mix

t = np.arange(0, 200, 1)  # Corrected step size
t1 = np.arange(100, 200, 1)  # Corrected step size
gauss_values = gauss(t, 100, 10)  # Örnek değerler: t0=100, sigma=10
f_values = f(t1)

plt.plot(t, gauss_values, label='gauss')
plt.plot(t1, f_values, label='f')  # Use t1 instead of t
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.title('Gauss ve f Fonksiyonları')
plt.show()
