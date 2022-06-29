'''
Time O(2^(r+c)) 
Space O(r+c)

'''


def count_paths(grid):
    return cp(grid, 0, 0, {})


def cp(grid, r, c, memo):

    p = (r, c)
    if p in memo:
        return memo[p]
    # base case
    if r == len(grid)-1 and c == len(grid[0])-1 and grid[r][c] == "O":
        return 1

    if r == len(grid) or c == len(grid[0]) or grid[r][c] == "X":
        return 0

    # sum contribution from left and right

    count_left = cp(grid, r+1, c, memo)
    count_right = cp(grid, r, c+1, memo)

    memo[p] = count_left + count_right

    return memo[p]


print(count_paths(grid=[
    ["O", "O", "O"],
    ["O", "O", "X"],
    ["O", "O", "O"],
]))
