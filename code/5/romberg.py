# 龙贝格

def f(x):
	return 4/(1 + x ** 2)

def f1(x):
	return 1 / (1+x)

def romberg(f, a, b, N=10, eps=10-9):
	Mat = [[0]*4 for _ in range(N+3)]
	Mat[0][0] = 1 / 2 * (f(a) + f(b))
	for i in range(1, N+3):
		Mat[i][0] = 1/2 * Mat[i-1][0] + (b - a) / 2**i * sum([f(a + (2*k - 1)*(b-a)/2**i) for k in range(1, 2**(i-1)+1)])
		for j in range(1, min(i+1, 4)):
			Mat[i][j] = (4**j * Mat[i][j-1] - Mat[i-1][j-1]) / (4 ** j - 1)
	return Mat

res = romberg(f1, 0, 1.5)
for line in res:
	print(line)
