

import numpy as np
import matplotlib.pyplot as plt

def P_3_1(X, Y, n):

    XM = []
    for i in range(2*len(X)):
        XM.append(sum([x_**i for x_ in X]))
    

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

X = [1.36, 1.49, 1.73, 1.81, 1.95]
Y = [14.094, 15.069, 16.844, 17.378, 18.435]


a1 = P_3_1(X, Y, 2)
print(a1)
xx = [i for i in np.arange(1.3, 2.0, 0.01)]
yy = [foo(a1, x) for x in xx]
plt.subplot(211)
plt.plot(X, Y, 'o')
plt.plot(xx, yy, '-')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

a2 = P_3_1(X, Y, 3)
print(a2)
xx = [i for i in np.arange(1.3, 2.0, 0.01)]
yy = [foo(a2, x) for x in xx]
plt.subplot(212)
plt.plot(X, Y, 'o')
plt.plot(xx, yy, '-')

plt.show()