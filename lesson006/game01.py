# 唐僧大战白骨精游戏
user_atk = 2
user_hp = 20
boss_atk = 3
boss_hp = 100

welcome_tip = '欢迎光临唐僧大战白骨精的游戏！'
identify_tip = '''
请选择你的身份:
    1.唐僧
    2.白骨精
请选择(1/2):'''
identify_1 = "你已经选择唐僧，恭喜你将以唐僧的身份进行游戏！"
identify_2 = "什么？你竟然选择了白骨精？太不要脸了，系统将自动分配你为唐僧..."
identify_3 = "你输入了个啥？？？系统想了想，决定还是给你分配唐僧角色，嘿嘿。。。"

info = f'你的身份是->唐僧<-,你的攻击力是: {user_atk}, 你的生命值是:{user_hp}'
op_tip = '''你选择你要做的操作: 
    1.练级
    2.打BOSS
    3.逃跑
请选择(1/2/3):'''
op = 0
op1 = '恭喜你！->唐僧<-,你升级了！你现在的攻击力是:%s,你的生命值是%s'
op3 = '退出游戏，游戏结束'
print(welcome_tip)
identify = input(identify_tip)
print("=" * 40)
if identify == "1":
    print(identify_1)
elif identify == "2":
    print(identify_2)
else:
    print(identify_3)
print(info)
while True:
    print("=" * 40)
    print(f"唐僧 生命值:{user_hp},攻击力:{user_atk}")
    print(f"白骨精 生命值:{boss_hp},攻击力:{boss_atk}")
    op = input(op_tip)
    print("=" * 40)
    if op == '1':
        user_atk += 2
        user_hp += 2
        print(op1 % (user_atk, user_hp))
    elif op == '2':
        print("=" * 18 + "开始战斗" + "=" * 18)
        # TODO 唐僧攻击，白骨精反击，判断唐僧的生命值，判断白骨精的生命值
        boss_hp = boss_hp - user_atk
        print(f"唐僧-->白骨精")
        print(f"唐僧攻击白骨精，白骨精生命值-{user_atk}")
        print(f"白骨精生命值:{boss_hp}")
        if boss_hp <= 0:
            print("恭喜恭喜，白骨精被你打败了")
            input("游戏结束")
            break
        print("=" * 40)
        user_hp = user_hp - boss_atk
        print(f"白骨精-->唐僧")
        print(f"白骨精反击唐僧，唐僧生命值-{boss_atk}")
        print(f"唐僧生命值:{user_hp}")
        print("=" * 18 + "战斗结束" + "=" * 18)
        if user_hp <= 0:
            print("很遗憾,你的血量值小于等于0,你挂了")
            input("游戏结束")
            break
    elif op == '3':
        print(op3)
        input("游戏结束")
        break
