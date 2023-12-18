_list = [1, 2, 3]
'''
1,2,3
1,3,2
2,1,3
2,3,1
3,1,2
3,2,1
'''
i = 0
result = []
while i < len(_list):
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

print(result)
