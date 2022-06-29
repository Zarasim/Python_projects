#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 09:37:56 2021

Find minimum island using DFS recursively

@author: simone
"""


grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]


def minimum_island_size(grid):
    """
          Return size of minimum island using DFS for computing the size 
    """

    nrows = len(grid)
    ncols = len(grid[0])
    visited = set()
    min_size = nrows*ncols + 1

    for r in range(nrows):
        for c in range(ncols):
            if not (r, c) in visited and grid[r][c] == 'L':
                # start BFS
                size = 0
                current = (r, c)
                sizeIsland = exploreDFS(grid, current, visited)
                if sizeIsland < min_size:
                    min_size = sizeIsland

    return min_size if min_size < nrows*ncols + 1 else 0


def exploreDFS(grid, current, visited):

    def limit_bound(x): return (x[0] >= 0 and x[0] < len(
        grid)) and (x[1] >= 0 and x[1] < len(grid[0]))

    if current in visited or not limit_bound(current) or grid[current[0]][current[1]] == 'W':
        return 0

    visited.add(current)
    size = 1
    r, c = current
    neighs = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
    for neigh in neighs:
        size += exploreDFS(grid, neigh, visited)

    return size


print(minimum_island_size(grid))
