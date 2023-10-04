import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def gauss(t, t0, s_r, s_f):
    N = 20
    if t < t0:
        expo = N * np.exp(-(t - t0)**2 / (2 * (s_r ** 2)))
        return expo
    else:
        mix = N * np.exp(- (t - t0)**2 /s_f **2 )
        return mix

t = np.linspace(0, 1024,1024)
#t0 = np.random.uniform(0,1024)
t0 = 512

s_r = 6
s_f = 25


y = np.array([gauss(i, t0, s_r, s_f) for i in t])
print(y)

"""def t_check(y, t_values, t0, s_r, s_f):
    for i, t in enumerate(t_values):
        if gauss(t, t0, s_r, s_f) == y:
            return t
    return None

result_t1 = t_check(2.273555, t, t0, s_r, s_f)
print(result_t1)"""
"""
desired_y = 2

# Initialize an empty list to store matching t values
matching_t_values = []

# Iterate over t values and check if gauss(t, t0, s_r, s_f) is equal to 2
for i in t:
    if gauss(t, t0, s_r, s_f) == desired_y:
        matching_t_values.append(t)

# Print the matching t values
print(matching_t_values)

################################################### --1
"""
"""max_index = np.argmax(y)
t0_value = t[max_index]
y_value = y[max_index]"""
""""""
#print("(t0, y) = ({}, {})".format(t0_value, y_value))

################################################### --2



plt.plot(t, y,'-b' , marker = '.')
plt.xlabel('t')
plt.ylabel('V')

plt.show()