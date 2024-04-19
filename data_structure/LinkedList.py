class HeroNode:
    def __init__(self, no, name):
        self.__no = no
        self.__name = name
        self.__next = None

    @property
    def next(self):
        return self.__next

    @property
    def no(self):
        return self.__no

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @next.setter
    def next(self, node):
        self.__next = node

    def __str__(self):
        return f'| no={self.no},name={self.name} |'


class LinkedList:

    def __init__(self):
        self.__head = HeroNode(0, '')

    @property
    def head(self):
        return self.__head

    def show(self):
        '''
        遍历打印链表
        :return: None
        '''
        temp = self.head.next
        while temp is not None:
            print(temp)
            temp = temp.next

    def add(self, node):
        '''
        向链表尾部插入节点
        :param node:
        :return:
        '''
        temp = self.head

        while temp is not None:
            if temp.next is None:
                temp.next = node
                break
            temp = temp.next

    def add_by_order(self, node):
        '''
        按照编号大小向链表中插入节点
        :param node:
        :return:
        '''
        temp = self.head

        while True:
            if temp.next is None:
                break
            if temp.next.no == node.no:
                raise ValueError("存在相同的no的node")

            if temp.next.no > node.no:
                break

            temp = temp.next

        node.next = temp.next
        temp.next = node
        pass

    def update(self, no, name):
        '''
        修改节点中的数据
        :param no:
        :param name:
        :return:
        '''
        temp = self.head.next
        while temp is not None:
            if temp.no == no:
                temp.name = name
            temp = temp.next
        pass

    def delete(self, no):
        '''
        删除节点
        :param no:
        :return:
        '''
        temp = self.head
        while temp is not None:
            if temp.next is None:
                break
            if temp.next.no == no:
                temp.next = temp.next.next
                break

            temp = temp.next
        pass

    def __len__(self):
        '''
        求链表中有效节点的个数(不统计头结点)
        :return:
        '''
        temp = self.head.next
        _len = 0
        while temp is not None:
            _len += 1
            temp = temp.next
        return _len

    @staticmethod
    def find_last_index_node(_list, k):
        '''
        查找链表的倒数第k个节点 (新浪面试题)
        :param _list:
        :param k:
        :return:
        '''
        length = len(_list)
        if k > length or k < 1:
            raise IndexError("Invalid k")
        n = length - k + 1

        temp = _list.head.next
        i = 1
        while i < n:
            temp = temp.next
            i += 1

        return temp

    def revert(self):
        '''
        将单链表在原有的结构上反转 (腾讯面试题)
        :return:
        '''
        # 定义反转链表头结点 revert_head
        # 遍历原有单链表
        # 定义next_node,记录当前节点current的next节点
        # 将current节点插入revert_head和revert_head.next之间
        # 将反转链表的数据指向原来链表的head
        revert_head = HeroNode(0, "")
        current_node = self.head.next
        while True:
            if current_node is None:
                break

            next_node = current_node.next
            current_node.next = revert_head.next
            revert_head.next = current_node
            current_node = next_node

        self.head.next = revert_head.next

    def revert_print(self):
        '''
        将单链表反向打印，不破坏原有结构 (腾讯面试题)
        压栈方式
        :return:
        '''
        stack = []
        temp = self.head.next

        while temp is not None:
            stack.append(temp)
            temp = temp.next

        while len(stack) != 0:
            print(stack.pop())

    @staticmethod
    def revert_print_with_recursion(temp):
        '''
        将单链表反向打印，不破坏原有结构 (腾讯面试题)
        递归方式
        :param temp:
        :return:
        '''
        if temp is None:
            return

        LinkedList.revert_print_with_recursion(temp.next)
        if temp.no != 0:
            print(temp)

    @staticmethod
    def merge(*lists):
        '''
        合并多个链表，合并之后的链表有序 (百度面试题)
        :param nodes:
        :return:
        '''

        result = LinkedList()
        for _list in lists:
            temp = _list.head.next

            while temp is not None:
                result.add_by_order(HeroNode(temp.no, temp.name))
                temp = temp.next

        return result


def main():
    _list = LinkedList()
    _list.add_by_order(HeroNode(9, 'A'))
    _list.add_by_order(HeroNode(8, 'B'))
    _list.add_by_order(HeroNode(7, 'B'))
    _list.add_by_order(HeroNode(6, 'B'))
    _list.add_by_order(HeroNode(5, 'B'))
    _list1 = LinkedList()
    _list1.add_by_order(HeroNode(91, 'A'))
    _list1.add_by_order(HeroNode(81, 'B'))
    _list1.add_by_order(HeroNode(71, 'B'))
    _list1.add_by_order(HeroNode(61, 'B'))
    _list1.add_by_order(HeroNode(51, 'B'))

    result = LinkedList.merge(_list, _list1)
    result.show()


if __name__ == '__main__':
    main()
