from time import *

'''
优化前:
范围:10000,时间:6.665999412536621s
范围:20000,时间:29.621161937713623s
'''
# 优化前
start = time()
num = 2
while num <= 20000:
    i = 1
    _count = 0
    while i <= num:
        if num % i == 0:
            _count += 1
        i += 1
    else:
        if _count == 2:
            pass
            # print(f"{num}是质数")
        # else:
        #     print(f"{num}是合数")
    num += 1
end = time()
print(f"执行时间{end - start}s")

