def fn4(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


a = {'a': 1000, 'b': 1, 'c': 3}
fn4(**a)
'''
a= 1000
b= 1
c= 3
'''

a = {'a': 1000, 'b': 1}
fn4(**a)  # TypeError: fn4() missing 1 required positional argument: 'c'

a = {'a': 1000, 'b': 1, 'd': 3}
# fn4(**a)#TypeError: fn4() got an unexpected keyword argument 'd'
