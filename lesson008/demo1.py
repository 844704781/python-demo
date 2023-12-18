_list = [{"a": 1}, {"a": 2}, {"a": 3}, {"a": 4}, {"a": 5}]

flag = False  # 未找到
current_value = None
for value in _list:
    if value['a'] == 10:
        flag = True  # 找到了
        current_value = value

print("是否找到：", flag)
print("value：", current_value)

# if value not in _list:
#     print("不在里面")
