employees = ['\t孙悟空\t18\t男\t花果山', '\t孙悟空\t18\t男\t花果山']

line = "="*57
while True:
    print("====================欢迎使用员工管理系统====================")
    num = input("""请选择要做的操作:
        1.查询员工
        2.添加员工
        3.删除员工
        4.退出系统
    请选择(1-4):""")
    if num == '1':
        # 查询
        print(line)
        print("序号\t姓名\t年龄\t性别\t住址")
        _index = 0
        for value in employees:
            print(f"{_index + 1}{value}")
            _index += 1
    elif num == '2':
        # 增加
        name = input("请输入员工的姓名:")
        age = input("请输入员工的年龄:")
        gender = input("请输入员工的性别:")
        address = input("请输入员工的住址:")
        check = input("是否确认该操作[Y/N]:")
        if check == 'Y' or check == 'y':
            employees.append(f"\t{name}\t{age}\t{gender}\t{address}")
            print(line)
            print(" " * 20 + "添加成功" + " " * 20)
            print(line)
        elif check == 'N' or check == 'n':
            print(line)
            print(" " * 20 + "添加已取消" + " " * 20)
            print(line)
        else:
            print("您的输入有误，请重新输入")
    elif num == '3':
        # 删除
        del_num = input("请输入要删除的员工的序号:")
        if 1 <= int(del_num) <= len(employees):
            print("以下员工将被删除")
            print(line)
            print("序号\t姓名\t年龄\t性别\t住址")
            print(f"{del_num}{employees[int(del_num) - 1]}")
            print(line)
            check = input("该操作不可恢复，是否确认[Y/N]:")
            if check == 'Y' or check == 'y':
                del employees[int(del_num) - 1]
                print(line)
                print(" " * 20 + "员工已被删除" + " " * 20)
                print(line)
            elif check == 'N' or check == 'n':
                print(line)
                print(" " * 20 + "操作已取消" + " " * 20)
                print(line)
            else:
                print("您的输入有误，请重新输入")
        else:
            print("您的输入有误，请重新输入")
    elif num == '4':
        # 退出
        print(line)
        print(" " * 20 + "感谢使用，再见！" + " " * 20)
        print(line)
        break
    else:
        print("您的输入有误，请重新输入")
