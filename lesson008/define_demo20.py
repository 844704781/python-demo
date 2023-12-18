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

data = [1, 2, 3, 5, 4, 1, 2, 3, 2, 1, 2, 3, 4]
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
            if len(meta) <= 3:
                '''
                    如果为2
                    则复制一份meta为copy_meta
                    copy_meta增加最后一个元素,变成长度为3
                    将copy_meta放到result列表中
                    此时meta还是2个元素
                '''
                if len(meta) == 2:
                    copy_meta = meta.copy()
                    copy_meta.append(v2)
                    result.append(copy_meta)
                else:
                    meta.append(v2)
                    '''
                     判断[1,2,x]是否结束
                    '''
        j += 1
    i += 1
print(result)

# all = []
# for meta in result:
#     # meta =[1,2,3]
#     i = 0
#     while i < len(meta):
#         v1 = meta[i]
#         m = [v1]
#         j = i + 1
#         if j == len(meta):
#             j = 0
#         while j < len(meta):
#             if i == j:
#                 break
#
#             v2 = meta[j]
#             if len(m) < 3:
#                 m.append(v2)
#                 if len(m) == 3:
#                     all.append(m)
#
#             j += 1
#             if j == len(meta):
#                 j = 0
#         i += 1
# print(all)
# print(len(all))
