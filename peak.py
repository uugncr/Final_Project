import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def f(t, t0, s_r, s_f):
    N = 20
    if t < t0:
        expo = N * np.exp(-(t - t0)**2 / (2 * (s_r ** 2)))
        return expo
    else:
        mix = N * np.exp(- (t - t0)**2 /s_f **2 )
        return mix


t = np.linspace(0, 1024,2048)
#t0 = np.random.uniform(0,1023)
#print(t0)
t0 = 512
s_r = 6
s_f = 25

y = np.array([f(i, t0, s_r, s_f) for i in t])
#print(y)
np.savetxt('gaussian.csv', y, delimiter=',')

cs = CubicSpline(t,y)
t_interp = t 
y_interp = cs(t_interp)

desired_value = 2
tolerance = 1e-0

for i in range(len(y_interp) - 1):
    if abs(y_interp[i] - desired_value) <= tolerance and abs(y_interp[i + 1] - desired_value) <= tolerance:
        print(f"Fonksiyon 2 olduğu nokta: x={t_interp[i]}, y={y_interp[i]}")
"""
def find_t(y, t, t0):
    closest_t = None
    min_diff = float('inf')

    for i in range(len(t)):
        if abs(y[i] - (t0 * 0.01)) < min_diff:
            min_diff = abs(y[i] - (t0 * 0.1))
            closest_t = t[i]

    return closest_t

# Call the function to find the closest t value to y = t0 * 0.1
closest_t = find_t(y, t, t0)
print(closest_t)

#formatted_array = [f"{num:.10f}" for num in y]
#print(formatted_array)
"""

"""
t1=[]

desir_y1 =20
if gauss(t, t0, s_r, s_f) == desir_y1 * 0.1:
    t1.append()

print(t1)"""

"""
index = np.argmax(y)
t0_value = t[index]
y_value = y[index]
print(t0_value, y_value)

"""
plt.plot(t, y, marker = '.')
plt.xlabel('t')
plt.ylabel('V')

plt.show()

