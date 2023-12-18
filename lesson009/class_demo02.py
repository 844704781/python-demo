# 定义一个类
class Dog:
    pass


# 直接打印类
print(Dog)  # <class '__main__.Dog'>

# 创建类的对象/类的实例化
dog1 = Dog()

print(isinstance(dog1, Dog)) #True
print(isinstance(dog1, str)) #False
print(isinstance(dog1, int)) #False

dog2 = Dog()
dog3 = Dog()
print(dog1, id(dog1), type(dog1))  # <__main__.Dog object at 0x00000192A4187E60> 1729329921632 <class '__main__.Dog'>
print(dog2, id(dog2), type(dog2))  # <__main__.Dog object at 0x00000192A4187DD0> 1729329921488 <class '__main__.Dog'>
print(dog3, id(dog3), type(dog3))  # <__main__.Dog object at 0x00000192A4187E00> 1729329921536 <class '__main__.Dog'>

