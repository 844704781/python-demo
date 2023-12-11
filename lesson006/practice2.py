'''
编写一个程序，检查任意一个年份是否是闰年。
   如果一个年份可以被4整除不能被100整除，或者可以被400整除，这个年份就是闰年。

'''

year = input("请输入年份:")
year = int(year)
condition01 = year % 4 == 0 and year % 100 != 0
condition02 = year % 400 == 0
if condition01 or condition02:
    print("这是闰年")
else:
    print("这是平年")
print("按Enter结束程序")
