import pprint


def to_sparse_array(two_d_array: list) -> list:
    '''
    二维数组转稀疏数组
    :return: 稀疏数组
    '''

    # 获取不需要压缩的值的个数max
    _sum = 0
    for row in two_d_array:
        for meta in row:
            if meta != 0:
                _sum += 1

    # 定义稀疏数组，设置第一行的值
    sparse_array = [[len(two_d_array), len(two_d_array[0]), _sum]]

    # 遍历二维数组，将非0的值记录到稀疏数组中
    for i, row in enumerate(two_d_array):
        for j, meta in enumerate(row):
            if meta != 0:
                sparse_array.append([i, j, meta])

    return sparse_array


def to2D_array(sparse_array: list) -> list:
    '''
    稀疏数组转二维数组
    :param sparse_array: 稀疏数组
    :return: 二维数组
    '''

    # 创建二维数组
    two_d_array = [[0] * sparse_array[0][0] for _ in range(sparse_array[0][1])]
    # 将稀疏数组的值设置到二维数组中
    for index, row in enumerate(sparse_array):
        if index == 0:
            continue
        two_d_array[row[0]][row[1]] = row[2]

    return two_d_array


two_d_array = [[0] * 11 for _ in range(11)]
two_d_array[1][2] = 1
two_d_array[2][3] = 2
two_d_array[5][6] = 22
# 二维转稀疏
sparse_array = to_sparse_array(two_d_array)
pprint.pprint(sparse_array)
# 稀疏转二维
_two_d_array = to2D_array(sparse_array)
pprint.pprint(_two_d_array)
