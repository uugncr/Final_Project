import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gauss(t, A, t0, sigma):
    exp = np.exp(-0.5 * ((t - t0) ** 2 / sigma ** 2))
    return A * exp

def expo(t, A, lamda):
    exp = np.exp(-lamda * t)
    return A * exp


N = 100
M =3 * N
t = np.linspace(0, 50, N)  
t1 = np.linspace(50, 200, M)

y = gauss(t, 100, 80, 50) 
y_data = y + np.random.uniform(0, 50, N)
popt, pcov = curve_fit(gauss, t, y_data) 
#print(popt)

y1 = expo(t1, 1,100)
y1_data = y1 + np.random.uniform(50, 200, M)
popt, pcov = curve_fit(expo, t1, y1_data) 
#print(popt)

plt.plot(t, y, '-b')
plt.plot(t1, y1, '-r')

plt.plot(t, y_data, '.')
plt.plot(t1, y1_data, '*')
plt.show()
