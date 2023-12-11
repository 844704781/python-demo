for i in range(10):
    if i == 5:
        continue
    if i == 8:
        break
    print(i, end="")
else:
    print("执行完毕")