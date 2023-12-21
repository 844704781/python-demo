a = '张三'
_b = '王老五'


def func():
    print("我是test模块的func方法")


class Demo:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    # 测试代码，主函数调用时则不会执行
    func()
