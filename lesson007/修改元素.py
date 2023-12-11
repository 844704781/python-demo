people = ['孙悟空', '猪八戒', '沙和尚',
          '唐僧', '蜘蛛精', '白骨精']
print("修改前:", people)  # 修改前: ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']
people[0] = 'sunwukong'
print("修改后:", people)  # 修改后: ['sunwukong', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']
# people[6] = 'xxx' #IndexError: list assignment index out of range

people = ['孙悟空', '猪八戒', '沙和尚',
          '唐僧', '蜘蛛精', '白骨精']
print("修改前:", people)  # 修改前: ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']
del people[0]
print("修改后:", people)  # 修改后: ['猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']

people = ['孙悟空', '猪八戒', '沙和尚',
          '唐僧', '蜘蛛精', '白骨精']

meta = people[3]
print('people[3]=', meta)  # people[3]= 唐僧

people = ['孙悟空', '猪八戒', '沙和尚',
          '唐僧', '蜘蛛精', '白骨精']

people[0:2] = ['牛魔王', '红孩儿']
print(people)  # ['牛魔王', '红孩儿', '沙和尚', '唐僧', '蜘蛛精', '白骨精']
people[0:2] = ['牛魔王', '红孩儿', '铁扇公主']
print(people)  # ['牛魔王', '红孩儿', '铁扇公主', '沙和尚', '唐僧', '蜘蛛精', '白骨精']

people = ['孙悟空', '猪八戒', '沙和尚',
          '唐僧', '蜘蛛精', '白骨精']
people[0:0] = ['菩提祖师', '太白金星']
print(people)  # ['菩提祖师', '太白金星', '孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']

people = ['孙悟空', '猪八戒', '沙和尚',
          '唐僧', '蜘蛛精', '白骨精']
people[0:1] = "swk"
print(people)  # ['s', 'w', 'k', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']
# people[0:1] = 11  # TypeError: can only assign an iterable

people = ['孙悟空', '猪八戒', '沙和尚',
          '唐僧', '蜘蛛精', '白骨精']
new_people = people[::2] = ['张三', '李四', '王老五']
print(people)  # ['张三', '猪八戒', '李四', '唐僧', '王老五', '白骨精']
print(new_people)  # ['张三', '李四', '王老五']
# people[::2] =['张三']  #ValueError: attempt to assign sequence of size 1 to extended slice of size 3

people = ['孙悟空', '猪八戒', '沙和尚',
          '唐僧', '蜘蛛精', '白骨精']
del people[0:2]
print(people)  # ['沙和尚', '唐僧', '蜘蛛精', '白骨精']

people = ['孙悟空', '猪八戒', '沙和尚',
          '唐僧', '蜘蛛精', '白骨精']
del people[::2]
print(people)  # ['猪八戒', '唐僧', '白骨精']

str = 'sunwukong'
print(str[2])  # n
s = str[::2]
print(s)  # snuog
str[0] = '1'  # TypeError: 'str' object does not support item assignment
str[::2] = ['a'] * 5  # TypeError: 'str' object does not support item assignment
