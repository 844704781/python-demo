add_result = [1, 2, 3] + [3, 4, 5]
print(add_result)  # [1, 2, 3, 3, 4, 5]

mul_result = [1, 2, 3] * 3
print(mul_result)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

people = ['孙悟空', '猪八戒', '沙和尚', '白龙马', '喵喵喵',
          '白龙马', '白骨精', '蜘蛛精', '喵喵喵', '蝎子精']
print('猪八戒' in people)  # True
if '喵喵喵' in people:
    print('喵喵叫')

people = ['孙悟空', '猪八戒', '沙和尚', '白龙马', '喵喵喵',
          '白龙马', '白骨精', '蜘蛛精', '喵喵喵', '蝎子精']
if '蔡徐坤' not in people:
    print('咯咯咯')

people = ['孙悟空', '猪八戒', '沙和尚', '白龙马', '喵喵喵',
          '白龙马', '白骨精', '蜘蛛精', '喵喵喵', '蝎子精']
print(len(people))  # 10

numbers = [1, 2, 3, 4, 2, -3, 4,
           3.9, 4.5, 9.9, 10.1,
           10.12, 3, 4, 6, 7]
print(min(numbers))  # -3

numbers = [1, 2, 3, 4, 2, -3, 4,
           3.9, 4.5, 9.9, 10.1,
           10.12, 3, 4, 6, 7]
print(max(numbers))  # 10.12

numbers = [1, 2, 3, 4, 2, -3,
           4, 3.9, 4.5, 9.9, 10.1,
           10.12, 3, 4, 6, 7]
meta_index = numbers.index(3)
print(meta_index)  # 2
meta_index = numbers.index(3, 3, 13)
print(meta_index)  # 12

numbers = [1, 2, 3, 4, 2, -3,
           4, 3.9, 4.5, 9.9, 10.1,
           10.12, 3, 4, 6, 7]
meta_count = numbers.count(3)
print(meta_count)  # 2
