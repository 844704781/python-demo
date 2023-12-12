_list = ['A', 'B', 'C']

a = 0
b = 1
c = 2

while True:
    a = int(input("请输入A的位置:"))
    b = int(input("请输入B的位置:"))
    c = int(input("请输入C的位置:"))
    break

# 方法1
_list[a-1]='A'
_list[b-1]='B'
_list[c-1]='C'
print(_list)

# 方法2
result = []
result.insert(a - 1, 'A')
result.insert(b - 1, 'B')
result.insert(c - 1, 'C')
print("排序后为:", result)
