def sum(n):
    """Using recursion, computes the sum of all integers between 1 and n, inclusive.
    Assume n is positive.

    >>> sum(1)
    1
    >>> sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    else:
        return n + sum(n-1)


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k//10)
    



def filter(f, seq):
    """Filter a sequence to only contain values allowed by filter.

    >>> def is_even(x):
    ...     return x % 2 == 0
    >>> def divisible_by5(x):
    ...     return x % 5 == 0
    >>> filter(is_even, [1,2,3,4])
    [2, 4]
    >>> filter(divisible_by5, [1, 4, 9, 16, 25, 100])
    [25, 100]
    """
    "*** YOUR CODE HERE ***"
    if not seq:
        return []
    elif not f(seq[0]):
        return filter(f, seq[1:])
    else:
        return [seq[0]] + filter(f,seq[1:])

    


def decimal(n):
    """Return a list representing the decimal representation of a number.

    >>> decimal(55055)
    [5, 5, 0, 5, 5]
    >>> decimal(-136)
    ['-', 1, 3, 6]
    """
    "*** YOUR CODE HERE ***"
    if n < 0:
        return ['-'] + decimal(-n)
    def base(x):

        x= str(x)
        if not x:
            return []
        else:
            return [int(x[0])] + base(x[1:])
    return base(n)



def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if (m ==1 or n ==1):
        return 1
    else:
        return paths(m-1,n) + paths(m, n-1)
