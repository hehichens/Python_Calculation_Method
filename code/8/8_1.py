# 实现欧拉方法和改进的欧拉方法

import numpy as np

def quadratic(a, b, c):
    if (b**2 - 4 * a * c) < 0:
        return 0
    delta = np.sqrt(b**2 - 4 * a * c)
    return (-b - delta) / (2 * a)

def _8_1_1(X):
	Y = [1]*len(X)
	for i in range(len(X)-1):
		Y[i+1] = Y[i] + 0.1 * 2 / 3 * X[i] * Y[i]**2
	return Y



def _8_1_2(X):
	Y = [1]*len(X)
	for i in range(len(X)-1):
		# print(1/30*X[i+1], -1, 1/30*X[i]*Y[i]**2+Y[i], quadratic(1/30*X[i+1], -1, 1/30*X[i]*Y[i]**2+Y[i]))
		Y[i+1] = quadratic(1/30*X[i+1], -1, 1/30*X[i]*Y[i]**2+Y[i])
	return Y



X = [0.0, 0.1, 0.2 ,0.3, 0.4 ,0.5,0.6,0.7]
print("before:", _8_1_1(X))
print("after:", _8_1_2(X))
