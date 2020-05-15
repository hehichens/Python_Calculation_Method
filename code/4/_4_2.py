# 反幂法求特征向量

import numpy as np 

def eig(X, v, N = 100, eps=1e-4):
	'''
	X:要求的矩阵
	v:初始化向量
	N：最大循环次数
    eps:允许误差

	return:
	特征值和特征向量
	'''
	m_old = np.inf
	inv_X = np.linalg.inv(X)
	u = v
	for i in range(N):
		v = np.dot(inv_X, u)
		m_new = max(v)
		u = v / m_new
		print(i+1, v, m_new, u)
		if np.abs(m_old - m_new) < eps:
			break
		else:
			m_old = m_new

	return m_new, u, i

# =============================================================================
 # 测试用例
A = np.array([[ 2,  3,  8],
         [3,  9, 4],
         [ 8,  4,  1]])


v = np.array([-1, 1, 1])

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
