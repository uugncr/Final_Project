import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def gaussian(x, x0, std_dev,λ):
    if x <x0:
        exp = np.exp(-((x - x0) ** 2) / (2 * std_dev ** 2))
        #coefficient = 1 / (std_dev * np.sqrt(2 * np.pi))
    else:
        exp = np.exp(λ * x)

    return exp


def V(x0, std_dev):
    result, _ = quad(lambda x: (x - x0) ** 2 * gaussian(x, x0, std_dev), -np.inf, np.inf)
    return result

def calculate_x0(std_dev):
    integrand = lambda x: x * gaussian(x, 0, std_dev)
    result, _ = quad(integrand, -np.inf, np.inf)
    return result


x0 = 500
std_dev = 100


x = np.linspace(0, 1024, 20)  # x değerleri: 1024 kanal 20 ns 
y = gaussian(x, x0, std_dev,)  # x değerlerine karşılık gelen yoğunluk değerlerini hesaplar


plt.plot(x, y)
plt.title('Gauss')
plt.xlabel('t')
plt.ylabel('V')
plt.grid(True)
plt.show()
