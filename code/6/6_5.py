# 牛顿法
# 6.5
# 

def f(x):
	return x**2 - 115

def df(x, d=1e-5):
	return (f(x+d)-f(x-d))/(2*d)

def _6_5(a, b, eps=1e-5):
	x_old = a
	while True:
		x_new = x_old - f(x_old) / df(x_old)
		if abs(x_old - x_new) < eps:
			return x_new
		else:
			x_old = x_new
		if x_new > b:
			return "no result,break!"
		print(x_old)


print(_6_5(10, 16))