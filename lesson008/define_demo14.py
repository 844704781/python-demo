b = 20


def fn():
    # 定义在函数内部，所以他的作用域就是函数内部，函数外部无法访问
    a = 10

    print("函数内部:", 'a=', a)
    print("函数内部:", 'b=', b)


fn()
print('函数外部:', 'b=', b)
print('函数外部:', 'a=', a)  # NameError: name 'a' is not defined
