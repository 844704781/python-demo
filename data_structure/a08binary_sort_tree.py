class Node:
    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return '{ value: %s }' % self.__value

    def add(self, node: 'Node'):
        if self.value >= node.value:
            if self.left is not None:
                self.left.add(node)
            else:
                self.left = node
        else:
            if self.right is not None:
                self.right.add(node)
            else:
                self.right = node

    def infix_order(self):
        if self.left is not None:
            self.left.infix_order()

        print(self)

        if self.right is not None:
            self.right.infix_order()

    def search(self, value):
        if self.value == value:
            return self
        elif self.value > value:
            if self.left is None:
                return
            return self.left.search(value)
        else:
            if self.right is None:
                return
            return self.right.search(value)

    def search_parent(self, node: 'Node'):
        if ((self.left is not None and self.left.value == node.value)
                or (self.right is not None and self.right.value == node.value)):
            return self
        elif self.value > node.value:
            if self.left is None:
                return
            return self.left.search_parent(node)
        else:
            if self.right is None:
                return
            return self.right.search_parent(node)

    def find_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current


class BinarySortTree:

    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, node):
        self.__root = node

    def add(self, other: Node):
        if self.__root is None:
            self.__root = other
        else:
            self.__root.add(other)

    def infix_order(self):
        if self.__root is None:
            return
        self.__root.infix_order()

    def search(self, value) -> Node:
        return self.root.search(value)

    def search_parent(self, node) -> Node:
        return self.root.search_parent(node)

    def find_max_and_del(self, node) -> Node:
        max_node = node.find_max()
        self.delete(max_node)
        return max_node

    def delete(self, value):
        if self.root is None:
            return
        target_node = self.search(value)

        if target_node is self.root:
            # 处理根节点
            if target_node.left is None and target_node.right is None:
                self.root = None
            elif target_node.right is None:
                # 左节点不为空
                self.root = self.root.left
            elif target_node.left is None:
                self.root = self.root.right
            else:
                # 左右都不为空,查找左子树的最大值，将其放在根节点位置
                max_node = self.find_max_and_del(self.root.left)
                max_node.right = target_node.right
                if max_node.left is None:
                    max_node.left = target_node.left
                self.root = max_node
        else:
            # 处理非根结点
            parent_node = self.search_parent(target_node)

            if target_node.left is None and target_node.right is None:
                # 删除的是叶子结点
                if target_node is parent_node.left:
                    parent_node.left = None
                else:
                    parent_node.right = None

            elif target_node.left is not None or target_node.right is not None:
                # 有一棵子树
                if parent_node.left is target_node:
                    if target_node.left is not None:
                        parent_node.left = target_node.left
                    else:
                        parent_node.left = target_node.right
                else:
                    if target_node.left is not None:
                        parent_node.right = target_node.left
                    else:
                        parent_node.right = target_node.right
            else:
                # 有两个子树
                max_node = self.find_max_and_del(target_node.left)
                max_node.right = target_node.right
                if max_node.left is None:
                    max_node.left = target_node.left
                if target_node is parent_node.left:
                    parent_node.left = max_node
                else:
                    parent_node.right = max_node


def main():
    nodes = [Node(num) for num in [8, 3, 1, 5, 9, 2, 7, 15, 10, 4, 6, 11, 12, 13, 14]]

    tree = BinarySortTree()
    for node in nodes:
        tree.add(node)

    for i in range(1, 16):
        if i == 14:
            pass
        tree.delete(i)
        tree.infix_order()
        print('%s' % i + "-" * 20)


main()
