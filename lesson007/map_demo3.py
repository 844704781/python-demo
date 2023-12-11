words = {'a': 1, 'b': 2,
         'c': 3, 'd': 4,
         'e': 5, 'f': 6, 'g': 7}
del words['a']
print(words)  # {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

# del words['h'] #KeyError: 'h'
print(words)

words = {'a': 1, 'b': 2,
         'c': 3}
print(words)  # {'a': 1, 'b': 2, 'c': 3}
item = words.popitem()
print(item)  # ('c', 3)
print(words)  # {'a': 1, 'b': 2}
words.popitem()
words.popitem()
# words.popitem() #KeyError: 'popitem(): dictionary is empty'

# 正常删除
words = {'a': 1, 'b': 2,
         'c': 3}
value = words.pop('a')
print(value)  # 1
print(words)  # {'b': 2, 'c': 3}

# 删除存在key，指定default
words = {'a': 1, 'b': 2,
         'c': 3}
value = words.pop('b', 111)
print(value)  # 2
print(words)  # {'a': 1, 'c': 3}

# 删除不存在key,指定default
words = {'a': 1, 'b': 2,
         'c': 3}
value = words.pop('g', 2222)
print(value)  # 2222
print(words)  # {'a': 1, 'b': 2, 'c': 3}

# 删除不存在key,未指定default
words = {'a': 1, 'b': 2,
         'c': 3}
#value = words.pop('h')  # KeyError: 'h'

words = {'a': 1, 'b': 2,
         'c': 3, 'd': 4,
         'e': 5, 'f': 6, 'g': 7}
words.clear()
print(words) #{}
