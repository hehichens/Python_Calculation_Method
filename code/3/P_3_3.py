

import numpy as np
import matplotlib.pyplot as plt

def P_3_3(X, Y, n):

    XM = []
    for i in range(2*len(X)):
        XM.append(sum([x_**i for x_ in X]))
    
    A = []  
    b = []       
    for i in range(n):
        if i != 1:
            a = []
            for j in range(n):
                if j != 1:
                    a.append(XM[i+j])
            A.append(a)
            b.append(sum([Y[k]*X[k]**i for k in range(len(X))]))
        
    A = np.mat(A)
    b = np.mat(b).T
    return [float(i) for i in np.linalg.solve(A,b)]

def foo(a, x):
    return a[0] + a[1]*x**2


X = [19, 25, 31, 38, 44]
Y = [19.0, 32.3, 49.0, 73.3, 97.8]
a = P_3_3(X, Y, 3)
print(a)
xx = [i for i in np.arange(19, 44, 0.01)]
yy = [foo(a, x) for x in xx]
plt.plot(X, Y, 'o')
plt.plot(xx, yy, '-')
plt.show()