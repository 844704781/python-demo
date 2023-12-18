# 斐波那契数列是指这样一个数列：1，1，2，3，5，8，13，21，34，55，89……这个数
# 列从第3项开始 ，每一项都等于前两项之和。
# 请打印n位斐波那契数列
from time import *

n = int(input('请输入要打印的多个斐波那契数列(n>=3):'))
start = time()
if n < 3:
    print("非法数字")
else:
    i = 0
    _list = [1, 1]
    while i < n - 2:
        # n == 3, i==0
        _sum = _list[i] + _list[i + 1]
        _list.append(_sum)
        i += 1

    print(_list)
end = time()
print(str(end - start) + "s")
