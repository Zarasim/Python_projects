from sklearn import tree


def invert_binary_tree(root):
    if root is None:
        return
    tree.left, tree.right = tree.right, tree.left

    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)

    return root
