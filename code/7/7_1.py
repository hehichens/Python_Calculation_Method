# 高斯消元法
# 课本例７．１

def _7_1(A, b):
    if len(A) != len(A[0]):
        return "the shape of A must be (n, n)"
    n = len(A)
    '''
    １．求m时，每次除的都是对角线上的值
    ２．两个循环只有ｋ　和　ｉ　的顺序不同
    '''
    # 高斯消元
    for k in range(n-1):
        for i in range(k+1, n):
            m = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= m * A[k][j]
            b[i] -= m * b[k]

    # print(A)
    # 回代
    for k in range(n-1, 0, -1):
        for i in range(k-1, -1, -1):
            m = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= m * A[k][j]
            b[i] -= m * b[k]
    return [b[i] / A[i][i] if b[i] != 0 else 0 for i in range(n) ]

A = [[2, 2, 2],
     [3, 2, 4],
     [1, 3, 9]]
b = [1, 1/2, 5/2]

# 使用了一个很小的数字做除数
# A = [[1e-5, 1],
#      [1, 1]]
# b = [1, 2]

print(_7_1(A, b))