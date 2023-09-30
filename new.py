import numpy as np
import matplotlib.pyplot as plt

def gauss(t, t0, sigma):
    expo = np.exp(-(t - t0)**2 / (2 * (sigma ** 2)))
    return expo

def f(t):
    lamda = 0.01
    mix = np.exp(-lamda * t)
    return mix

def combined_function(tr, t0, tf):
    t = np.linspace(tr, tf, 1000)
    t_gauss = t[np.logical_and(t >= tr, t <= t0)]
    t_f = t[np.logical_and(t >= t0, t <= tf)]
    
    gauss_values = gauss(t_gauss, t0, 100)
    f_values = f(t_f)
    
    return np.concatenate((gauss_values, f_values), axis=None)

tr = 0
t0 = np.random.uniform(0, 51)  # 0 ile 51 arasında rastgele bir t0 değeri üretir
tf = t0 + 51

result = combined_function(tr, t0, tf)
data = np.array(result)
uniform_data = data  #np.random.uniform(0, 0.3, data.shape[0])

mean = np.mean(data)
maximum = np.max(data)
minimum = np.min(data)
print("t0:", t0)
print("Mean:", mean)
print("Maximum:", maximum)
print("Minimum:", minimum)

plt.plot(uniform_data, marker='.')
plt.show()
