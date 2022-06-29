#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 11:15:22 2021

@author: simone
"""

# search for a path in a undirected graph
# this can be stored as a list of edges

# we first convert the list of edges in a adjacency list (dictionary)
# To avoid enter in a cycle, we define a set to mark the visited nodes
# time complexity O(e) and space complexity is O(n)

# lookup for a set requires O(1) in time , while for an array is O(n)

from collections import defaultdict


def buildGraph(edges):
    """
    Convert edge list into adjacency list
    Input: edge list as list of tuples
    Output; adjacency list as dictionary
    """

    graph = defaultdict(list)  # initialize empty dictionary

    for e in edges:

        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    return graph


def undirectedPath(edges, source, target):
    """
    Implementation with Depth First Search in recursive way
    """

    visited = set()
    graph = buildGraph(edges)
    return hasPath(graph, source, target, visited)

# implement the recursion call as a different function TO AVOID BUILDING THE GRAPH AT EACH ITERATION


def hasPath(graph, source, target, visited):

    if source not in visited:
        visited.add(source)

        if source == target:
            return True

        for neig in graph[source]:
            return hasPath(graph, neig, target, visited)

    return False


edges = [('i', 'j'), ('k', 'i'), ('m', 'k'), ('k', 'l'), ('o', 'n')]


#graph = buildGraph(edges)
print(undirectedPath(edges, 'l', 'j'))
