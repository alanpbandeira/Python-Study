from Study.AVL.node import Node


class AVL(object):
    """docstring"""
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        """docstring"""

        parent_node = self.root_node

        if self.root_node is None:
            parent_node = Node(data, None)
            self.root_node = parent_node
        else:
            parent_node = self.root_node.insert(data, self.root_node)

        self.rebalance_tree(parent_node)

    def rebalance_tree(self, parent_node):
        """docstring"""

        self.setBalance(parent_node)

        if parent_node.balance < -1:
            if self.height(parent_node.left_child.left_child) >= self.height(
                    parent_node.left_child.right_child):
                parent_node = self.rotateRight(parent_node)
            else:
                parent_node = self.rotateLeftRight(parent_node)

        elif parent_node.balance > 1:
            if self.height(parent_node.right_child.right_child) >= self.height(
                    parent_node.right_child.left_child):
                parent_node = self.rotateLeft(parent_node)
            else:
                parent_node = self.rotateRightLeft(parent_node)

        if parent_node.parent_node is not None:
            self.rebalance_tree(parent_node.parent_node)
        else:
            self.root_node = parent_node

    def setBalance(self, node):
        """docstring"""
        node.balance = (self.height(node.right_child) - self.height(node.left_child))

    def height(self, node):
        """docstring"""
        if node is None:
            return -1
        else:
            return 1 + max(self.height(node.left_child), self.height(node.right_child))

    def rotateRight(self, node):
        """docstring"""
        print("Rotate Right...")

        b = node.left_child
        b.parent_node = node.parent_node

        node.left_child = b.right_child

        if node.left_child is not None:
            node.left_child.parent_node = node

        b.right_child = node
        node.parent_node = b

        if b.parent_node is not None:
            if b.parent_node is not None:
                if b.parent_node.right_child == node:
                    b.parent_node.right_child = b
                else:
                    b.parent_node.left_child = b

        self.setBalance(b)
        self.setBalance(node)

        return b

    def rotateLeft(self, node):
        """docstring"""
        print("Rotate Left...")

        b = node.right_child
        b.parent_node = node.parent_node

        node.right_child = b.left_child

        if node.right_child is not None:
            node.right_child.parent_node = node

        b.left_child = node
        node.parent_node = b

        if b.parent_node is not None:
            if b.parent_node.right_child == node:
                b.parent_node.right_child = b
            else:
                b.parent_node.left_child = b

        self.setBalance(node)
        self.setBalance(b)

        return b

    def rotateLeftRight(self, node):
        """docstring"""
        print("Rotation Left - Right...")
        node.left_child = self.rotateLeft(node.left_child)
        return self.rotateRight(node)

    def rotateRightLeft(self, node):
        """docstring"""
        print("Rotation Right - Left...")
        node.right_child = self.rotateRight(node.right_child)
        return self.rotateLeft(node)

    def traverse_in_order(self):
        """docstring"""
        self.root_node.traverse_in_order()
