# remember that you cannot cast a float to an int
# with -1 reordering the first element is the last one of the listt


def reverse(x: int) -> int:

    x = str(x)

    if x[0] == '-':
        x = -int(float(x[:0:-1]))
    else:
        x = int(float(x[:0:-1]))

    if (x >= -2**31) & (x <= 2**31-1):
        return x
    else:
        return 0


print(reverse(-123))
