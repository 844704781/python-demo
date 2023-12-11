people = ['张三', '李四', '王老五']
print('改变前的people:', people)  # ['张三', '李四', '王老五']
people.append('王富贵')
print('改变后的people:', people)  # ['张三', '李四', '王老五', '王富贵']

people = ['张三', '李四', '王老五']
people.insert(2, '王老六')
print(people)  # ['张三', '李四', '王老六', '王老五']

people = ['张三', '李四', '王老五']
people.extend(['zhangsan', 'lisi', 'wanglaowu'])
print(people)  # ['张三', '李四', '王老五', 'zhangsan', 'lisi', 'wanglaowu']

people = ['张三', '李四', '王老五']
people.clear()
print(people)  # []

people = ['张三', '李四', '王老五']
meta = people.pop()
print(meta)  # 王老五
print(people)  # ['张三', '李四']

people = ['张三', '李四', '王老五', '张三']
people.remove('张三')
print(people)  # ['李四', '王老五', '张三']

people = ['张三', '李四', '王老五']
people.reverse()
print(people)  # ['王老五', '李四', '张三']

people = [4, 5, 61, 32, 4, 3, 4,
          6, 7, 8, 434, 3, 2, 4]
people.sort()
print(people)  # [2, 3, 3, 4, 4, 4, 4, 5, 6, 7, 8, 32, 61, 434]
people.sort(reverse=True)
print(people)  # [434, 61, 32, 8, 7, 6, 5, 4, 4, 4, 4, 3, 3, 2]
