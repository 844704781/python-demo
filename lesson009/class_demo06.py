class Person:

    print("我是代码块")
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("你好!%s" % self.name)  # 直接使用时报错：NameError: name 'name' is not defined. Did you mean: 'self.name'?


# p1 = Person() #TypeError: Person.__init__() missing 1 required positional argument: 'name'

p1 = Person("张三")
p1.say_hello()  # 你好!张三
p2 = Person("李四")
p2.say_hello()  # 你好!李四
'''
我是代码块
你好!张三
你好!李四
'''