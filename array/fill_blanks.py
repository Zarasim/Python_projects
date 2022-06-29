# Given an array containing None values fill in the None values with most recent
# non None value in the array
array1 = [1, None, 2, 3, None, None, 5, None]


def solution(array):

    valid = 0
    for i, elem in enumerate(array):
        if elem != None:
            valid = elem
        else:
            array[i] = valid

    return array


print(solution(array1))
