'''

For breadth-first-traversal use queue
Time/Space O(n)

'''

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs(root):
    if root == None:
        return []

    queue = deque()
    queue.append(root)

    result = []
    while len(queue) > 0:
        # remove front of the queue
        current = queue.popleft()
        result.append(current.val)
        if current.left != None:
            queue.append(current.left)
        if current.right != None:
            queue.append(current.right)

    return result


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

print(bfs(a))
