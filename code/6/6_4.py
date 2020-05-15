# 迭代法
# 书中例6.4
# 只测试了区间[0, 2]
import math

def g(x):
	return (2*x + 3)**(1 / 3)
	# return math.log(x+2)
def f(x):
	return x**3 - 2*x - 3

def _6_4(a, b, eps = 1e-6):
	x_old = a
	while True:
		x_new = g(x_old)
		print(x_new)
		if abs(x_new - x_old) < eps:
			return x_new
		else:
			x_old = x_new

		if(x_new > b):
			return "no result,break!"


print(_6_4(1, 2))