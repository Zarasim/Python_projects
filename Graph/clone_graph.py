# Assume Node class defined with val and neigh attributes

from sklearn.feature_selection import SelectFdr


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


def cloneGraph(node):
    oldtonew = {}

    def dfs(node):
        if node in oldtonew:
            return oldtonew[node]

        copy = Node(node.val)
        oldtonew[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node) if node else None
