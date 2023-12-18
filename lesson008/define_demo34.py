lambda1 = lambda meta: meta % 2 != 0
result1 = lambda1(3)
print(result1)
# 或者
result2 = (lambda meta: meta % 2 != 0)(3)
print(result2)
