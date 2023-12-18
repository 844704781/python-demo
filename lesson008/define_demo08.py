def fn4(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


t = (1, 2, 3)
fn4(*t)
'''
a= 1
b= 2
c= 3
'''
t = [1, 2, 3]
fn4(*t)
'''
a= 1
b= 2
c= 3
'''
fn4(t)  # TypeError: fn4() missing 2 required positional arguments: 'b' and 'c'
