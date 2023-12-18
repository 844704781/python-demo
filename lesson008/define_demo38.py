my_tuple = (1, 2, 4, 5, '1', '100', '2', '28')
result = sorted(my_tuple, key=int)
print(result)  # [1, '1', 2, '2', 4, 5, '28', '100']
print(type(result))  # <class 'list'>

s = 'helloworld'
result = sorted(s)
print(result)  # ['d', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
print(''.join(result))  # dehllloorw
