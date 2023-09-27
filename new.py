import numpy as np
import matplotlib.pyplot as plt
import random
def gauss(t, t0, sigma):
    expo = np.exp(-(t - t0)** 2 / (2 * (sigma ** 2)))
    return expo


def f(t):
    lamda = 0.01
    mix = np.exp(- lamda * t)
    return mix
#####################################################################

def combined_function(tr, t0, tf):
    t = np.linspace(tr, tf, 200)
    t_gauss = t[np.logical_and(t >= tr, t <= t0)]  # tr ile t0 arasındaki değerler
    t_f = t[np.logical_and(t >= t0, t <= tf)]  # t0 ile tf arasındaki değerler
    
    gauss_values = gauss(t_gauss, t0, 1)  # Gauss fonksiyonunu tr ile t0 arasında hesapla
    f_values = f(t_f)  # f fonksiyonunu t0 ile tf arasında hesapla
    
    return np.concatenate((gauss_values, f_values),axis=None)

#Örnek 
tr = 0
t0 =random.uniform(0,512)
tf = 512

result = combined_function(tr, t0, tf)
data = np.array(result)
uniform_data = data + np.random.uniform(0, 0.3, data.shape[0] )

mean = np.mean(data)
maximum = np.max(data)
minimum = np.min(data)
print(mean, maximum, minimum)

plt.plot(uniform_data) # marker = '.'

plt.show()


