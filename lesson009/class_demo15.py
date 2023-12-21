class Dog:

    def run(self):
        print("我会跑")

    def __len__(self):
        return 10


class Cat:

    def run(self):
        print("我会跑")


dog = Dog()
cat = Cat()
print(len(dog))  # 10
print(len(cat))  # TypeError: object of type 'Cat' has no len()
