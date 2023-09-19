import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import quad

def gaussian(x, x0, std_dev):
    exp = np.exp(-((x - x0) ** 2) / (2 * std_dev ** 2))
    #coefficient = 1 / (std_dev * np.sqrt(2 * np.pi))
    return exp

def calculate_x0(std_dev):
    integrand = lambda x: x * gaussian(x, 0, std_dev)
    result, _ = quad(integrand, -np.inf, np.inf)
    return result


x = np.linspace(0, 1024)
std_dev = 200
x0 = calculate_x0(std_dev)
y = [gaussian(x_val, x0, std_dev) for x_val in x]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gaussian function')
plt.grid(True)
plt.show()
