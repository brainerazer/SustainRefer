#!/usr/local/bin/python3

import scipy.optimize
import numpy as np
from math import ceil, log, exp
import matplotlib.pyplot as plt
import sys
from matplotlib2tikz import save as tikz_save

data = np.genfromtxt(sys.argv[1], delimiter=',')

def B_func(p, c):
    l = p
    ll = np.log(l)
    pw = np.multiply(np.power(l, 0.5), np.power(ll, 1 - 0.5))
    e = np.exp(np.multiply(0.5, pw))
    r = np.ceil(np.multiply(c, e))
    return r

def R_func(p, c):
    l = p
    ll = np.log(l)
    pw = np.multiply(np.power(l, 0.5), np.power(ll, 1 - 0.5))
    e = np.exp(np.multiply(2, pw))
    r = np.ceil(np.multiply(c, e))
    return r

x = data[:, 1]
log_x = np.log(x)
y = data[:, 2]

print(log_x)
print(y)

b = scipy.optimize.curve_fit(B_func, log_x, y, bounds=(1,8), diff_step=0.01)

print(b)

points = plt.plot(data[:, 0], y, 'ro', label='Реальні результати')
plt.xlabel("Довжина, біт")
plt.ylabel("Межа B")

plt.plot(data[:, 0], B_func(log_x, b[0]), label='Апроксимована крива')

plt.legend(loc='lower right')
tikz_save('figure.tex')