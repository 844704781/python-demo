# 装饰器的引入
def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def hello():
    print('hello')


# 需求:要求将在函数执行前打印程序开始执行，函数执行完毕后打印程序结束执行
def my_decorator(func):
    def do(*x, **y):
        print("程序开始执行")
        r = func(*x, **y)
        print("程序结束执行")
        return r

    return do


my_decorator_do = my_decorator(mul)
r = my_decorator_do(2, 3)
print(r)
'''
程序开始执行
程序结束执行
6
'''

my_decorator_do = my_decorator(add)
r = my_decorator_do(2, 3)
print(r)
'''
程序开始执行
程序结束执行
5
'''

my_decorator_do = my_decorator(hello)
r = my_decorator_do()
print(r)
'''
程序开始执行
hello
程序结束执行
None
'''
