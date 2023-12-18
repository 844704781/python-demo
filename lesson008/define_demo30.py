a = 30

print("刚开始声明时a的id", id(a), "a=", a)


def fn2():
    # 使用global关键字表示引用外部作用域的变量a
    global a
    # a = 20  # 修改的是外部作用域的a
    print("函数内部的a的id", id(a), "a=", a)

# del a
fn2()
print("函数外部的a的id", id(a), "a=", a)
