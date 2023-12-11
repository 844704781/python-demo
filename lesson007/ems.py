# 员工管理系统
employees = ["孙悟空\t18\t男\t花果山"]
line = "=" * 60

while True:
    print("=" * 20 + "欢迎使用员工管理系统" + "=" * 20)
    print("请选择要做的操作:")
    print("\t1.查询员工")
    print("\t2.添加员工")
    print("\t3.删除员工")
    print("\t4.退出系统")
    op = int(input("请选择(1-4):"))
    if op == 1:
        print(line)
        print("\t序号\t姓名\t年龄\t性别\t住址")
        i = 1
        for value in employees:
            print(f"\t{i}\t{value}")
            i += 1
        print(line)
    elif op == 2:
        print(line)
        name = input("请输入员工的姓名:")
        age = input("请输入员工的年龄:")
        gender = input("请输入员工的性别:")
        address = input("请输入员工的住址:")

        is_add = input("是否确认该操作[Y/N]:")
        if is_add == 'Y' or is_add == 'y':
            employees.append(f"{name}\t{age}\t{gender}\t{address}")
            print(line)
            print(" " * 24 + "添加成功" + " " * 24)
            print(line)
        else:
            print(line)
            print(" " * 23 + "添加已取消" + " " * 23)
            print(line)
    elif op == 3:
        while True:
            del_num = int(input("请输入要删除的员工的序号:"))
            if 0 < del_num <= len(employees):
                print("以下员工将被删除")
                print(line)
                print("\t序号\t姓名\t年龄\t性别\t住址")
                print(f"\t{del_num}\t{employees[del_num - 1]}")
                print(line)
                is_del = input("该操作不可恢复，是否确认[Y/N]:")
                if is_del == 'Y' or is_del == 'y':
                    employees.pop(del_num - 1)
                    print(line)
                    print(" " * 23 + "员工已删除" + " " * 23)
                    print(line)
                    break
                else:
                    print(line)
                    print(" " * 24 + "操作取消" + " " * 24)
                    print(line)
            else:
                print("您的输入有误，请重新输入")
    elif op == 4:
        print(line)
        print(" " * 22 + "感谢使用，再见！" + " " * 22)
        print(line)
        break
    else:
        print("无效的选择")
