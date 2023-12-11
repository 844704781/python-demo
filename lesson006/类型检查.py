a =123
b= '123'
print('a=',a)
print('b=',b)
'''
a= 123
b= 123
'''

c = type('123')
print(c) # <class 'str'>
d = type(a)
print(d) # <class 'int'>
e = type(b)
print(e) # <class 'str'>

print(type(1)) # <class 'int'>
print(type(1.4)) # <class 'float'>
print(type(True)) # <class 'bool'>
print(type('hello')) # <class 'str'>
print(type(None)) # <class 'NoneType'>
