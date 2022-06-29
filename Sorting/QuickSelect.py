#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:01:45 2021

@author: simone

k-th largest element with quickSelect

"""

def quickSelect(nums,l,r,k):
    
  
    pivot,p = nums[r],l
    for i in range(l,r):
        if nums[i] <= pivot:
            nums[p],nums[i] = nums[i],nums[p]
            p+=1
            
    nums[p],nums[r] = nums[r],nums[p]
    
    if p > k:
       return quickSelect(nums,l,p-1,k)
    if p < k:
        return quickSelect(nums,p+1,r,k)
    else:
        return nums[p]
    

nums = [3,2,1,5,6,4]
k = 2
k = len(nums) - k

print(quickSelect(nums,0,len(nums)-1,k))