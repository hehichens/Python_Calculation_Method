# -*- coding: utf-8 -*-
"""
拉格朗日线性插值和抛物线插值
"""
import numpy as np
import matplotlib.pyplot as plt

def _2_2(X, Y, x, method='linear'):     
    if method == 'linear':
        y = Linear(X, Y, x)
    elif method == 'parabola':
        y = Parabola(X, Y, x)
    return y
        
def Linear(X, Y, x):
    for i in range(len(X)):
        if X[i] > x:
            break
    x0, y0 = X[i-1], Y[i-1]
    x1, y1 = X[i], Y[i]
     
    y = -y0*(x - x1) + y1*(x - x0)
    return y

def Parabola(X, Y, x):
    for i in range(len(X)):
        if X[i] > x:
            break
    x0, y0 = X[i-1], Y[i-1]
    x1, y1 = X[i], Y[i]
    x2, y2 = X[i+1], Y[i+1]
    y = 1/2*y0*(x - x1)*(x - x2) - y1*(x - x0)*(x - x2) + 1/2*y2*(x - x0)*(x - x1)
    return y

X = [10, 11, 12, 13, 14]
Y = [2.3026, 2.3979, 2.4849, 2.5649, 2.6391]
x = 11.5

# =============================================================================
# 测试例题
# print(_2_3(X, Y, x, method='linear'))
# print(_2_3(X, Y, x, method='parabola'))
# =============================================================================

# =============================================================================

# 可视化
# xx = np.arange(min(X)+0.1, max(X)-1, 0.1)
# yy1 = np.array([_2_3(X, Y, x, method='linear') for x in xx])
# yy2 = np.array([_2_3(X, Y, x, method='parabola') for x in xx])
# plt.subplot(211)
# plt.plot(X, Y, 'o')
# plt.plot(xx, yy1)
# plt.title('yy1')
# plt.subplot(212)
# plt.plot(X, Y, 'o')
# plt.plot(xx, yy2)
# plt.title('yy2')
# plt.show()
# =============================================================================
