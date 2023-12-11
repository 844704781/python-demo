# 获取用户输入的任意数，判断其是否是质数
num = int(input("请输入任意一个整数："))
i = 1
_count = 0
while i <= num:
    if num % i == 0:
        _count += 1
    i += 1
else:
    if _count == 2:
        print("这是一个质数")
    else:
        print("这是一个合数")
