'''
Write a function, max_path_sum, that takes in the root of a binary tree that contains number values. The function should return the maximum sum of any root to leaf path within the tree.

'''
from numpy import infty
import numpy


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_path_sum(root):

    if root == None:
        return -infty

    if root.left == None and root.right == None:
        return root.val

    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

print(max_path_sum(a))
