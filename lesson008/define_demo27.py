'''
创建一个函数power来为任意数字做幂运算n**i

结束条件:
  i == 0
    return;
递归公式：
2**8-->2 *2 *2  *2  *2  *2  *2  *2
  n*f(n,i-1)
'''


def power(n, i):
    if i == 1:
        return 2
    return n * pow(n, i - 1)


print(power(2, 10))
