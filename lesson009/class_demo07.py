class Cat:

    def __init__(self, name, age, gender, color):
        self.name = name
        self.age = age
        self.gender = gender
        self.color = color
        print(f"大家好，我是{self.name},我的年龄是{self.age},我的性别是{self.gender},我的颜色是{self.color}")

    def catch_mouse(self):
        print("我在抓老鼠")

    def eat(self):
        print("我在吃喵喵粮")

    def meow(self):
        print("喵~喵~喵~喵~喵~")


cat = Cat('喵喵喵', 3, '女', '橘色')
cat.catch_mouse()
cat.eat()
cat.meow()
'''
大家好，我是喵喵喵,我的年龄是3,我的性别是女,我的颜色是橘色
我在抓老鼠
我在吃喵喵粮
喵~喵~喵~喵~喵~
'''
