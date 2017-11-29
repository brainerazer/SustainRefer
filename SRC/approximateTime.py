# coding: utf-8
import numpy as np
from scipy import optimize
from math import sqrt

def First_func(p, c):
        l = p
        ll = np.log(l)
        pw = np.multiply(np.power(l, 0.5), np.power(ll, 1 - 0.5))
        e = np.exp(np.multiply(sqrt(2), pw))
        r = np.ceil(np.multiply(c, e))
        return r
def Second_func(p, c):
        l = p
        ll = np.log(l)
        pw = np.multiply(np.power(l, 0.5), np.power(ll, 1 - 0.5))
        e = np.exp(np.multiply(1, pw))
        r = np.ceil(np.multiply(c, e))
        return r
def Func(p, c2, c3):
        return First_func(p, c2) + Second_func(p, c3)
def F(p):
    return Func(p, 2.66617175e-05, 3.30120489e-13)

def F(p, w):
    return Func(p, 2.66617175e-05 * (4 / w), 3.30120489e-13)

wholetime = lambda p: First_func(p / 1.44269504089, 2.66617175e-05) * 4 + Second_func(p, 3.30120489e-13)

print(optimize.ridder(lambda x : F(x, 4) - 31536000, 1, 500) * 1.44269504089)
print(wholetime(124) / 60 * 0.0065)