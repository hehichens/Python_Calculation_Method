#  四阶龙格一库塔法
#  
#  

def _8_3(X):
	Y = [1] * len(X)
	for i in range(len(X)-1):
		K1 = 2 / 3 * X[i] * Y[i]**2
		K2 = 2 / 3 * (X[i] + 0.05)*(Y[i] + 0.05 * K1)**2
		K3 = 2 / 3 * (X[i] + 0.05)*(Y[i] + 0.05 * K2)**2
		K4 = 2 / 3 * (X[i] + 0.1)*(Y[i] + 0.1 * K3)**2
		Y[i+1] = Y[i] + 1 / 60 * (K1 + 2*K2 + 2*K3 + K4)
	return Y


X = [0.0, 0.1, 0.2 ,0.3, 0.4 ,0.5,0.6,0.7]
print(_8_3(X))
