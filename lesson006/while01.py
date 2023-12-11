# 求100以内所有的奇数之和
i = 0
_sum = 0
while i <= 100:
    if i % 2 != 0:
        print(f"{i}是奇数")
        _sum += i
    i += 1
else:
    print(f"奇数的和是{_sum}")  # 2500
