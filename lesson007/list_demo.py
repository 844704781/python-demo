# # 创建列表，通过[]来创建列表
# my_list = []  # 创建列表
# print(my_list)
# print(type(my_list))
#
# # 列表存储的数据，我们称为元素
# # 一个列表中可以存储多个元素，也可以在创建列表时，来指定列表中的元素
# my_list = [1]
# print(my_list)
# print(type(my_list))
#
# # 当向列表中添加多个元素时，多个元素之间使用，隔开
# my_list = [1, 2, 3]
# print(my_list)
# print(type(my_list))
#
# # 列表中可以保存任意的对象
# my_list = [1, '', 'hello_word', None, 1.11, True]
# print(my_list)
# print(type(my_list))
# # 列表中的对象都会按照插入的顺序存储到列表中，
# #   第一个插入的对象保存到第一个位置，第二个保存到第二个位置
# # 我们可以通过索引(index)来获取列表中的元素
# #   索引是元素在列表中的位置，列表中的每一个元素都有一个索引
# #   索引是从0开始的整数,列表的第一个位置索引为0，第二个位置索引为1，第三个位置索引为2，以此类推
# my_list = [1, '', 'hello_word', None, 1.11, True]
# print(my_list[0])
# print(my_list[2])
# print(my_list[5])
#
# # 通过索引获取列表中的元素
# # 语法:my_list[索引] my_list[0]
# print(my_list[4])
# # 如果使用的索引超过了最大的范围，会抛出异常IndexError: list index out of range
# # print(my_list[6]) #IndexError: list index out of range
# # 获取列表的长度，列表中元素的个数
# # len()函数，通过该函数可以获取列表的长度
# # 获取到的长度值，是列表的最大索引+1
# print(len(my_list))
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(my_list[::2]) #[1, 3, 5, 7]
# print(my_list[1:5:2]) #[2, 4]
#
# # print(my_list[::0]) #ValueError: slice step cannot be zero
# print(my_list[::-1]) #[8, 7, 6, 5, 4, 3, 2, 1]
# print(my_list[::-2]) #[8, 6, 4, 2]
#
# print(my_list[1:5:-1]) #[]
#

my_list = []
a = [1, 2, 3, 1, 2, 2, 3, 3]
b = [3, 4, 6]

# xxxxxxx

# my_list[]

n = a[0]
my_list.append(n)
# my_list.append(a[1])
# my_list.append(a[2])
# my_list.append(b[1])

print(my_list)
