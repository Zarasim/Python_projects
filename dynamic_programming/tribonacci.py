def tribonacci(n):
    memo = {}
    return _trib(n, memo)


def _trib(n, memo):

    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    memo[n] = _trib(n-1, memo) + _trib(n-2, memo) + _trib(n-3, memo)
    return memo[n]


print(tribonacci(20))  # -> 35890
