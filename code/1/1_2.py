# -*- coding: utf-8 -*-
"""
求相对误差限
"""

def Relative_Error_Limit(x, n):
    '''
    x:数字
    n:有效位数
    return:
    sigma:相对误差限
    '''
    
    alpha = int(str(x)[0]) # 求alpha_1
    sigma = 1 / (2*alpha) * 10**(1-n)
    return sigma

x = 3.1416
n = 5
print(Relative_Error_Limit(x, n))