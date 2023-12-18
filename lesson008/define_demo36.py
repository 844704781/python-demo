_list = [1, "2", 3, 2, 5, "3", 7, "1", 5, 10]
# _list.sort()#TypeError: '<' not supported between instances of 'str' and 'int'
_list.sort(key=int)  # 将每个元素转成int再比较

print(_list)  # [1, '1', '2', 2, 3, '3', 5, 5, 7, 10]

_list.sort(key=str)  # 将每个元素转成字符再比较
print(_list)  # [1, '1', 10, '2', 2, 3, '3', 5, 5, 7]

_list = ["abc:", "2", "324s", "hello", "ko", "3", 's', "1", "android", "apple"]
_list.sort(key=len)
print(_list)  # ['2', '3', 's', '1', 'ko', 'abc:', '324s', 'hello', 'apple', 'android']
