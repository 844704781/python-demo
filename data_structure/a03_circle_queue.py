class ArrayQueue:

    def __init__(self, max_size):
        self.front = 0
        self.rear = 0
        self.max_size = max_size
        self.data = [0] * max_size

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def is_empty(self):
        return self.front == self.rear

    def get(self):
        if self.is_empty():
            print("队列为空")
            return
        _value = self.data[self.front]
        self.data[self.front] = 0
        self.front = (self.front + 1) % self.max_size
        return _value

    def add(self, _value):
        if self.is_full():
            print("数据已满")
            return
        self.data[self.rear] = _value
        self.rear = (self.rear + 1) % self.max_size

    def head(self):
        if self.is_empty():
            print("队列为空")
            return
        return self.data[self.front]

    def show(self):
        print(self.data)


queue = ArrayQueue(5)

while True:
    _input = input('''
    请输入你需要的功能：
        a. 增加
        s. 展示
        g. 获取第一个元素
        h. 查看第一个元素
    ''')

    if _input == 'a':
        value = int(input('请输入数字:\t'))
        queue.add(value)
        queue.show()
        pass
    elif _input == 's':
        queue.show()
        pass
    elif _input == 'g':
        value = queue.get()
        print('取出第一个元素:', value)
        pass
    elif _input == 'h':
        value = queue.head()
        print('第一个元素:', value)
        pass
    else:
        print("不支持的功能")
