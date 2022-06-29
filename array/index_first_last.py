# given target in array sorted find first and last index.

# start from first position until reaching the first index

# T(n) = O(n)  S(n) = O(1)

############################################

# pay attention to equality ! in 39

# à

from typing import List


def first_last(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
            return [start, i]

    return [-1, -1]


# binary search

def find_start(arr, target):
    if arr[0] == target:
        return 0

    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        print(mid)
        if arr[mid] == target and arr[mid-1] < target:
            return mid
        elif arr[mid] >= target:
            # look at left side of array
            right = mid - 1
        else:
            # look at right side of array
            left = mid + 1

    return -1


def find_end(arr, target):
    if arr[-1] == target:
        return len(arr) - 1

    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target and arr[mid+1] > target:
            return mid
        elif arr[mid] > target:
            # look at left side of array
            right = mid - 1
        else:
            # look at right side of array
            left = mid + 1

    return -1

# T(n) = 2 O(log n)
# S(n) = O(1)


def first_and_last(arr, target):
    # consider 3 cases where it's impossible to find target
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, 1]

    start = find_start(arr, target)
    end = find_end(arr, target)
    return [start, end]


arr = [1, 3, 4, 7, 7, 7, 8, 8, 8, 9]


print(first_and_last(arr, 7))
