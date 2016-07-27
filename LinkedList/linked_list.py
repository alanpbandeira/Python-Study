from node import Node


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.counter = 0

    def traverseList(self):

        current_node = self.head

        while current_node is not None:
            print ("%d ", current_node.data)
            current_node = current_node.next_node

    def insertStart(self, data):

        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

        self.counter += 1

    def insertEnd(self, data):

        if self.head is None:
            self.insertStart(data)
            return

        new_node = Node(data)
        current_node = self.head

        while current_node.next_node is not None:
            current_node = current_node.next_node

        current_node.next_node = new_node
        self.counter += 1

    def remove(self, data):

        if self.head:
            if self.head.data == data:
                self.head = self.head.next_node
            else:
                self.head.remove(data, self.head)

        self.counter -= 1

    def size(self):
        return self.counter


