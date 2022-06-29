# Given an array of integers, determine whether the array is monotonic or not.
from audioop import reverse
from collections import OrderedDict
from re import L
A = [6, 5, 4, 4]
B = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
C = [1, 1, 2, 3, 7]

# solution 1


def solution(nums):

    if sorted(nums) == nums or sorted(nums, reverse=True) == nums:
        return True

    return False


# solution 2
def solution2(nums):

    l = len(nums)
    order = ''

    for i in range(l-1):
        if nums[i] >= nums[i+1]:
            if order == 'a':
                return False
            order = 'd'
        elif nums[i] < nums[i+1]:
            if order == 'd':
                return False
            order = 'a'
    return True


def solution3(nums):
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)))


print(solution2(A))
