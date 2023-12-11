print('语句1') if True else print('条件2')

'''
现在有a,b,c三个变量，三个变量中分别保存有三个值
现在通过条件运算符获取三个值的最大值
'''
a = 1
b = 2
c = 3
max = a if (a > b) else b
max = c if (c > max) else max
print(max)  # 3
