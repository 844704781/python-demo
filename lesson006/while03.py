# 水仙花是指一个n位数(n>=3)，它的每个位上的数字的n次幂之和等于它本身
# (例如:`1**3+5**3+3**3=153`)
# 求1000以内所有的水仙花数
i = 1
while i <= 1000:
    str_i = str(i)

    if len(str_i) == 3:
        one = i // 100
        two = (i - one * 100) // 10
        three = i - (one * 100 + two * 10)
        if one ** 3 + two ** 3 + three ** 3 == i:
            print(f"{one}**3+{two}**3+{three}**3={i}")
    i += 1

