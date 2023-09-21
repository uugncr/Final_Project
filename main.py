import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import quad


def gauss(x, mu, sigma):
    return np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

def gauss1(x, mu, sigma):

    if x < mu:
        return gauss(x , mu, sigma)

    else:
        cons1 = 2.3
        cons2 = 3
        cons3 = 0.3
        if x <= mu * sigma:
            return  np.exp(- cons1 * x)
        elif x<= mu * 2 * sigma:
            return np.exp(- cons2 * x)
        else:
            return np.exp(-cons3 * x)

x = np.arange(0, 1024, 20)
mu = 500
sigma = 100

y = gauss(x, mu, sigma)
plt.plot(x, y, label="Gaussian")

"""y1 = np.array([quad(gauss1, 0, val, args=(mu, sigma))[0] for val in x])
plt.plot(x, y1, label="Gauss1")
"""
y2 = [gauss1(val, mu, sigma) for val in x]
plt.plot(x, y2, label="Gauss2")


plt.xlabel("x")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
