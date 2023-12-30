import sympy as sp

x = sp.Symbol('x')
# 定义表达式y = x**20+x**2
y = x ** 3 + x ** 2
diffy = sp.diff(y)
print(diffy)
xvalue = sp.solve(diffy, x)
print(xvalue)
for value in xvalue:
    print(y.subs(x, value))
