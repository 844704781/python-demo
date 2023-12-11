'''
编写一个程序，获取一个用户输入的整数。然后通过程序显示这个数是奇数还是偶数。
'''
number = input("请输入一个整数:")
number = int(number)
if number % 2 == 0:
    print("这是偶数")
else:
    print("这是奇数")
input("按Enter结束程序")
