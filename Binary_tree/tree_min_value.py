
'''
Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. The function should return the minimum value within the tree.
'''


from numpy import infty


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_min_value(root):
    if root == None:
        return infty

    return min(root.val, tree_min_value(root.left), tree_min_value(root.right))


a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(14)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e

print(tree_min_value(a))  # -> -2
