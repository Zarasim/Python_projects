#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 17:52:25 2021

@author: simone

 a  -->  c
 |       |
 |       |
 b       e
 |
 |
 d - - - f


"""

graph = {'a': ['b', 'c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [], 'f': []}


# HasPath problem

# Depth first search implementation
# with n nodes and e edges the time complexity is O(e) and space is O(n)

def hasPath(graph, source, target):

    if source == target:
        return True

    stack = []
    # use stack for DFS
    # start from source and visit neighbors
    stack += graph[source]

    while stack != []:
        current = stack.pop()
        if current == target:
            return True

        if current != []:
            stack += graph[current]

    return False


def hasPathRecursive(graph, current, target):

    if current == target:
        return True

    for child in graph[current]:
        if hasPathRecursive(graph, child, target):
            return True

    return False


def hasPathBFS(graph, source, target):
    # work with queue
    if source == target:
        return True

    queue = []
    # use stack for DFS
    # start from source and visit neighbors
    queue += graph[source]

    while queue != []:
        current = queue.pop(0)
        if current == target:
            return True
        queue += graph[current]

    return False


print(hasPathBFS(graph, 'b', 'e'))   # true
print(hasPath(graph, 'b', 'e'))   # false
