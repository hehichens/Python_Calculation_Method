# 乘幂法的加速法

import numpy as np

def Aitken(X, v, N = 100, eps=1e-9):
    a = [] # 保存a
    lambda_old = np.inf
    for i in range(N):
        v = np.dot(X, v)
        a.append(v.max())
        v = v / a[-1]
        if i >= 2:
            # 第三次计算lambda
            # print(a)
            a0, a1, a2 = a[-3:]
            lambda_new = a0 - (a1 - a0)**2 / (a2 - 2*a1 + a0)
            if np.abs(lambda_new - lambda_old) < eps:
                break
            else:
                lambda_old = lambda_new
    return a[-1], v, i

# =============================================================================
# # 测试用例
# A = np.array([[ 2,  3,  2],
#         [10,  3,  4],
#         [ 3,  6,  1]])
# v = np.array([0, 0, 1])
# 
# a, v, i = Aitken(A, v)
# print("eig value:", a)
# print("eig vector:", v)
# print("times:", i)
# =============================================================================
            
        