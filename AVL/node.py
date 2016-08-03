class Node(object):
    def __init__(self, data, parent_node):
        self.data = data
        self.balance = 0
        self.parent_node = parent_node
        self.left_child = None
        self.right_child = None

    def insert(self, data, parent_node):
        if data < self.data:
            if not self.left_child:
                self.left_child = Node(data, parent_node)
            else:
                self.left_child.insert(data, parent_node)
        else:
            if not self.right_child:
                self.right_child = Node(data, parent_node)
            else:
                self.right_child.insert(data, parent_node)

        return parent_node

    def remove(self):
        pass

    def traverseInOrder(self):
        if self.left_child:
            self.left_child.traverseInOrder()

        print(self.data)

        if self.right_child:
            self.right_child.traverseInOrder()

    def getMin(self):
        if not self.left_child:
            return self.data
        else:
            self.left_child.getMin()


    def getMax(self):
        if not self.right_child:
            return self.data
        else:
            self.right_child.getMax()



