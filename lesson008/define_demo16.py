a = 30

print("刚开始声明时a的id", id(a), "a=", a)


def fn2():
    # 声明在函数内部使用的a是全局变量，此时再去修改a时，就是在修改全局的a
    global a
    a = 20
    print("函数内部的a的id", id(a), "a=", a)


fn2()
print("函数外部的a的id", id(a), "a=", a)
'''
为局部变量赋值时:
刚开始声明时a的id 140715531685208 a= 30
函数内部的a的id 140715531684888 a= 20
函数外部的a的id 140715531684888 a= 20
'''