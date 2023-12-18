class Animal:

    def sleep(self):
        print("动物睡觉")

    def run(self):
        print("动物跑")


class Dog(Animal):
    def bark(self):
        print("狗叫")


print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False
print(isinstance(Dog, object))  # True
print(isinstance(Animal, object))  # True

dog = Dog()
dog.bark()  # 狗叫
dog.run()  # 动物跑
dog.sleep()  # 动物睡觉

print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True
print(isinstance(dog, object))  # True
