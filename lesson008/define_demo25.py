# 斐波那契数列是指这样一个数列：1，1，2，3，5，8，13，21，34，55，89……这个数
# 列从第3项开始 ，每一项都等于前两项之和。
# 请打印n位斐波那契数列
n = 100


def fib(n):
    a = 1
    b = 1
    if n < 3:
        print("无效的位数")
    else:
        i = 2
        while i < n:
            value = a + b
            a = b
            b = value
            i += 1
    # 354224848179261915075
    return n


print(fib(100))

