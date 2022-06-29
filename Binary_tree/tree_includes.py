'''

Given a target, we have to answer True or False depending whether it is included or not

'''

#from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_includes(root, target):
    '''
    Use dfs recursively to find the target

    '''
    if root == None:
        return False
    elif root.val == target:
        return True

    return tree_includes(root.left, target) | tree_includes(root.right, target)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(tree_includes(a, "e"))
