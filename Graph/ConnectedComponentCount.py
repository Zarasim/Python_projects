#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 11:45:21 2021

@author: simone


connnected components count problem

time is O(e) and space O(n)  

"""


graph = {'0': ['8', '1', '5'],
         '1': ['0'],
         '5': ['0', '8'],
         '8': ['0', '5'],
         '2': ['3', '4'],
         '3': ['2', '4'],
         '4': ['3', '2']}


def connectedComponentCount(graph):
    """

    Iterative implementation of connectedComponentCount
    Use BFS with queue

    """
    visited = set()
    count = 0
    queue = []

    for node in graph.keys():
        if node in visited:
            continue

        queue = [node]
        #current = node
        # visited.add(current)
        while queue != []:
            current = queue.pop(0)
            for child in graph[current]:
                if child not in visited:
                    visited.add(child)
                    queue += child

        count += 1

    return count


def connected_components_count(graph):
    visited = set()
    count = 0
    for node in graph:
        if traversal(node, graph, visited):
            count += 1

    return count


def traversal(node, graph, visited):
    if node not in visited:
        visited.add(node)

        for neigh in graph[node]:
            traversal(neigh, graph, visited)

        return True

    else:
        return False


print(connected_components_count(graph))


###############################################################################

# largest component of graph
# O(e) time O(n) space


def largest_component(graph):
    max_size = 0
    visited = set()

    for node in graph:
        size_component = get_size(node, graph, visited)

        if size_component > max_size:
            max_size = size_component

    return max_size


def get_size(node, graph, visited):
    if node not in visited:
        visited.add(node)
        size = 1

        for neigh in graph[node]:
            size += get_size(neigh, graph, visited)

        return size

    else:

        return 0


print(largest_component({
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}))
