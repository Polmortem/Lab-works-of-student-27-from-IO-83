from random import randrange

a0, a1, a2, a3 = 1, 3, 3, 7
print("a0 =", a0, "\na1 =", a1, "\na2 =", a2, "\na3 =", a3)

X1 = [randrange(1, 21, 1) for k in range(8)]
X2 = [randrange(1, 21, 1) for k in range(8)]
X3 = [randrange(1, 21, 1) for k in range(8)]

Y = [a0 + a1 * X1[k] + a2 * X2[k] + a3 * X3[k] for k in range(8)]
print("X1:", X1, "\nX2:", X2, "\nX3:", X3, "\nY: ", Y)

X01 = (max(X1) + min(X1)) / 2
X02 = (max(X2) + min(X2)) / 2
X03 = (max(X3) + min(X3)) / 2
print("x0:", X01, X02, X03)

dX1 = X01 - min(X1)
dX2 = X02 - min(X2)
dX3 = X03 - min(X3)
print("dx:", dX1, dX2, dX3)

Xn1 = [(X1[k] - X01) / dX1 for k in range(8)]
Xn2 = [(X2[k] - X02) / dX2 for k in range(8)]
Xn3 = [(X3[k] - X03) / dX3 for k in range(8)]
print("Xн1:", Xn1, "\nXн2:", Xn2, "\nXн3:", Xn3)

Yet = a0 + a1 * X01 + a2 * X02 + a3 * X03
print("Yет:", Yet)

f = [(Y[k] - Yet) ** 2 for k in range(8)]
res = min(f)
print("(Y-Yет)²:", f)
print("min(Y-Yет)²:", res)
