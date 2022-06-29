
def is_even(x):
    if x == 0:
        return True
    else:
        print(x, 'called by is_even')
        return is_odd(x-1)


def is_odd(x):
    print(x, 'called by is_odd')
    return not is_even(x)


# print(is_odd(3))
print(is_even(3))


"""

WHAT HAPPENED STEP BY STEP

is_even(3)

    3 called by is_even

    return is_odd(3-1)

==============================

is_odd(2)
    
    2 called by is_odd

    return not is_even(2)

==============================

is_even(2)

    2 called by is_even 

    return is_odd(2-1)

==============================

is_odd(1)

    1 called by is_odd 

    return not is_even(1)

==============================

is_even(1)

    1 called by is_even 

    return is_odd(1-1)

==============================

is_odd(0)

    0 called by is_odd

    return not is_even(0)

==============================

is_even(0)

    return True

==============================

NOW WORK YOUR WAY UP!

4. not(True) = False    <- End

3. not(False) = True

2. not(True) = False

1. True                 <- Start

ANSWER : FALSE

==============================

OR ANOTHER WAY TO VISUALLY EXPLAIN

1. not(not(not(True)))    

2. not(not(False))

3. not(True)

4. False

ANSWER : FALSE
"""
