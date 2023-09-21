import numpy as np
import matplotlib.pyplot as plt


def gauss(x, mu, sigma):
    exp = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    coefficient = 1 / (sigma * np.sqrt(2 * np.pi))
    return coefficient * exp

def gauss1(x, mu, sigma):
    y = np.zeros_like(x)
    
    y[x < mu] = np.exp(-cons1 * x[x < mu])
    y[(x >= mu) & (x <= mu + sigma)] = np.exp(-cons2 * x[(x >= mu) & (x <= mu + sigma)])
    y[(x > mu + sigma) & (x <= mu + 2 * sigma)] = np.exp(- cons3 * x[(x > mu + sigma) & (x <= mu + 2 * sigma)])
    
    return y


x = np.arange(0, 1024, 20)

mu = 512
sigma = 170

cons1 = 100
cons2 = 200
cons3 = 400

y = [gauss(i, mu, sigma) for i in x]
#y = gauss(x, mu, sigma)
plt.plot(x, y, label="Gauss")


y1 = [gauss1(i, mu, sigma) for i in x]
y1 = gauss1(x, mu, sigma)
plt.plot(x, y1, label="Gauss_Exp")

plt.xlabel("x")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
