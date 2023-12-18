# def factorial(n: int) -> int:
#     _sum = 1
#     for i in range(1, n + 1):
#         _sum = _sum * i
#     return _sum
#
#
# a = factorial(10)
# print(a)  # 3628800


# def fn():
#     print("从前有座山，山里有座庙，庙里有个老和尚，老和尚在将故事，故事里说:")
#     fn()
#
# fn()


'''
求x的阶乘
x * (x-1) * (x-2) * (x-3) ... * 1
即
x *(x-1) * (x-1-1) * (x-1-1-1) ... * 1

 结束条件
    n == 1
 递归条件
    f(n)=n*f(n-1)
'''


def factorial(n: int) -> int:
    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(10))
