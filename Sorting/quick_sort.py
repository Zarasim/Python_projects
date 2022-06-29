'''


Because of how the Quicksort algorithm works, the number of recursion levels depends on where pivot ends up in each partition. In the best-case scenario, the algorithm consistently picks the median element as the pivot. That would make each generated subproblem exactly half the size of the previous problem, leading to at most log2n levels.

On the other hand, if the algorithm consistently picks either the smallest or largest element of the array as the pivot, then the generated partitions will be as unequal as possible, leading to n-1 recursion levels. That would be the worst-case scenario for Quicksort.

As you can see, Quicksort’s efficiency often depends on the pivot selection. If the input array is unsorted, then using the first or last element as the pivot will work the same as a random element. But if the input array is sorted or almost sorted, using the first or last element as the pivot could lead to a worst-case scenario. Selecting the pivot at random makes it more likely Quicksort will select a value closer to the median and finish faster.


'''


from random import randint


def quicksort(array):

    if len(array) < 2:

        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly

    pivot = array[randint(0, len(array) - 1)]

    for item in array:

        # Elements that are smaller than the `pivot` go to

        # the `low` list. Elements that are larger than

        # `pivot` go to the `high` list. Elements that are

        # equal to `pivot` go to the `same` list.

        if item < pivot:

            low.append(item)

        elif item == pivot:

            same.append(item)

        elif item > pivot:

            high.append(item)

    # The final result combines the sorted `low` list

    # with the `same` list and the sorted `high` list

    return quicksort(low) + same + quicksort(high)
