class Demo:

    def hello(self):
        print("我是实例方法")

    def __del__(self):
        print("我要被回收了，拜拜", self)


a = Demo()
print("1")
print("2")
input("按Enter拜拜")
'''
1
2
按Enter拜拜
我要被回收了，拜拜 <__main__.Demo object at 0x103dd97f0>
'''
