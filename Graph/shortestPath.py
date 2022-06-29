#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 15:49:08 2021

@author: simone

Implementation of Shortest Path 
using Breadth First Search

Keep track of the tuple (current,distance) from the source to the target

Use the queue for BFS traversal

This has a linear complexity

Alternative version:
    
    
def shortest_path(edges, node_A, node_B):
  graph = buildGraph(edges)
  
  # initialize queue for BFS
  dist = 0
  queue = [(node_A,dist)]
  visited = set(node_A)
  
  while queue != []:
    current,dist = queue.pop(0)
    
    if current == node_B:
      return dist
    
    for child in graph[current]:
      if child not in visited:      
        visited.add(child)    
        queue += [(child,dist+1)]
    
  
  return -1  
  
"""


import time
edges = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
]


def shortest_path(edges, node_A, node_B):
    graph = buildGraph(edges)

    # initialize queue for BFS
    dist = 0
    queue = [(node_A, dist)]
    visited = set()

    while queue != []:
        current, dist = queue.pop(0)
        if current in visited:
            continue   # run next iteration of while

        visited.add(current)
        if current == node_B:
            return dist

        dist += 1
        for child in graph[current]:
            queue += [(child, dist)]

    return -1


def buildGraph(edges):
    """
    Convert edge list into adjacency list
    Input: edge list as list of tuples
    Output; adjacency list as dictionary
    """

    graph = {}  # initialize empty dictionary

    for e in edges:
        if not e[0] in graph.keys():
            graph[e[0]] = []
        if not e[1] in graph.keys():
            graph[e[1]] = []

        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    return graph


t0 = time.time()
print(shortest_path(edges, 'e', 'c'))
print(time.time() - t0)
