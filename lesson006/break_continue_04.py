from time import *

'''
break优化后:
范围:10000,时间: 0.11440920829772949s
范围:20000,时间: 0.3162860870361328s
范围:100000,时间: 3.0849106311798096s
'''
# 优化前
start = time()
num = 2
_sum = 100
while num <= _sum:

    '''
    判断num是不是质数
    '''
    i = 1
    _count = 0
    while i <= num and _count <= 2 and i <= _sum ** 0.5:
        if num % i == 0:
            if _count > 2:
                break
            _count += 1
        i += 1
    else:
        if _count == 2:
            pass
            print(f"{num}是质数")
        # else:
        #     print(f"{num}是合数")
    num += 1
end = time()
print(f"执行时间{end - start}s")
