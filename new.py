import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Proje dizinindeki dosya yolunu oluştur
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'gaussian.csv')

# Veriyi oku
data = pd.read_csv(file_path)

# X eksenini oluştur
x_axis = np.linspace(0, 200, len(data))

# En yüksek değeri (T0) ve indeksini bul
max_value = data.values.max()
max_index = data.values.argmax()
max_x = x_axis[max_index]

# T0'nun %10 ve %90 değerlerini hesapla
t0_10_percent = max_value * 0.1
t0_90_percent = max_value * 0.9

# Lineer interpolasyon fonksiyonu
def linear_interpolate(x0, y0, x1, y1, y):
    return x0 + (y - y0) * (x1 - x0) / (y1 - y0)

# T1, T2, T3, T4 değerlerini bulma fonksiyonu
def find_t_values(data, x_axis, max_index, target_value):
    for i in range(len(data) - 1):
        if (data[i] - target_value) * (data[i + 1] - target_value) < 0:
            return linear_interpolate(x_axis[i], data[i], x_axis[i + 1], data[i + 1], target_value)
    return None

# T1, T2, T3, T4 değerlerini bul
t1_x = find_t_values(data.values[:max_index].flatten(), x_axis[:max_index], max_index, t0_10_percent)
t2_x = find_t_values(data.values[:max_index].flatten(), x_axis[:max_index], max_index, t0_90_percent)
t3_x = find_t_values(data.values[max_index:].flatten(), x_axis[max_index:], max_index, t0_90_percent)
t4_x = find_t_values(data.values[max_index:].flatten(), x_axis[max_index:], max_index, t0_10_percent)
print("t0_peak:", max_x, "\nt1:", t1_x, "\nt2:", t2_x, "\nt3:", t3_x, "\nt4:", t4_x)

# Trapezoid yöntemi ile integral hesaplama fonksiyonu
def trapezoidal_rule(x, y):
    integral = 0.0
    for i in range(len(x) - 1):
        integral += (x[i + 1] - x[i]) * (y[i + 1] + y[i]) / 2
    return integral

# T1'den T4'e kadar integral hesaplama
t1_index = np.where(x_axis >= t1_x)[0][0]
t3_index = np.where(x_axis >= t3_x)[0][0]
t4_index = np.where(x_axis >= t4_x)[0][0]


integral_t1_t4 = trapezoidal_rule(x_axis[t1_index:t4_index+1], data.values.flatten()[t1_index:t4_index+1])
integral_t3_t4 = trapezoidal_rule(x_axis[t3_index:t4_index+1], data.values.flatten()[t3_index:t4_index+1])

print("integral_t3_t4:", integral_t3_t4)
print("integral_t1_t4:", integral_t1_t4)
print("integral_oranlari:", integral_t3_t4/integral_t1_t4)

#Time
delta_rise = t2_x - t1_x
delta_fall = t4_x - t3_x
print("delta_rise:", delta_rise, "\ndelta_fall:", delta_fall)

# Grafiği çiz
plt.figure(figsize=(12, 7))
plt.plot(x_axis, data.values.flatten(), label='Data')
plt.scatter(max_x, max_value, color='red', label='T0 (Max Value)')
plt.text(max_x, max_value, ' T0', verticalalignment='bottom', horizontalalignment='right')
plt.scatter([t1_x, t2_x, t3_x, t4_x], [t0_10_percent, t0_90_percent, t0_90_percent, t0_10_percent], color='green', label='T1, T2, T3, T4 Points')
plt.text(t1_x, t0_10_percent, ' T1', verticalalignment='bottom', horizontalalignment='right')
plt.text(t2_x, t0_90_percent, ' T2', verticalalignment='bottom', horizontalalignment='right')
plt.text(t3_x, t0_90_percent, ' T3', verticalalignment='bottom', horizontalalignment='right')
plt.text(t4_x, t0_10_percent, ' T4', verticalalignment='bottom', horizontalalignment='right')
plt.title('Data Distribution with T0, T1, T2, T3, T4 Points Marked')
plt.xlabel('X Axis')
plt.ylabel('Data Values')
plt.legend()
plt.grid(True)
plt.show()

