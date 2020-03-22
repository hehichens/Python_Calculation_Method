# -*- coding: utf-8 -*-
"""
根据相对数字计算有效数字
"""

# import utils
import numpy as np
import sys
sys.path.append('..') # 为了导入上一层目录的utils
import utils

def _1_3(x, eps):
    '''
    x:小数
    eps:相对误差
    return:
    n:有效位数
    x_hat:  根据相对数字计算的有效数字
    '''
    alpha = int(str(x)[0]) # 求alpha_1
    N = len(str(x))
    for i in range(N):
        if (1/(2*alpha) * 10**(-i+1)) <= eps:
            break
    n = i
    x_hat = utils.Significant_Digit(x, n)
    return n, x_hat

x = np.sqrt(20)
eps = 1e-3
print(_1_3(x, eps))