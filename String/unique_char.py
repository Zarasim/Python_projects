# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.

from collections import defaultdict
from collections import Counter

# Approach 1


def solution(s):
    str_dict = {}
    for i, char in enumerate(s):
        if char not in str_dict:
            str_dict[char] = i
        else:
            del str_dict[char]

    if str_dict != {}:
        return next(iter(str_dict.values()))
    else:
        return -1


# import Counter from collections

def solution2(s):
    # build hash map : character and how often it appears
    # <-- gives back a dictionary with words occurrence count
    count = Counter(s)
    #Counter({'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1})
    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1


print(solution('alphabet'))
print(solution('barbados'))
print(solution('crunchy'))


print(solution2('alphabet'))
print(solution2('barbados'))
print(solution2('crunchy'))
