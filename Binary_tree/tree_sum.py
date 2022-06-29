class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_sum(root):
    '''
        return total sum in the tree
    '''
    if root == None:
        return 0

    return root.val + tree_sum(root.left) + tree_sum(root.right)


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


print(tree_sum(a))
