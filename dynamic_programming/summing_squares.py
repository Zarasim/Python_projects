def summing_squares(n):
    # define first perfect squares
    squares = [i**2 for i in range(1, n+1) if i**2 <= n]

    amount = n
    if amount in squares:
        return 1
    else:
        return sum_rec(squares, amount, {})


def sum_rec(squares, amount, memo):

    if amount in memo:
        return memo[amount]

    # base case
    if amount < 0:
        return 0

    if amount == 0:
        return 0

    min_count = float('inf')
    values = [amount - i for i in squares if amount >= i]
    for val in values:
        count = 1 + sum_rec(squares, val, memo)
        if count < min_count:
            min_count = count

    memo[amount] = min_count

    return memo[amount]


print(summing_squares(87))
