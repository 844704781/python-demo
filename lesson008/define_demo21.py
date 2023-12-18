# _list = [1, 2, 3, 4]
# _result = []
# for index, value in enumerate(_list):
#     copy_list = _list.copy()
#     copy_list.pop(index)
#     _result.append(copy_list)
#
# print(_result)

# 3--->1
# 4--->2
# 5--->6

# [
# [1, 2, 3]
# [1, 2, 5]
# [1, 2, 4]
# [2, 3, 5]
# [2, 3, 4]
# [3, 5, 4]
# ]
def combinations(data):
    # data = [1, 2, 3, 5, 4, 1, 2, 3, 2, 1, 2, 3, 4]
    # 去重复
    _list = []
    for value in data:
        if value not in _list:
            _list.append(value)

    result = []
    i = 0
    while i < len(_list):

        v1 = _list[i]
        meta = [v1]
        # 1
        j = i + 1
        while j < len(_list):
            v2 = _list[j]
            if v2 not in meta:
                # [1,2,x]
                meta.append(v2)
                k = j + 1
                while k < len(_list):
                    v3 = _list[k]
                    if v3 not in meta:
                        copy_meta = meta.copy()
                        copy_meta.append(v3)
                        result.append(copy_meta)
                    k += 1
                else:
                    meta.pop()
            j += 1
        i += 1
    return result


def permutations(_collections):
    result = []
    for _list in _collections:
        '''
        排列
        1,2,3
        1,3,2
        2,1,3
        2,3,1
        3,1,2
        3,2,1
        '''
        i = 0
        while i < len(_list):
            print("-----")
            v1 = _list[i]  # 2

            j = 0
            meta = [v1]
            while j < len(_list):
                v2 = _list[j]  # 1 或者 #3
                if v2 not in meta:
                    meta.append(v2)
                else:
                    j += 1
                    continue

                k = 0
                while k < len(_list):
                    v3 = _list[k]
                    if v3 not in meta:
                        _meta = meta.copy()
                        _meta.append(v3)
                        result.append(_meta)
                    else:
                        k += 1
                        continue
                    k += 1
                else:
                    meta.pop()
                j += 1
            else:
                meta.pop()
            i += 1

    return result


result = combinations([1, 2, 3, 4, 5,6])
all = permutations(result)
print("组合的长度:", len(result))
print("排列的长度:", len(all))
print("组合:", result)
print("排列:", all)
