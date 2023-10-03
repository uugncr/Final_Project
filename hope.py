import numpy as np
import matplotlib.pyplot as plt

def gauss(t, t0, s_r, s_f):
    if t < t0:
        expo = np.exp(-(t - t0)**2 / (2 * (s_r ** 2)))
        return expo
    else:
        #mix = np.exp(- t * (1 /2 * s_f ** 2)) t=0  icin 
        mix = np.exp(- (t - t0)**2 /s_f **2 )
        return mix

t = np.linspace(0, 1024)
t0 = np.random.uniform(0,1024)
s_r = 100
s_f = 400
y = np.array([gauss(i, t0, s_r, s_f) for i in t])
print(y)

###################################################
"""
perfect_gauss = np.exp(-(t - t0) ** 2 / (2 * s_r ** 2)) / (s_r * np.sqrt(2 * np.pi))
plt.plot(t, perfect_gauss, '-b')
"""
###################################################


plt.plot(t, y,'-r' , marker = '.')
plt.xlabel('t')
plt.ylabel('gauss(t)')

plt.show()