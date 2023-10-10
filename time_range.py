import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy import integrate

#Fonksiyon 

def f(t, t0, s_r, s_f,N):
    if t < t0:
        expo = N * np.exp(-(t - t0)**2 / (2 * (s_r ** 2)))
        return expo
    else:
        mix = N * np.exp(- (t - t0)**2 /s_f **2 )
        return mix

t = np.linspace(0, 1024, 1024)
t0 = np.random.uniform(0, 1024)
N = 20
s_r = 6
s_f = 25

y = np.array([f(i, t0, s_r, s_f, N) for i in t])

np.savetxt('gaussian_2.csv', y, delimiter=',')

#Interplasyon 

t1, t2, t3, t4 = None, None, None, None

cs = CubicSpline(t, y)
t_interp = np.linspace(0, 1024, 100000)
y_interp = cs(t_interp)


desired_value = N * 0.1
tolerance = 1e-1

desired_value_1 = N * 0.1
for i in range(len(y_interp) - 1):
    if abs(y_interp[i] - desired_value_1) <= tolerance and abs(y_interp[i + 1] - desired_value_1) <= tolerance:
        t1 = t_interp[i]
        break

desired_value_2 = N * 0.9
for i in range(len(y_interp) - 1):
    if abs(y_interp[i] - desired_value_2) <= tolerance and abs(y_interp[i + 1] - desired_value_2) <= tolerance:
        t2 = t_interp[i]
        break


desired_value_3 = N * 0.9
for i in range(len(y_interp) - 1, 0, -1):
    if abs(y_interp[i] - desired_value_3) <= tolerance and abs(y_interp[i - 1] - desired_value_3) <= tolerance:
        t3 = t_interp[i]
        break


desired_value_4 = N * 0.1
for i in range(len(y_interp) - 1, 0, -1):
    if abs(y_interp[i] - desired_value_4) <= tolerance and abs(y_interp[i - 1] - desired_value_4) <= tolerance:
        t4 = t_interp[i]
        break

print(f"t1: {t1}\nt2: {t2}\nt0: {t0}\nt3: {t3}\nt4: {t4}")

#Integral 

integral3, error = integrate.quad(lambda x: cs(x), t0, t4)
integral4, error2 = integrate.quad(lambda x: cs(x), t1, t4)
print("integral_oranlari_cs:", integral3/integral4)


f_lambda = lambda x: f(x, t0, s_r, s_f, N)
integral, error = integrate.quad(f_lambda, t0, t4)
integral2, error2 = integrate.quad(f_lambda, t1, t4)
print("integral_t0_t4:",integral)
print("integral_t1_t4:",integral2)
print("integral_oranlari_duz:", integral/integral2)

delta_rise = t2 - t1
delta_fall = t4 - t3
print("delta_rise:", delta_rise, "\ndelta_fall:", delta_fall)

plt.plot(t, y, marker='.')
plt.xlabel('t')
plt.ylabel('V')

plt.show()
