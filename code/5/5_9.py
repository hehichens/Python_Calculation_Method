

def backward(X):
    x0, x1, x2 = X[:]
    return 1/0.2 * (-3 * f(x0) + 4 * f(x1) - f(x2))

def forward(X):
    x0, x1, x2 = X[:]
    return 1 / 0.2 * (f(x0)  - 4 * f(x1) + 3 * f(x2))

def mid(X):
    x0, x1, x2 = X[:]
    return 1 / 0.2 * (f(x2) - f(x0))

# define the function
X = [2.5, 2.6, 2.7, 2.8, 2.9]
Y = [12.1825, 13.4637, 14.8797, 16.4446, 18.1741]
F = {}
for x, y in zip(X, Y):
    F[x] = y
def f(x):
    return F[x]

print(backward(X[2:]))
print(forward(X[:3]))
print(mid(X[1:4]))
