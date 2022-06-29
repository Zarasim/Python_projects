def max_path_sum(grid):
    return cp(grid, 0, 0, {})


def cp(grid, r, c, memo):

    p = (r, c)
    if p in memo:
        return memo[p]

    # base case
    if r == len(grid)-1 and c == len(grid[0])-1 and grid[r][c]:
        return grid[r][c]

    if r == len(grid) or c == len(grid[0]):
        return 0

    # sum contribution from left and right

    res = max(grid[r][c] + cp(grid, r+1, c, memo),
              grid[r][c] + cp(grid, r, c+1, memo))

    memo[p] = res

    return memo[p]
