def accumulator():
    '''
      定义一个累加器
    :return: 累加方法
    '''
    a = 0

    def increment():
        nonlocal a
        a = a + 1
        print(a)

    a = 2 # 这种写法在Java是不被允许的，在Python可以
    return increment


increment = accumulator()
increment()
increment()
increment()
increment()
