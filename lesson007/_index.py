_list = [2, 3, 4, 5, 6, 3, 2, 4, 8, 3, 12, 34, 67, 8, 12, 4, 6]
target = 8
start = 0
end = len(_list) - 1

_index = None

i = 0
while i < len(_list):
    if start <= i < end:
        current = _list[i]
        if current == target:
            _index = i
            break
    i += 1
print("index:", _index)
