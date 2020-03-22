'''
保留有效数字
'''

def Significant_Digit(x, n):
    '''
    x:输入的数字
    n：有效位数
    return：
    x_hat:有效数字
    '''
    m = len(str(int(x))) # 求取整数位数
    x_hat = round(x, n-m)

    return x_hat
            
x = 3.1415926  
n = 5
print(Significant_Digit(x, n))
