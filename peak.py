import numpy as np
import matplotlib.pyplot as plt

def gauss(t, t0, s_r, s_f):
    N = 20
    if t < t0:
        expo = N * np.exp(-(t - t0)**2 / (2 * (s_r ** 2)))
        return expo
    else:
        mix = N * np.exp(- (t - t0)**2 /s_f **2 )
        return mix


t = np.linspace(0, 1024,1024)
t0 = np.random.uniform(0,1024)

s_r = 6
s_f = 25


y = np.array([gauss(i, t0, s_r, s_f) for i in t])

x = t
y = y

print(x)
print(y)
"""
plt.plot(t, y,'-b' , marker = '.')
plt.xlabel('t')
plt.ylabel('V')

plt.show()

"""