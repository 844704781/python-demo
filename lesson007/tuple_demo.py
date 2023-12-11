my_tuple = ()  # 创建了一个空元组
print(my_tuple)  # ()
print(type(my_tuple))  # <class 'tuple'>

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # (1, 2, 3, 4, 5)
print(my_tuple[3])  # 4
# my_tuple[0] = 1 #TypeError: 'tuple' object does not support item assignment
my_tuple = 1, 2, 3, 4, 5
print(my_tuple)  # (1, 2, 3, 4, 5)
my_tuple = 4,
print(my_tuple)  # (4,)

# 解包
my_tuple = 10, 20, 30, 40
a, b, c, d = my_tuple
print("a=", a)  # a= 10
print("b=", b)  # b= 20
print("c=", c)  # c= 30
print("d=", d)  # d= 40

a, b = 5, 2
a, b = b, a
print(a, b)  # 2 5

a, b, c, d = 10, 20, 30, 40
print(a, b, c, d)  # 10 20 30 40
# a, b = 10, 20, 30, 40  # ValueError: too many values to unpack (expected 2)
my_tuple = 10, 20, 30, 40
a, *b = my_tuple
print(a, b)  # 10 [20, 30, 40]
*a, b = my_tuple
print(a, b)  # [10, 20, 30] 40
a, *b, c = my_tuple
print(a, b, c)  # 10 [20, 30] 40
my_tuple = 10, 20, 30, 40, 50
# a, *b, *c, d = my_tuple #SyntaxError: multiple starred expressions in assignment

my_tuple = (0, 1, 2, 3, 4, 5, 1)
t1 = my_tuple[1:3]
print(t1)  # (1, 2)
print(my_tuple.count(1))
