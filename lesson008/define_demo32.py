def select(func, _list):
    '''
    获取列表中所有偶数返回
    :param _list:
    :return:
    '''
    _result = []
    for v in _list:
        if func(v):
            _result.append(v)

    return _result


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
result = select(condition4, params)
print(result)  # [2, 6, 8, 2, 2, 4, 18]
