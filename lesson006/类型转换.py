a = True
a = int(a)

print(a) #1

a = 12.222
a= int(a)
print(a) #12

a= '123'
a= int(a)
print(a) #123

a='123.11'
#a= int(a) #ValueError: invalid literal for int() with base 10: '123.11'

a = None
#a = int(a)#TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'


a=True
a=float(a)
print(a)#1.0

a=False
a=float(a)
print(a)#0.0

a='123.011'
a=float(a)
print(a)#123.011

a='12312.ss'
#a=float(a) #ValueError: could not convert string to float: '12312.ss'

a = None
#a=float(a) #TypeError: float() argument must be a string or a real number, not 'NoneType'


b=123
b=str(b)
print('b=',b)#b= 123
print('type=',type(b))#type= <class 'str'>

b=True
b=str(b)
print('b=',b)#b= True
print('type=',type(b))#type= <class 'str'>

b=None
b=str(b)
print('b=',b)#b= None
print('type=',type(b))#type= <class 'str'>


c='12321'
c=bool(c)
print('c=',c) # c= True
print('type=',type(c)) #type= <class 'bool'>

c=''
c=bool(c)
print('c=',c) # c= False
print('type=',type(c)) #type= <class 'bool'>

c=None
c=bool(c)
print('c=',c) # c= False
print('type=',type(c)) #type= <class 'bool'>

c=0
c=bool(c)
print('c=',c) # c= False
print('type=',type(c)) #type= <class 'bool'>

c='0'
c=bool(c)
print('c=',c) # c= True
print('type=',type(c)) #type= <class 'bool'>



