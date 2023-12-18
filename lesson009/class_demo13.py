class Animal:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def sleep(self):
        print("动物睡觉")

    def run(self):
        print("动物跑")


class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name)
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def bark(self):
        print("狗叫")


dog = Dog('旺财', 18)
print(dog.name)  # 旺财
print(dog.age)  # 18
