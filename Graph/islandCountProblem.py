#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 17:23:07 2021

@author: simone

island count problem

time complexity O(rc) for iterative implementation
Space complexity O(rc) if we add all the cells in the visited set

from collections import deque()
pop with popleft()

"""


grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

grid = [
    ['L', 'W', 'W', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'L'],
]

grid = [
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
]

grid = [
    ['W', 'W'],
    ['W', 'W'],
    ['W', 'W'],
]


def island_count(grid):
    nrows = len(grid)
    ncols = len(grid[0])
    visited = set()
    count = 0

    for r in range(nrows):
        for c in range(ncols):
            if not (r, c) in visited and grid[r][c] == 'L':
                # start BFS with queue
                start = (r, c)
                queue = [start]
                visited.add(start)

                while queue != []:
                    r, c = queue.pop(0)
                    children = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                    neighs = list(filter(lambda x: (x[0] >= 0 and x[0] < nrows) and (
                        x[1] >= 0 and x[1] < ncols), children))
                    for child in neighs:
                        if child not in visited and grid[child[0]][child[1]] == 'L':
                            visited.add(child)
                            queue += [child]

                count += 1

    return count


print(island_count(grid))
