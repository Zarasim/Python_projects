def min_change(amount, coins):
    # define new function with memoization
    ans = min_change_memo(amount, coins, {})
    if ans == float('inf'):
        return -1
    else:
        return ans


def min_change_memo(amount, coins, memo):

    if amount in memo:
        return memo[amount]

    if amount < 0:
        return float('inf')

    if amount == 0:
        return 0

    min_coins = float('inf')

    for coin in coins:
        n_coins = 1 + min_change_memo(amount - coin, coins, memo)
        min_coins = min(min_coins, n_coins)

    memo[amount] = min_coins
    return min_coins
