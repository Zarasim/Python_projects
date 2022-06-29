def merge(self, arr1, arr2, n, m):

    i = n-1
    j = 0

    while((i >= 0) & (j < m)):
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]

        i -= 1
        j += 1

    print(sorted(arr1) + sorted(arr2))
    print(sorted(arr2))

    return sorted(arr1) + sorted(arr2)
