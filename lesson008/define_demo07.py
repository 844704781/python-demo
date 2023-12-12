# def sum(*a):
#     print("a:", a)
#     print("a:", type(a))
#     sum = 0
#     for value in a:
#         sum += value
#     print("sum=", sum)
#
#
# sum(1, 2, 3, 4, 5, 6, 7, 8, 9)

# *a 会接受所有的位置实参，并且会将这些实参统一保存到一个元组中（包装）
# def fn(*a):
#     print("a=", a, type(a))
#
#
# fn(1, 2, 3, 4, 5, 6)
'''
a= (1, 2, 3, 4, 5, 6) <class 'tuple'>
'''

# 第一个参数给a，第二个参数给b，剩下的都保存到c的元组中
# def fn2(a, b, *c):
#     print('a=', a)
#     print('b=', b)
#     print('c=', c)


'''
a= 1
b= 2
c= (3, 4, 5, 6, 7, 8, 9)
'''

# fn2(1, 2, 3, 4, 5, 6, 7, 8, 9)

# def fn2(a, *b, c):
#     print('a=', a)
#     print('b=', b)
#     print('c=', c)
#
#
# fn2(1, 2, 3, 4, c=5)
# '''
# a= 1
# b= (2, 3, 4)
# c= 5
# '''
# # 这样传会报错:TypeError: fn2() missing 1 required keyword-only argument: 'c'
# fn2(1, 2, 3, 4, 5)


# 所有的位置参数都给a,b和c必须使用关键字参数
# def fn2(*a, b, c):
#     print('a=', a)
#     print('b=', b)
#     print('c=', c)
#
#
# fn2(1, 2, 3, b=1, c=2)
'''
a= (1, 2, 3)
b= 1
c= 2
'''

# 如果在形参的开头直接写一个*，则要求我们的所有的参数必须以关键字参数的形式传递
# def fn2(*, a, b, c):
#     print('a=', a)
#     print('b=', b)
#     print('c=', c)


# fn2(a=1, b=2, c=3)
'''
a= 1
b= 2
c= 3
'''

# fn2(1, 2, 3)  # TypeError: fn2() takes 0 positional arguments but 3 were given

# 形参只能接收位置参数，而不能接收关键字参数
# def fn3(*a):
#     print('a=', a)


# fn3(1, 2, 3, 4, 5)
'''
a= (1, 2, 3, 4, 5)
'''


# fn3(a=1)  # TypeError: fn3() got an unexpected keyword argument 'a'


def fn3(b, c, **a):
    print('a=', a, type(a))


fn3(1, 2, a=3, g=4)
fn3(1, 2, a=3, b=4) #TypeError: fn3() got multiple values for argument 'b'
