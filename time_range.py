import peak as p
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

index = np.argmax(p.y)
t0_value = p.t[index]
y_value = p.y[index]

print(t0_value, y_value)

t0_inter = interpolate.interp1d(p.y)
t0_new = [p.t0+1, p.t0-1]
