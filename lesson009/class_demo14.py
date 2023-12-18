class A:
    def test1(self):
        print("AAA")

    def hello(self):
        print("hello A")


class B:
    def test2(self):
        print("BBB")

    def hello(self):
        print("hello B")


class C(A, B):
    def test(self):
        print("CCC")


c = C()
c.test1()  # AAA
c.test2()  # BBB
c.test()  # CCC
c.hello()  # hello A
