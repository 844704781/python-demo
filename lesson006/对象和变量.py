a = 123
b = a
print(id(a)) #140715606595832
print(id(b)) #140715606595832
a =345
print(id(a)) #2211088695728
print(id(b)) #140715606595832
user1 ={"name":"张三","age":12}
user2 = user1
print(id(user1)) #2046136516672
print(id(user2)) #2046136516672
user1['name'] = '李四'
print(user1)#{'name': '李四', 'age': 12}
print(user2)#{'name': '李四', 'age': 12}
print(id(user1)) #2046136516672
print(id(user2)) #2046136516672
user1={'name': '李四', 'age': 12}
print(id(user1)) #3180781599680
print(id(user2)) #3180781666368
print(user1,user2) #{'name': '李四', 'age': 12} {'name': '李四', 'age': 12}
