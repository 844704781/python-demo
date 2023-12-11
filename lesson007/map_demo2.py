# user = dict(name='孙悟空', age=17, gender='男')
# print(user, type(user))#{'name': '孙悟空', 'age': 17, 'gender': '男'} <class 'dict'>
#
# a = [1, 2, [3, 1, 2], 2, 3]
# print(len(a)) #5
# print(a[2]) #[3, 1, 2]

user = dict([('name', '孙悟空'), ('age', 18)])
print(user, type(user))
# {'name': '孙悟空', 'age': 18} <class 'dict'>

user = {'name': '张三', 'age': 18}
print(len(user))  # 2

user = {'name': '张三', 'age': 18}
print('name' in user)  # True
print('gender' not in user)  # True

user = {'name': '张三', 'age': 18}
print(user['name'])  # 张三
age = 'age'
print(user[age])  # 18

user = {'name': '张三', 'age': 18}
print(user.get("name"))  # 张三
print(user.get("gender"))  # None
print(user.get("gender", "男"))  # 男

user = {'name': '张三', 'age': 18}
user['name'] = '李四'
print(user)  # {'name': '李四', 'age': 18}
user['gender'] = '男'
print(user)  # {'name': '李四', 'age': 18, 'gender': '男'}

user = {'name': '张三', 'age': 18}
value = user.setdefault('name', '李四')
print(user)  # {'name': '张三', 'age': 18}
print(value)  # 张三
value = user.setdefault('gender', '男')
print(user)  # {'name': '张三', 'age': 18, 'gender': '男'}
print(value)  # 男

map1 = {"a": 1, "b": 2, "c": 3}
map2 = {"a": 2, "d": 3, "e": 4}
map1.update(map2)
print(map1)  # {'a': 2, 'b': 2, 'c': 3, 'd': 3, 'e': 4}
print(map2)  # {'a': 2, 'd': 3, 'e': 4}
