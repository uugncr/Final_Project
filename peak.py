import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def f(t, t0, s_r, s_f):
    N = 20
    if t < t0:
        expo = N * np.exp(-(t - t0)**2 / (2 * (s_r ** 2)))
        return expo
    else:
        mix = N * np.exp(- (t - t0)**2 /s_f **2 )
        return mix


t = np.linspace(0, 1024,1024)
#t0 = np.random.uniform(0,1023)
#print(t0)
t0 = 512
s_r = 6
s_f = 25

y = np.array([f(i, t0, s_r, s_f) for i in t])
#print(y)
np.savetxt('gaussian.csv', y, delimiter=',')

cs = CubicSpline(t,y)
t_interp = np.linspace(0, 1024, 10000) 
y_interp = cs(t_interp)

desired_value = 2
tolerance = 1e-1

for i in range(len(y_interp) - 1):
    if abs(y_interp[i] - desired_value) <= tolerance and abs(y_interp[i + 1] - desired_value) <= tolerance:
        print(f"Fonksiyon 2 olduğu nokta: x={t_interp[i]}, y={y_interp[i]}") 




plt.plot(t, y, marker = '.')
plt.xlabel('t')
plt.ylabel('V')

plt.show()

