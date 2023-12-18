class Cat:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("获取方法执行了")
        return self._name

    @name.setter
    def name(self, name):
        print("设置方法执行了")
        self._name = name

    def meow(self):
        print(f'大家好,我是{self._name}')


cat = Cat('喵喵喵')
cat.name = '李四'
cat.name
cat.meow()
'''
设置方法执行了
获取方法执行了
大家好,我是李四
'''