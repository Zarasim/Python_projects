#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 17:49:35 2021


MOTIVATION: Array: contiguous space allocation
Linked list: values not stored contiguosly. 

Insert new element q at position 2 in an array of 4 elements:

- Usually you find the index, shift all the element from that index on the right and then insert the element. 
  For a long array you have to shift a lot of elements, the worst case scenario is O(n)
- Create a new node q and say, the next element of element 1 is q and q is linked to element 3. The cost is O(1).


@author: simone
"""

import numpy as np


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)


a.next = b
b.next = c
c.next = d

# a -> b -> c -> d -> null

# linked list traversal
# iterative O(n) time
# recursive O(n) time and space


def printLinkedList(head):
    current = head
    while current != None:
        print(current.val, '\n')
        current = current.next


printLinkedList(a)


def printLinkedListRecursive(head):
    if head == None:
        return

    print(head.val, '\n')
    printLinkedListRecursive(head.next)


printLinkedListRecursive(a)


# fill an array with the values of a linked list
# trivial for iterative way


def fillValuesRecursive(head, ls):
    if head == None:
        return

    ls.append(head.val)
    fillValuesRecursive(head.next, ls)


ls = []
fillValuesRecursive(a, ls)
print(ls)


# return total sum of the elements of a linked list
# iteratively time complexity O(m) and space complexity O(1) as we maintain a sum variable
# recursively we call the next nodes and we pass the sum value O(m) in space
# and time for the function call stack


def SumValuesRecursive(head):
    if head == None:
        return 0

    return head.val + SumValuesRecursive(head.next)


total = SumValuesRecursive(a)
print(total)


# linkedlistfind

# we return True or False based on the fact that the value is inside the list or not
# iterative has O(n) time complexity and O(1) space complexity
# recursive must have 2 base cases O(n) time and space for call stack

def findLinkedList(head, value):
    current = head
    while current != None:
        if current.val == value:
            return True
        current = current.next

    return False


def findLinkedListRecursive(head, value):
    # if head.val == value we call back the functions and never evaluate the condition
    # head == None

    if head == None:
        return False
    elif head.val == value:
        return True

    # if you don't define a return here you get a True that is not returned by the function
    return findLinkedListRecursive(head.next, value)


print(findLinkedList(a, 2))
print(findLinkedListRecursive(a, 2))

# get node value

# return node value at the given index
# iterative O(m) time and O(1) space
# recursive O(m) time and space


def getValueList(head, idx):
    current = head
    for i in range(idx):
        current = current.next
        if current == None:
            return None

    return current.val


def getValueListRecursive(head, idx):

    if idx == 0:
        return head.val
    if head == None:
        return None

    return getValueListRecursive(head.next, idx-1)


print(getValueList(a, 2))
print(getValueListRecursive(a, 1), '\n')


# Reverse list

# Use prev current and next temporary variables
# iterative time O(m) and space O(1)
# recursive as usual has space O(n)

def reverseList(head):
    prev = None
    current = head

    while current != None:

        front = current.next
        current.next = prev

        prev = current
        current = front


def reverseListRecursive(current, prev=None):
    # base case
    if current == None:
        return prev

    front = current.next
    current.next = prev

    return reverseListRecursive(front, current)


#new = reverseListRecursive(a)
# print(new.val)
# printLinkedList(d)


# zipper list

# take two linked list and form a single list that alternates the elements
# between them

# given list of length n and m, time is O(min(n,m)) and space O(1)


e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)
k = Node(9)
l = Node(10)


e.next = f
f.next = g
g.next = h
h.next = k
k.next = l


def zipperList(head1, head2):
    """ 
    Form a single Linked list alternating elements of the 
    two Linked List. 

    Input: head of each Linked List
    Output: None 

    """
    while head1 != None and head2 != None:

        front1 = head1.next
        front2 = head2.next

        head1.next = head2

        if front1 != None:
            head2.next = front1

        head1 = front1
        head2 = front2


def zipperListRecursive(head1, head2):

    # base case
    if head1 == None or head2 == None:
        return

    front1 = head1.next
    front2 = head2.next

    head1.next = head2

    if front1 != None:
        head2.next = front1

    return zipperListRecursive(front1, front2)


zipperListRecursive(a, e)
print('ZipperList', '\n')
printLinkedList(a)
