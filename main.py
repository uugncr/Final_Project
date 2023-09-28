import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gauss(t, A, t0, sigma):
    exp = np.exp(-0.5 * ((t - t0) ** 2 / sigma ** 2))
    return A * exp

def expo(t, A, lamda):
    exp = np.exp(-lamda * t)
    return 1 / A * exp


N = 100

t = np.linspace(0, 50, N)  
t1 = np.linspace(50, 200, N)

y = gauss(t, 100, 80, 50) 
y_data = y + np.random.uniform(0, 0.3)
popt, pcov = curve_fit(gauss, t, y_data) 
print(popt)

y1 = expo(t1, 100,100)
y1_data = y1 + np.random.uniform(0, 0.3)
#popt, pcov = curve_fit(expo, t1, y1_data) 
#print(popt)

plt.plot(t, y_data, '.')
plt.plot(t1, y1_data, '*')


plt.plot(t, gauss(t, 200, 160, 183), label='Gaussian')
plt.plot(t1, expo(t1, 200, 100), label='Exponential')
plt.plot(t1, y, label='Mixed')
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.show()
