#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 11:20:57 2021

@author: simone
"""

def reverseString(string):
    if len(string) == 1:
        return string
    
    return reverseString(string[1:]) + string[0]



def isPalindrome(string):
    if len(string) == 1 or len(string) == 0:
        return True
    
    elif string[0] == string[-1]:        
        return isPalindrome(string[1:-1])
    
    return False

def convertBinary(num):
    
    if num == 1:
        return [1]
    if num == 0:
        return [0]
    
    binary = [num % 2]
    num = num // 2
    
    return binary + convertBinary(num)



def sumNatural(num):
    if num <= 1:
        return num
    
    return num + sumNatural(num-1)

print(reverseString('I am an Engineer'))
print(isPalindrome('kayyak'))
print(convertBinary(199))
print(sumNatural(10))