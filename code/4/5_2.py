from scipy.optimize import fsolve
def func(X):
	return [
		X[0]+X[1]+X[2],
		X[0]**2+X[1]**2+X[2]**2,
		X[0]**3+X[1]**3+X[2]**3
	]

fsolve(func, [0, 1, ])