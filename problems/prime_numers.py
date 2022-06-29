# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

n = 35


def solution(n):

    res = []
    for i in range(1, n):
        prime = 1
        for j in range(2, i):
            if i % j == 0:
                prime = 0
                break
        if prime:
            res.append(i)

    return res


print(solution(n))
