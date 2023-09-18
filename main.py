import numpy as np 
import matplotlib.pyplot as plt

def gaussian(x, x0, std_dev, lambda_val):
    if x <= x0:
        exp = np.exp(-((x - x0) ** 2) / (2 * std_dev ** 2))
        coefficient = 1 / (std_dev * np.sqrt(2 * np.pi))
        return coefficient * exp
    else:
        return np.exp(-lambda_val * (x - x0))

x = np.linspace(0, 1024, 20)
x0 = 0
std_dev = 1
lambda_val = 0.5

y = [gaussian(x_val, x0, std_dev, lambda_val) for x_val in x]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Mixed Gaussian and Exponential function')
plt.grid(True)
plt.show()
