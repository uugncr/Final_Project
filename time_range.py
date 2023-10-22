import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import integrate
from scipy import interpolate

#Fonksiyon

def f(t, t0, s_r, s_f,N):
    if t < t0:
        expo = N * np.exp(-(t - t0)**2 / (2 * (s_r ** 2)))
        return expo
    else:
        mix = N * np.exp(- (t - t0)**2 /s_f **2 )
        return mix

t = np.linspace(0, 200, 1024)
t0 = np.random.uniform(30, 50)
N = np.random.uniform(20, 500)
s_r = np.random.uniform(5.5, 6.5)
#s_f = np.random.uniform(23, 102)
s_f = np.random.uniform(98, 102)
print("N:", N, "\nN%10:", N * 0.1, "\nN%90:", N * 0.9, "\ns_r:", s_r, "\ns_f:", s_f)

########

y = np.array([f(i, t0, s_r, s_f, N) for i in t])
noise = np.random.uniform(4, 12, 1024)
peak = noise + y

#np.savetxt('noise.csv', noise, delimiter=',')
np.savetxt('gaussian.csv', peak, delimiter=',')




########

# t degerlerinin bulunmasi

t1 = t[np.where(np.logical_and(peak < N * 0.1, t < t0))][-1]
t2 = t[np.where(np.logical_and(peak < N * 0.9, t < t0))][-1]
t3 = t[np.where(np.logical_and(peak > N * 0.9, t > t0))][-1]
t4 = t[np.where(np.logical_and(peak > N * 0.1, t > t0))][-1]

print(f"t1: {t1}\nt2: {t2}\nt0: {t0}\nt3: {t3}\nt4: {t4}")

#Integral

f_lambda = lambda x: f(x, t0, s_r, s_f, N)
integral, error = integrate.quad(f_lambda, t0, t4)
integral2, error2 = integrate.quad(f_lambda, t1, t4)
print("integral_t0_t4:", integral)
print("integral_t1_t4:", integral2)
print("integral_oranlari:", integral/integral2)

#Time

delta_rise = t2 - t1
delta_fall = t4 - t3

print("delta_rise:", delta_rise, "\ndelta_fall:", delta_fall)

# % degerlerin cizimi

plt.plot([t[0], t[-1]], [N * 0.1, N * 0.1], 'r--', label='N%10')
plt.plot([t[0], t[-1]], [N * 0.9, N * 0.9], 'r--', label='N%90')

#noise alt/ust cizimi

plt.plot([t[0], t[-1]], [4, 4], 'g--', label='y = 4')
plt.plot([t[0], t[-1]], [12, 12], 'g--', label='y = 12')

#plt.plot(t, y = f(t, t0, s_r, s_f, N), 'b--', marker=',')
plt.plot (t, peak, marker=',')
plt.xlabel('t')
plt.ylabel('V')

plt.show()

#https://ravenfo.com/2021/07/11/normal-dagilim-python-normallik-testi/
#bak 

""" s_f =23<27
0.731
0.762
0.751
0.753
0.756
0.754
0.741
0.748
0.761
0.735
"""
"""s_f = 48<52
0.848
0.868
0.861
0.858
0.855
0.859
0.860
0.849
0.854
0.863
"""
"""s_f = 98<102
0.923
0.918
0.920
0.927
0.924
0.919
0.924
0.921
0.923
0.917
"""
