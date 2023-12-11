a = 0
a=not a
print(a) #True

print(1 and 2) # 2
print(3 and 555) #555
print(not '222' or 'c') #c

True and print('hello world') #hello world

# and
# True and True
print(2 and 3) # 3
# True and False
print(2 and 0) # 0
# False and True
print(None and '张三') # None
# False and False
print(0 and '') # 0

# or
# True or True
print(1 or 2) #1
# True or False
print('ss' or None) #ss
# False or True
print('' or 123) # 123
# False or False
print('' or 0)#0