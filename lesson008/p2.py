scissor = '剪刀'
stone = '石头'
cloth = '布'

a = input('A用户请出拳(剪刀/石头/布):')
b = input('B用户请出拳(剪刀/石头/布):')
if a == b:
    print("平局")
elif a == scissor:
    if b == stone:
        print("B赢")
    else:
        print("A赢")
elif a == stone:
    if b == scissor:
        print("A赢")
    else:
        print("B赢")
else:
    # A布
    if b == scissor:
        print("B赢")
    else:
        print("A赢")
