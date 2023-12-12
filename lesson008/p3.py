_list = []
while True:
    name = input("请输入你喜欢的西游记人物(输入空格结束):")
    if name == ' ':
        break
    _list.append(name)

for value in _list:
    print(value)
