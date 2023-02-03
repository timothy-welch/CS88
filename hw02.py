"""Homework 2."""

def fib(n):
    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(100)
    354224848179261915075
    """
    "*** YOUR CODE HERE ***"
    if n == 0 or n == 1:
        return n
    a, b, i = 0,1,1
    while i < n:
        total = a + b
        a,b = b, total
        i += 1
    return total

def nonzero(lst):
    """ Returns the first nonzero element of a list

    >>> nonzero([1, 2, 3])
    1
    >>> nonzero([0, 1, 2])
    1
    >>> nonzero([0, 0, 0, 0, 0, 0, 5, 0, 6])
    5
    """
    "*** YOUR CODE HERE ***"
    for num in lst:
        if num != 0:
            return num


def has_n(lst, n):
    """ Returns whether or not a list contains the value n.

    >>> has_n([1, 2, 2], 2)
    True
    >>> has_n([0, 1, 2], 3)
    False
    >>> has_n([], 5)
    False
    """
    "*** YOUR CODE HERE ***"
    try:
        lst.index(n)
    except: 
        return False
    a = lst.index(n)
    if a > 0:
        return True

def total_price(prices):
    """
    Finds the total price of all products in prices including a
    50% tax on products with a price greater than or equal to 20.
    >>> total_price([5, 20, 30, 7])
    87
    >>> total_price([8, 4, 3])
    15
    >>> total_price([10, 100, 4])
    164
    """
    "*** YOUR CODE HERE ***"
    total = 0
    for num in prices:
        if num >= 20:
            num = num * 1.5
            total = total + num
        else:
            total = total + num
    return int(total)


def arange(start, end, step=1):
    """
    arange behaves just like np.arange(start, end, step).
    You only need to support positive values for step.

    >>> arange(1, 3)
    [1, 2]
    >>> arange(0, 25, 2)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    >>> arange(999, 1231, 34)
    [999, 1033, 1067, 1101, 1135, 1169, 1203]

    """
    "*** YOUR CODE HERE ***"
    grp = []
    grp.append(start)
    while start < (end-1):
        if (start + step) <= (end - 1):
            grp.append(start + step)
            start = start + step
        else:
            start = start + step
    return grp

    


def reverse_iter_for(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter_for([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    grp = []
    for i in lst:
        if i != 0:
            grp.append(lst[-i])
        else:
            grp.append(lst[i - 1])
    return grp
        



def reverse_iter_while(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter_while([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    rev_lst = []
    i = 0
    while i < len(lst):
        "*** YOUR CODE HERE ***"
        rev_lst.append(lst[-i - 1])
        i += 1
    return rev_lst

