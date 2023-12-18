# 定义一个类
class Dog:
    pass


print(Dog, id(Dog), type(Dog))  # <class '__main__.Dog'> 2123576889728 <class 'type'>
# Dog其实是type类型的对象，定义类其实就是使用Dog这个变量接收了一个type类型的对象
# 我们可以给Dog这个变量重新赋值
Dog = 1
print(Dog, id(Dog), type(Dog))  # 1 140715510843832 <class 'int'>
