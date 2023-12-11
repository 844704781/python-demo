from time import *

'''
break优化后:
范围:10000,时间: 2.5416488647460938s
范围:20000,时间: 10.196908473968506s
'''
# 优化前
start = time()
num = 2
while num <= 20000:
    i = 1
    _count = 0
    while i <= num:
        if num % i == 0:
            if _count > 2:
                break
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
