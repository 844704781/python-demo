a = 30
def fn2():
    #a = 30
    def fn3():
        print('fn3中:', 'a=', a)
    fn3()

fn2()
