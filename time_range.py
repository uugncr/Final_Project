import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import interpolate

#Fonksiyon aaa

def f(t, t0, s_r, s_f,N):
    if t < t0:
        expo = N * np.exp(-(t - t0)**2 / (2 * (s_r ** 2)))
        return expo
    else:
        mix = N * np.exp(- (t - t0)**2 /s_f **2 )
        return mix

t = np.linspace(0, 1024, 1024)

t0 = np.random.uniform(0, 1024)
N = np.random.uniform(20, 500)
s_r = np.random.uniform(5.5, 6.5)
s_f = np.random.uniform(48, 52)

y = np.array([f(i, t0, s_r, s_f, N) for i in t])

#np.savetxt('gaussian_2.csv', y, delimiter=',')
print("N:", N, "\nN%10:", N * 0.1, "\nN%90:", N * 0.9)

t1 = t[np.where(np.logical_and(y < N * 0.1, t < t0))][-1]
t2 = t[np.where(np.logical_and(y < N * 0.9, t < t0))][-1]
t3 = t[np.where(np.logical_and(y > N * 0.9, t > t0))][-1]
t4 = t[np.where(np.logical_and(y > N * 0.1, t > t0))][-1]

print(f"t1: {t1}\nt2: {t2}\nt0: {t0}\nt3: {t3}\nt4: {t4}")

#Integral
f_lambda = lambda x: f(x, t0, s_r, s_f, N)
integral, error = integrate.quad(f_lambda, t0, t4)
integral2, error2 = integrate.quad(f_lambda, t1, t4)
print("integral_t0_t4:",integral)
print("integral_t1_t4:",integral2)
print("integral_oranlari:", integral/integral2)

#Time
delta_rise = t2 - t1
delta_fall = t4 - t3
print("delta_rise:", delta_rise, "\ndelta_fall:", delta_fall)

plt.plot(t, y, marker='.')
plt.xlabel('t')
plt.ylabel('V')

plt.show()
