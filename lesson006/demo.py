num = 0
_sum = 0
while num < 100:
    num += 1
    # print(f"num:{num}")
    if int(num) % 2 == 0:
        print(f"{num}偶数")
    else:
        print(f"{num}奇数")
        _sum+=num
else:
    print(f"sum:{_sum}")


