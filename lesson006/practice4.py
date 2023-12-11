'''
从键盘输入小明的期末成绩：
	当成绩为100时，奖励一辆BMW，
	当成绩为[80-99]时，奖励一台iphone，
	当成绩为[60-79]时，奖励一本参考书
	其他时，什么奖励也没有
'''
score = input("请输入成绩：")
score = int(score)
if score < 0 or score > 100:
    print("您的输入不合法")
else:
    if score == 100:
        print("奖励一辆BMW")
    elif 80 <= score <= 99:
        print("奖励一台iPhone")
    elif 60 <= score <= 79:
        print("奖励一本参考书")
    else:
        print("什么奖励都没有")
