# given n find the k-th permutation

'''
There are n! elements can be divided into n column with starting number from 1 to n

'''

# O(n) space complexity
# O(n^2) time complexity


def getPermutation(n, k):
    permutation = []
    unused = list(range(1, n+1))
    fact = [1]*(n+1)
    for i in range(1, n+1):
        fact[i] = i*fact[i-1]

    k -= 1  # we start from 0 index

    # shift elements to the left for n times
    while n > 0:
        part_length = fact[n]//n
        i = k//part_length
        permutation.append(unused[i])
        unused.pop(i)
        n -= 1
        k %= part_length

    return ''.join(map(str, permutation))
