# 在Python中数值分为三种:整数，浮点，复数
# 在Python中所有的整数都是int类型
a = 10
b = 20
# Python中的整数的大小没有限制，可以是一个无限大的整数
c = 9999999999999999999999999999999999999999999999999999999999
print(c)
# 如果数字的长度过大，可以使用下划线作为分隔符
c = 123456789
print(c)
c = 123_456_789
print(c)  # 123456789

# d = 0123456 十进制的数不能以0开头,编辑器会报错
# 其它进制的整数，只要是数字打印时一定是以十进制的形式显示的
# 二进制 0b开头
c = 0b10  # 二进制的10
# 八进制 0o开头
c = 0o10
# 十六进制 0x开头
c = 0x10
# 也可以通过运算法来对数字进行运算，并且可以保证整数运算的精确
c = -100
c = c + 3
# 浮点数(小数)，在Python中所有小数都是float类型
c = 1.23
c = 4.56

# 对浮点数进行运算时，可能会得到一个不精确的结果
c = 0.1 + 0.2
print(c)
