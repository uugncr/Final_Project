import numpy as np


def gauss(t, t0, sigma):
    expo = np.exp(- (t - t0)** 2 / (2 * (sigma ** 2)))
    return expo

def f(t):
    lamda = 0.01
    mix = np.exp(- lamda * t)
    return mix


