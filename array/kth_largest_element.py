# find k-th largest element in array
# we remove the first k-1 largest element and retrieve the maximum one

# time complexity: n for max elem, and n for shifting n-1 values. This gives (k-1)*2n + n = O(kn)

# space complexity O(1)


import heapq  # minimum heap, so change sign


def kth_largest(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)


# improved solution by first sorting the elements

def kth_largest(arr, k):
    n = len(arr)
    arr.sort()        # T: O(nlogn)
    return arr[n-k]   # T: O(1)

# priority-queue implemented with heaps to get O(logn).
# heapify: Transform list x into a heap, in-place, in linear time.

# heappop: Pop and return the smallest item from the heap, maintaining the heap invariant.

# Time : n for arr, n for heap, (k-1)*logn + logn
# O(n + klogn). Works fine when k is smaller than n

# Space: n for arr


def kth_largest(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)
