class Cat:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def meow(self):
        print(f'大家好,我是{self.__name}')


cat = Cat('喵喵喵')
cat._Cat__name = '张三'
cat.meow()
print(cat.get_name())
#print(cat.__name) #AttributeError: 'Cat' object has no attribute '__name'

'''
大家好,我是张三
张三
'''
