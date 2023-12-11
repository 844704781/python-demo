def mul(a=10, b=11, c=12):
    print("a=", a)
    print("b=", b)
    print("c=", c)
    print(a * b * c)


mul(1, 2, 3)
'''
a= 1
b= 2
c= 3
6
'''

mul(1)
'''
a= 1
b= 11
c= 12
132
'''


def mul(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)
    print(a * b * c)


mul(a=10, c=20, b=30)


def mul(a, b):
    print("a=", a)
    print("b=", b)
    print(a * b)


mul(1, b=2)
mul(1, a=1) #TypeError: mul() got multiple values for argument 'a'
