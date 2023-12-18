class Cat:

    def __init__(self, name):
        self.hidden_name = name

    def get_name(self):
        return self.hidden_name

    def set_name(self, name):
        self.hidden_name = name

    def meow(self):
        print(f'大家好,我是{self.hidden_name}')


cat = Cat('喵喵喵')
cat.set_name('张三')
cat.meow()
print(cat.get_name())

'''
大家好,我是张三
张三
'''
