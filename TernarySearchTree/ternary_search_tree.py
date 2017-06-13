from .node import Node

class TST(object):
    """docstring for TST."""
    def __init__(self):
        super(TST, self).__init__()
        self.root = None

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value, 0)

    def put_item(self, node, key, value, index):

        c = key[index]

        if node == None:
            node = Node(c)

        if c < node.character:
            node.left_node = self.put_item(node.left_node, key, value, index)
        elif c > node.character:
            node.right_node = self.put_item(node.right_node, key, value, index)
        elif index < (len(key) - 1):
            node.mid_node = self.put_item(node.mid_node, key, value, index+1)
        else:
            node.value = value

        return node

    def get(self, key):
        node = self.get_item(self.root, key, 0)

        if node == None:
            return None

        return node.value

    def get_item(self, node, key, index):

        if node == None:
            return None

        c = key[index]

        if c < node.character:
            return self.get_item(node.left_node, key, index)
        elif c > node.character:
            return self.get_item(node.right_node, key, index)
        elif index < (len(key) - 1):
            return self.get_item(node.mid_node, key, index+1)
        else:
            return node

    def traverse_util(self, root, c_buffer, depth):
        if root is not None:
            self.traverse_util(root.left_node, c_buffer, depth)
            # c_buffer[depth] = str(root.character)
            c_buffer.append(str(root.character))

            # if len("".join(c_buffer)) == 2:
            #     print("".join(c_buffer))

            # if not any([root.left_node, root.right_node, root.mid_node]):
            # if root.value and len("".join(c_buffer)) == 2:
            if root.value:
                print("".join(c_buffer))
                # c_buffer = []

            self.traverse_util(root.mid_node, c_buffer, depth+1)
            if c_buffer:
                c_buffer.pop()

            self.traverse_util(root.right_node, c_buffer, depth)
            if c_buffer:
                c_buffer.pop()


    def traverse(self):
        # buf = [''] * 50
        buf = []
        self.traverse_util(self.root, buf, 0)
