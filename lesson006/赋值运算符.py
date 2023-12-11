a = {'name': '张三'}

b = a

print(b == a) # True
print(b is a) # True
b = {'name': '张三'}
print(b==a) #True
print(b is a) #False


w1='c'
w2='b'
print(w1>w2)#True
w3='cool'
w4='b'
print(w3>w4)#True,和上面结果一致，因为是逐位比较
