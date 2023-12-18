a = [30]

print("刚开始声明时a的id", id(a), "a=", a)


def fn2():
    global a
    a =[30]
    print("函数内部的a的id", id(a), "a=", a)

a = None
fn2()
print("函数外部的a的id", id(a), "a=", a)
'''
为局部变量赋值时:
刚开始声明时a的id 140715048488280 a= 30
函数内部的a的id 140715048487960 a= 20
函数外部的a的id 140715048488280 a= 30
'''

print(id(None))