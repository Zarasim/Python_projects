#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 15:54:05 2021

@author: simone

Application of XOR operator (the application is bitwise):
    
a^0 = a
a^a  = 0
a^b^c = a^c^b

"""

## swap two values x and y in place


x = 52
y = 31

x ^= y  #  x^y,y
print(x,y)
y ^=x   # (y^x^y,0)
print(y,x)
x ^= y  # (x^y^y^x^y,x) = (x^x^y,x) =  (y,x)
print(x,y)


## Finding the missing number

#You are given an array A of n - 1 integers which are in the range between 1 and n. All numbers appear exactly once,
# except one number, which is missing. Find this missing number.


def findMissing(arr):
    
    n = len(arr) + 1
    
    for i in range(n):
        # impossible to cover the index n-1 as the missing number cannot be the last one
        v = i+1
        res = arr[i]^v
        if res != 0:
            return v
        

arr = [1,2,3,4,5,6,7,8,10]

print(findMissing(arr))



## Finding the Duplicate Number
# You are given an array A of n + 1 integers which are in the range between 1 and n. 
# All numbers appear exactly once, except one number, which is duplicated. Find this duplicated number.


def findDuplicated(arr):
    N = len(arr)
    res = 0
    for i in range(N):
        res ^= arr[i]
        if res == 0:
            return arr[i]
        else:
            res = arr[i]
        
arr = [11,12,13,13,14,15,16,17,18]
print(findDuplicated(arr))

## Finding Two Missing/Duplicate Numbers


# You are given an array A of n - 2 integers which are in the range between 1 and n.
# All numbers appear exactly once, except two numbers, which are missing. Find these two missing numbers.


def findTwoMissing(arr):
    
    N = len(arr) 
    blub = 0
    
    res2 = []
    for i in range(N):
        v = i+1
        if blub: v +=blub
        res = arr[i]^v
        if res != 0:
            res2.append(v)
            blub += 1 
            if len(res2) == 3:
                return res2
        

arr = [1,2,3,5,6,7,8,10,11,13,14,15]

print(findTwoMissing(arr))






        

        





