_list = [1, 2, 6, 2, 4, 67, 3, 2]
_max = 0
i = 0
while i < len(_list):
    num = _list[i]
    if num > _max:
        _max = num
    i += 1
print(_max)