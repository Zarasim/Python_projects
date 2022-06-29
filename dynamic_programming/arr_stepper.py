def array_stepper(numbers):
    idx = 0
    return _arr_stepper(numbers, idx, {})


def _arr_stepper(numbers, idx, memo):

    if idx in memo:
        return memo[idx]

    # base case
    if idx == len(numbers) - 1:
        return 1

    if idx >= len(numbers):
        return 0

    current = numbers[idx]
    if current == 0:
        return False

    for i in range(1, current+1):
        memo[idx] = _arr_stepper(numbers, idx + i, memo)
        if memo[idx]:
            return True

    memo[idx] = False
    return False


print(array_stepper([
    31, 30, 29, 28, 27,
    26, 25, 24, 23, 22,
    21, 20, 19, 18, 17,
    16, 15, 14, 13, 12,
    11, 10, 9, 8, 7, 6,
    5, 3, 2, 1, 0, 0, 0
]))
