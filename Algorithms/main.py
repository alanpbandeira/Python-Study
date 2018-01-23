from TernarySearchTree.ternary_search_tree import TST


tree = TST()

tree.put("apple", 100)
tree.put("apples", 100)
tree.put("orange", 200)
tree.put("ob", 200)
tree.put("oe", 200)
tree.put("og", 200)

print (tree.get("orange"))

tree.traverse()
