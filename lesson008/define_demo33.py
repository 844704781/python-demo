def condition1(meta):
    '''
    判断meta是否是奇数
    :param meta:
    :return:
    '''
    return meta % 2 != 0


def condition2(meta):
    '''
    判断meta是否是偶数
    :param meta:
    :return:
    '''
    return meta % 2 == 0


def condition3(meta):
    '''
    判断meta是否大于5
    :param meta:
    :return:
    '''
    return meta > 5


def condition4(meta):
    '''
    判断meta是否大于2小于5
    :param meta:
    :return:
    '''
    return 2 < meta < 5


params = [2, 3, 5, 6, 8, 2, 1, 2, 4, 18]
result = filter(condition4, params)
print(list(result))  # [2, 6, 8, 2, 2, 4, 18]
