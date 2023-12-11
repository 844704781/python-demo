i = 0
while i < 5:
    j = 0
    while j < 5:
        print("* ", end='')
        j += 1
    print()
    i += 1


i = 0
while i < 5:
    j = 0
    while j <= i:
        print("* ", end='')
        j += 1
    print()
    i += 1

i = 0
while i < 5:
    j = 0
    while j < 5 - i:
        print("* ", end='')
        j += 1
    print()
    i += 1

'''
0 --->5
1 --->4
2 --->3
4 --->1
'''
