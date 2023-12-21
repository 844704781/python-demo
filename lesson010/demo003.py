class MyError(Exception):
    pass


def division(a, b):
    if b == 0:
        raise MyError("除数不能是0")
    return a / b


try:
    division(10, 0)
except MyError as e:
    print("出错啦", e)
# 出错啦 除数不能是0
