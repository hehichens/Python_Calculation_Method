#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:41:27 2020

@author: hichens
"""

import numpy as np
import matplotlib.pyplot as plt

def _3_1(X, Y, n):

    XM = []
    for i in range(2*len(X)):
        XM.append(sum([x_**i for x_ in X]))
    
    print(XM)
    A = []
    b = []       
    for i in range(n):
        a = []
        for j in range(n):
            a.append(XM[i+j])
        A.append(a)
        b.append(sum([Y[k]*X[k]**i for k in range(len(X))]))
    A = np.mat(A)
    b = np.mat(b).T
    return [float(i) for i in np.linalg.solve(A,b)]

def foo(a, x):
    return sum(a[i]*x**i for i in range(len(a)))

X = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1]
Y = [-0.2209, 0.3295, 0.8826, 1.4392, 2.0003, 2.5645, 3.1334, 3.7601, 4.2836]
a = _3_1(X, Y, 3)
print(a)

xx = [i for i in np.arange(-0.99, 0.99, 0.01)]
yy = [foo(a, x) for x in xx]
plt.plot(X, Y, 'o')
plt.plot(xx, yy, '-')
plt.show()