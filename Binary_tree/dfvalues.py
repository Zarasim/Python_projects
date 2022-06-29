class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs(root):
    # base case
    if not root:
        return []

    stack = [root]
    result = []
    while stack != []:
        current = stack.pop()
        result.append(current.val)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return result


def dfs_rec(root):
    if root == None:
        return []

    leftvalues = dfs_rec(root.left)
    rightvalues = dfs_rec(root.right)

    return [root.val] + leftvalues + rightvalues


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

print(dfs_rec(a))
