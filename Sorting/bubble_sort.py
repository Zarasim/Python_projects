'''
 
 With every new pass, the largest element in the list “bubbles up” toward its correct position.

Your implementation of bubble sort consists of two nested for loops in which the algorithm performs n - 1 comparisons, then n - 2 comparisons, and so on until the final comparison is done. This comes at a total of (n - 1) + (n - 2) + (n - 3) + … + 2 + 1 = n(n-1)/2 comparisons

'''


def bubble_sort(array):

    n = len(array)

    for i in range(n):

        already_sorted = True
        # Start looking at each item of the list one by one,

        # comparing it with its adjacent value. With each

        # iteration, the portion of the array that you look at

        # shrinks because the remaining items have already been

        # sorted.

        for j in range(n - i - 1):

            if array[j] > array[j + 1]:

                # If the item you're looking at is greater than its

                # adjacent value, then swap them

                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False

        # If there were no swaps during the last iteration,

        # the array is already sorted, and you can terminate

        if already_sorted:

            break

    return array
