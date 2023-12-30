import sympy as sp

x, y = sp.symbols('x y')
# 解方程组
# y=1-x
# 3x+2y=5
result = sp.solve([sp.Eq(y, 1 - x), sp.Eq(3 * x + 2 * y, 5)], [x, y])
print(result)  # {x: 3, y: -2}
