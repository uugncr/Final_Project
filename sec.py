import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import quad

x = np.linspace(0, 1024, 20)

std_dev = 500
x0 = 500

def gaussian(x, x0, std_dev):
    exp = np.exp(-((x - x0) ** 2) / (2 * std_dev ** 2))
    return exp

def perf_gaus(x,x0,std_dev):
    exp = np.exp(-((x - x0) ** 2) / (2 * std_dev ** 2))
    coefficient = 1 / (std_dev * np.sqrt(2 * np.pi))
    return coefficient *exp


def calculate_x0(std_dev):
    integrand = lambda x: x * gaussian(x, 0, std_dev)
    result, _ = quad(integrand, -np.inf, np.inf)
    return result



#x0 = calculate_x0(std_dev)

x_less_x0 = x[np.where(x < x0)]
x_equal_x0 = x[np.where(np.isclose(x, x0))]
x_greater_x0 = x[np.where(x > x0)]


y_less_x0 = gaussian(x_less_x0, x0, std_dev)
y_equal_x0 = gaussian(x_equal_x0, x0, std_dev)
y_greater_x0 = gaussian(x_greater_x0, x0, std_dev)
y = perf_gaus(x, x0, std_dev) 

plt.plot(x_less_x0, y_less_x0, label='x < x0', color='blue')  # Mavi renk
plt.plot(x_equal_x0, y_equal_x0, label='x = x0', color='red')  # Kırmızı renk
plt.plot(x_greater_x0, y_greater_x0, label='x > x0', color='green')  # Yeşil renk
plt.plot(x, y, color='black')  # Siyah renk

plt.xlabel('x')
plt.ylabel('y')
plt.title('Mixed Gaussian Distribution')
plt.legend()
plt.grid(True)
plt.show()
