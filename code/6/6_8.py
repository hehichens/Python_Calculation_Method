# 解非线性方程组的牛顿法
# 书中例6.8
# 
import numpy as np 

def J(x):
	# 求雅可比矩阵
	return np.array([[-2*x[0], 1], 
		[1-x[1], -x[0]]])

def F(x):
	return np.array([
		x[1] - x[0]**2,
		x[0] - x[0]*x[1] + 1
	])

def _6_8(x0, eps=1e-6):
	x_old = x0
	while True:
		A = np.mat(J(x_old))
		b = -np.mat(F(x_old)).T # 注意这里是负数
		dx = np.array([float(i) for i in np.linalg.solve(A,b)])
		if(dx[0] == np.nan):
			break
		x_new = x_old + dx
		# print(x_new)
		if np.sum(F(x_new)**2) < eps:
			return x_new
		else:
			x_old = x_new

print(_6_8(np.array([1.5, 1.5])))