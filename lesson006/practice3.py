'''
我家的狗5岁了，5岁的狗相当于多大的年龄的人呢？
其实非常简单，狗的前两年每一年相当于人类的10.5岁，然后每增加一年就增加4岁。
那么5岁的狗等于人类的年龄就应该是10.5+10.5+4+4+4 = 33岁
'''
dog_age = input("请输入狗的岁数：")
dog_age = float(dog_age)
like_person_age = 0

if dog_age > 0:
    if dog_age <= 2:
        like_person_age = dog_age * 10.5
    else:
        like_person_age = 2 * 10.5 + (dog_age - 2) * 4
    print(f"狗的年龄:{dog_age},相当于人的年龄:{like_person_age}")
else:
    print(f"无效的年龄:{dog_age}")
input("按Enter结束程序")
