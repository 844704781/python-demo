class Person:
    name = 'wjh'

    def say_hello(self):
        print("你好!%s" % self.name)  # 直接使用时报错：NameError: name 'name' is not defined. Did you mean: 'self.name'?


p1 = Person()
p1.name = 'laimin'
p1.say_hello()  # 你好!laimin

p2 = Person()
p2.name = 'miaomiaomiao'
p2.say_hello()  # 你好!miaomiaomiao

p3 = Person()
p3.say_hello()  # 你好!wjh
