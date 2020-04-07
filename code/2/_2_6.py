#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import numpy as np
import matplotlib.pyplot as plt

def _2_6(X, Y, ml, mr):
    H = [X[i] - X[i-1] for i in range(1, len(X))]
    alpha = [H[j-1]/(H[j-1]+H[j]) for j in range(1, len(H))]
    beta = [H[j]/(H[j-1]+H[j]) for j in range(1, len(H))]
    D = [3*(beta[j-1]/H[j-1]*(Y[j] - Y[j-1]) + alpha[j-1]/H[j]*(Y[j+1] - Y[j])) for j in range(1,len(H))]
    M = [None]*len(X)
    M[0], M[-1] = ml, mr    
    A = []
    b = []
    
    for j in range(1, len(H)):
        if M[j-1] != None:
            A.append([2, alpha[j-1]])
            b.append(D[j-1] - beta[j-1]*M[j-1])
        if M[j+1] != None:
            A.append([beta[j-1], 2])
            b.append(D[j-1] - alpha[j-1]*M[j+1])
    A = np.mat(A)
    b = np.mat(b).T
    M[1:-1] = [float(i) for i in np.linalg.solve(A,b)]
    return H, M
    # Solve the equation

def foo(X, Y, H, M, x):
    for j in range(len(X)):
        if x < X[j]:
            break
    j = j-1
    y = (1+2*(x - X[j])/H[j])*((x - X[j+1])/H[j])**2*Y[j] + \
        (1-2*(x - X[j+1])/H[j])*((x - X[j])/H[j])**2*Y[j+1] + \
        (x - X[j])*((x - X[j+1])/H[j])**2*M[j] + \
        (x - X[j+1])*((x - X[j])/H[j])**2*M[j+1]
    return y
   
    
X = [-1, 0, 1, 2]
Y = [0, 0.5, 2, 1.5]
ml = 0.5
mr = -0.5
H, M = _2_6(X, Y, ml, mr)
print("M:", M)

x = 1.5
y = foo(X, Y, H, M, x)
print(y)


xx = [i for i in np.arange(-0.99, 1.99, 0.01)]
yy = [foo(X, Y, H, M, x) for x in xx]
plt.plot(X, Y, 'o')
plt.plot(xx, yy, '-')
plt.show()