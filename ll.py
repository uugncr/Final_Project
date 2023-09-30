import numpy as np
import matplotlib.pyplot as plt
import random
from noise import pnoise1

def gauss(t, t0, s_r):
    expo = np.exp(-(t - t0)**2 / (2 * (s_r ** 2)))
    return expo

def expo(t, s_f):
    mix = np.exp(- (t/2) * (1 / s_f ** 2))
    return mix


def combined_function(tr, t0, tf):
    t = np.linspace(0, 1024, 512)
    t_gauss = t[np.logical_and(t >= tr, t <= t0)]  
    t_f = t[np.logical_and(t >= t0, t <= tf)]  
    
    gauss_values = gauss(t_gauss, t0, 200)  
    f_values = expo(t_f, 100)
    
    return np.concatenate((gauss_values, f_values))


tr = 0
t0 = 500
tf = 1024

result = 6 + combined_function(tr, t0, tf) 
#print(result)


data = np.array(result)

s_data = data

plt.plot(s_data, marker='.')
plt.show()
