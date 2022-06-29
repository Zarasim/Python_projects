#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 17:20:15 2021

@author: simone
"""

def climbStairs(self, n: int) -> int:
    """
    :type N: int
    :rtype: int
    """
    cache = {}
    def recur_stairs(N,result):
        if N in cache:
            return cache[N]

        if N <= 2:
            result = N
        else:
            result = recur_stairs(N-1,result) + recur_stairs(N-2,result)

        # put result in cache for later reference.
        cache[N] = result
        return result

    return recur_stairs(n,0)