import numpy as np
import pandas as pd
from scipy import integrate
from scipy.interpolate import interp1d

# Function
def f(t, t0, s_r, s_f, N):
    expo = np.exp(-(t - t0)**2 / (2 * (s_r ** 2)))
    mix = np.exp(- (t - t0) / (s_f))
    return N * expo if t < t0 else N * mix

# Veri çerçeveleri ve listeleri
#gaussian_data = pd.DataFrame()
parameters_list = []

for i in range(5000):
    t = np.linspace(0, 200, 1024)
    t0 = round(np.random.uniform(30,40), 4)
    N = round(np.random.uniform(50, 800), 4)
    s_r = round(np.random.uniform(5.5, 6.5), 4)
    s_f = round(np.random.uniform(98,102), 4)
    # Gaussian sinyali üretiliyor
    y = np.array([f(i, t0, s_r, s_f, N) for i in t])
    noise = np.random.uniform(2, 8, 1024)
    peak = noise + y
    
    interpolated_peak = interp1d(t, peak, kind='cubic')

    t_fine = np.linspace(t.min(), t.max(), 10000)
    peak_fine = interpolated_peak(t_fine)
    

    t1 = t_fine[np.where(np.logical_and(peak_fine < N * 0.1, t_fine < t0))][-1]
    t2 = t_fine[np.where(np.logical_and(peak_fine < N * 0.9, t_fine < t0))][-1]
    t3 = t_fine[np.where(np.logical_and(peak_fine > N * 0.9, t_fine > t0))][-1]
    t4 = t_fine[np.where(np.logical_and(peak_fine > N * 0.1, t_fine > t0))][-1]
    
    # Integral
    f_lambda = lambda x: f(x, t0, s_r, s_f, N)
    integral, error = integrate.quad(f_lambda, t3, t4)
    integral2, error2 = integrate.quad(f_lambda, t1, t4)
    fom = integral / integral2

    # Time
    d_r = t2 - t1
    d_f = t4 - t3

    # Veriler listeye ekleniyor
    #new_columns = {f'signal_{i}': [peak] for i in range(len(peak))}
    #new_columns_df = pd.DataFrame(new_columns)

    # Concatenate with the original DataFrame
    #gaussian_data = pd.concat([gaussian_data, new_columns_df], axis=1)
    parameters_list.append({'t0': t0, 't1': t1, 't2': t2, 't3': t3, 't4': t4, 's_r': s_r, 's_f': s_f, 'N': N, 'd_r': d_r, 'd_f': d_f, 'total_integral': integral, 'tail_integral': integral2, 'fom': fom})


# Listeyi DataFrame'e dönüştürme
parameters_data = pd.DataFrame(parameters_list)

# Verileri kaydetme (burada kullanıcının belirleyebileceği dinamik bir yol kullanılabilir)
#gaussian_data.to_csv('data.csv', index=False)
parameters_data.to_csv('parameters100.csv', index=False)

