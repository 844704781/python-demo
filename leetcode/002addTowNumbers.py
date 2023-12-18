'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
比如
a = [3,2,1]
b = [7,8,9,9]
sum = [0,1,1,0,1]
       123  -->a
    + 9987  -->b
    -------
     10110
'''


def addTwoNumbers(l1, l2):
    '''
    列表求和
    :param l1: 整数1列表
    :param l2: 整数2列表
    :return:
    '''
    def add(list_a, list_b, c, _sum):
        '''
        使用递归列表求和

        结束条件:
          a,b,c都是0
         递归条件：
          当前计算结果的序列
          add(下一个a,下一个b,当前进位,当前计算结果序列)
        :param list_a: 整数1列表
        :param list_b: 整数2列表
        :param c: 进位
        :param _sum: 初始结果列表
        :return: 结果列表
        '''
        if _sum == None:
            _sum = []

        if len(list_a) == 0 and len(list_b) == 0 and c == 0:

            return _sum
        else:
            a = 0
            if len(list_a) != 0:
                a = list_a[0]
            b = 0
            if len(list_b) != 0:
                b = list_b[0]

            _sum.append((a + b + c) % 10)  # 计算每一位
            c = (a + b + c) // 10  # 下一个进位
            return add(list_a[1:], list_b[1:], c, _sum)

    return add(l1, l2, 0, [])


def intToSequence(num: int):
    '''
    将一个自然数倒叙，并存储列表中
    比如1234->[4,3,2,1]
    :param num: 自然数
    :return: 列表
    '''
    num_str = str(num)
    num_list = list(num_str)
    num_list.reverse()
    result = []
    for v in num_list:
        result.append(int(v))
    return result


num1 = intToSequence(123)
num2 = intToSequence(2343242)

s = addTwoNumbers(num1, num2)
print(s)
