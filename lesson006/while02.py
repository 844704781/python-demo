# 求100以内所有7的倍数之和，以及个数
i = 0
_sum = 0
_count = 0
while i <= 100:
    if i % 7 == 0:
        _sum += i
        _count += 1
    i += 1
else:
    print(f"_sum是{_sum}, 个数是{_count}")  # _sum=735
