i = 0
while i < 9:
    j = 0
    while j <= i:
        print(f"{i + 1}*{j + 1}={(i + 1) * (j + 1)} ", end='')
        j += 1
    i += 1
    print()

num = 2
while num <= 100:
    i = 1
    _count = 0
    while i <= num:
        if num % i == 0:
            _count += 1
        i += 1
    else:
        if _count == 2:
            print(f"{num}是质数")
        # else:
        #     print(f"{num}是合数")
    num += 1
