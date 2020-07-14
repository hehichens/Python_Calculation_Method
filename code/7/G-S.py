# G-S迭代算法
# 

def G_S(A, b, max_iter=30, eps=1e-6):
	N = len(b)
	X_old = [0, 0, 0]
	X_new = X_old.copy()
	for iter in range(max_iter):
		for i in range(N):
			X_new[i] = (b[i] 
				- sum([A[i][j]*X_new[j] for j in range(i)]) 
				- sum([A[i][j]*X_old[j] for j in range(i+1, N)])) / A[i][i] # 更新

		err = max([abs(x_old - x_new) for x_old, x_new in zip(X_old, X_new)])

		print(iter+1, X_new, err)
		if (err) < eps:
			return X_new 
		else:
			X_old = X_new.copy()
	return X_new

# A = [[4, 1, -1], [2, 5, 2], [1, 1, 3]]
# b = [5, -4, 3]

# A = [[10, -2, -1], [-2, 10, -1], [-1, -2, 5]]
# b = [3, 15, 10]

A = [[-8, 1, 1],
[1, -5, 1], 
[1, 1, -4]]
b = [1, 16, 7]
print(G_S(A, b))