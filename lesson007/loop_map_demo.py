words = {'a': 1, 'b': 2,
         'c': 3, 'd': 4,
         'e': 5, 'f': 6, 'g': 7}
items = words.items()  # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7)])
print(items)
for key, value in items:
    print(f'key:{key},value:{value}')
# key:a,value:1
# key:b,value:2
# key:c,value:3
# key:d,value:4
# key:e,value:5
# key:f,value:6
# key:g,value:7


# values = words.values()
# print(values)  # dict_values([1, 2, 3, 4, 5, 6, 7])
# for value in values:
#     print(value)

# keys = words.keys()
# print(keys) #dict_keys(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
# for key in keys:
#     print(words[key])
