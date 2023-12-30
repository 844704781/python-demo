import sympy as sp

x = sp.Symbol('x')
y = x ** 3 - 6 * x ** 2 + 9 * x + 1
print("原函数f(x)=", y)
# 求导
fn = sp.diff(y, x)
print("导数:", fn)  # 3*x**2 - 12*x + 9
s = sp.solve(fn, x)
print("极值点:", s)  # [1, 3]
s0 = y.subs(x, s[0])
s1 = y.subs(x, s[1])
print(s0)  # 5
print(s1)  # 1
