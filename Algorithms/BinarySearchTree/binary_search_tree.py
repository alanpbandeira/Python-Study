from Study.BinarySearchTree.node import Node


class BST(object):

    def __init__(self):
        self.root_node = None

    def insert(self, data):
        if not self.root_node:
            self.root_node = Node(data)
        else:
            self.root_node.insert(data)

    def remove(self, target_data):
        if self.root_node:
            if self.root_node.data == target_data:
                temp_node = Node(None)
                temp_node.left_child = self.root_node
                self.root_node.remove(target_data, temp_node)
            else:
                self.root_node.remove(target_data, None)

    def getMax(self):
        if self.root_node:
            return self.root_node.getMax()

    def getMin(self):
        if self.root_node:
            return self.root_node.getMin()

    def traverseInOrder(self):
        if self.root_node:
            return self.root_node.traverseInOrder()