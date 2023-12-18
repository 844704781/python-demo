# 需求:要求将在函数执行前打印程序开始执行，函数执行完毕后打印程序结束执行
def my_decorator(func):
    def do(*x, **y):
        print("程序开始执行")
        r = func(*x, **y)
        print("程序结束执行")
        return r

    return do


def my_decorator2(func):
    def do(*x, **y):
        print("程序2开始执行")
        r = func(*x, **y)
        print("程序2结束执行")
        return r

    return do


# 装饰器的引入
@my_decorator
@my_decorator2
def add(x, y):
    return x + y


@my_decorator
def mul(x, y):
    return x * y


@my_decorator
def hello():
    print('hello')


r = add(1, 2)
print(r)
'''
程序开始执行
程序2开始执行
程序2结束执行
程序结束执行
3
'''

r = mul(1, 2)
print(r)
'''
程序开始执行
程序结束执行
2
'''

r = hello()
print(r)
'''
程序开始执行
hello
程序结束执行
None
'''
