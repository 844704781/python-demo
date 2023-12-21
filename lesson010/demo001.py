try:
    print("开始")
    a = 1/0
    print("结束")
except NameError:
    print("异常啦")
else:
    print("恭喜你，成功了")
finally:
    print("我必须执行")
'''
开始
异常啦
我必须执行
'''