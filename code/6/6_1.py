
# 二分法求方程的根
# 参考书例子6.1
# 

# def f(x):
# 	return x**6 - x -1

def f(x):
	return x**3 + x - 4

def _6_1(a, b, eps = 1e-4):
	while True:
		t = (a +b) / 2
		print("[", a, "    ", b, "]", "    ", t,  "    ", f(t))
		if (b - a) < eps:
			return t
		if(f(a)*f(t) < 0):
			b = t
		else:
			a = t 

print(_6_1(1, 2))