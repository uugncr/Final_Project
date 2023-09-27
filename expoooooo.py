import numpy as np
import matplotlib.pyplot as plt

def f(t):
    lamda = 0.001  # Decrease the value of lamda for proper visualization
    mix = np.exp(-lamda * t)
    return mix

t = np.linspace(0, 200, 200)
y = f(t)

plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Exponential Decay')
plt.show()

