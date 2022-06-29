# Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
# the non-zero elements.

array1 = [0, 1, 0, 3, 12]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]


def solution(nums):

    idx = 0
    idx_zero = 0
    for num in nums:
        if num != 0:
            nums[idx] = num
            idx += 1
        else:
            idx_zero += 1

    # assign a list with another list. It does not cast as for numpy arrays
    nums[idx:] = [0]*idx_zero

    return nums


print(solution(array2))
