numbers = range(6)
print(numbers)  # range(0, 6)
print(list(numbers))  # [0, 1, 2, 3, 4, 5]
print(list(range(3, 7)))  # [3, 4, 5, 6]
print(list(range(2, 10, 2)))  # [2, 4, 6, 8]

for i in range(10):
    if i == 5:
        continue
    if i == 8:
        break
    print(i, end="")
else:
    print("执行完毕")
##0123467
