d = {}  # 创建字段
print(d, type(d))  # {} <class 'dict'>

_map = {
    "name": "张三",
    10: "我的key是int",
    (2, 3): "我的key是tuple",
    True: "我的key是布尔值"
}

print(_map)  # {'name': '张三',# 10: '我的key是int', (2, 3): '我的key是tuple', True: '我的key是布尔值'}
print(_map[10])  # 我的key是int
print(_map[(2, 3)])  # 我的key是tuple
print(_map[True])  # 我的key是布尔值
print(_map["name"])  # 张三

_map = {
    "name": "张三",
    "name": "李四"
}
print(_map)  # {'name': '李四'}

user = {
    "name": "张三",
    "age": 12
}

# print(user['gender'])  # KeyError: 'gender'
