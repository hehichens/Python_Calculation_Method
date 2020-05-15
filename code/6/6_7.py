# 迭代法解非线性方程组
# 书中例6.7
# 

import numpy as np

def g(x):
	return np.array([-np.sqrt(4 - x[1]**2), 1-np.exp(x[0])])

def _6_7(x0, eps=1e-3):
	x_old = x0
	while True:
		x_new = g(x_old)
		# print(x_new)
		if abs(np.sum(x_old - x_new)) < eps:
			return x_new
		else:
			x_old = x_new

print(_6_7(np.array([-1.8, 0.8])))