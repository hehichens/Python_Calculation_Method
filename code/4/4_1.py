# 使用幂乘法求矩阵的特征值和特征向量

import numpy as np 

def eig(X, v, N = 100, eps=1e-9):
	'''
	X:要求的矩阵
	v:初始化向量
	N：最大循环次数
    eps:允许误差

	return:
	特征值和特征向量
	'''
	a_old = np.inf
	for i in range(N):
		
		v = np.dot(X, v)
		a_new = v.max()
		v = v / a_new
		print(i, v, a_new)
		if np.abs(a_old - a_new) < eps:
			break
		else:
			a_old = a_new

	return a_new, v, i

# =============================================================================
 # 测试用例
A = np.array([[ 7,  3,  -2],
         [3,  4, -1],
         [ -2,  -1,  3]])
v = np.array([0, 0, 1])
 
a, v, i = eig(A, v)
print("eig value:", a)
print("eig vector:", v)
print("times:", i)
# =============================================================================


# =============================================================================
 # 使用numpy 求
#A = np.array([[ 7,  3,  -2],
#         [3,  4, -1],
#         [ -2,  -1,  3]])
# eig_value, eig_vector = np.linalg.eig(A)
# print("eig value:", eig_value)
# print("eig vector:", eig_vector)
# =============================================================================
