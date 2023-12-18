def sum(*nums):
    _sum = 0
    for num in nums:
        _sum += num
    return _sum


_sum = sum(1, 2, 3, 4, 6, 2, 1)
print(_sum)


def animal():
    def cat():
        return "I am cat"

    return cat


str = animal()
print(str)  # <function animal.<locals>.cat at 0x000002AD14D4BCE0>
print(str())  # I am cat


def fun3():
    print("hello")
    return


def fun4():
    print("hello")


print(fun3())  # None
print(fun4())  # None


def fun5():
    return
    print("hello")  # 不会执行


fun5()


def fun6():
    for i in range(5):
        if i == 3:
            break
        print("i=", i)
    print("循环结束啦")

print(fun6())
'''
i= 0
i= 1
i= 2
循环结束啦
None
'''

def fun7():
    for i in range(5):
        if i == 3:
            return i
        print("i=", i)
    print("循环结束啦")

print(fun7())
'''
i= 0
i= 1
i= 2
3
'''

def fun8():
    return 10

print(fun8) #<function fun8 at 0x0000018A0655F600>
print(fun8()) #10
