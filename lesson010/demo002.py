def division(a, b):
    if b == 0:
        raise Exception("除数不能是0")
    return a / b


division(10, 0)
#Exception: 除数不能是0
