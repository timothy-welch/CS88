######################
# Required Questions #
######################

# Probably a die-re situation

from operator import add, mul

def reduce(reducer, seq, start):
    """Reduce a sequence under a two-argument function starting from a start value.

    >>> def add(x, y):
    ...     return x + y
    >>> def mul(x, y):
    ...     return x*y
    >>> reduce(add, [1,2,3,4], 0)
    10
    >>> reduce(mul, [1,2,3,4], 0)
    0
    >>> reduce(mul, [1,2,3,4], 1)
    24
    """
    "*** YOUR CODE HERE ***"
    if seq == []: 
        return start #base case
    step = reducer(start, seq[0])
    return reduce(reducer, seq[1:], step)


def remove_last(x, lst):
    """Create a new list that is identical to lst but with the last
    element from the list that is equal to x removed.

    >>> remove_last(1,[])
    []
    >>> remove_last(1,[1])
    []
    >>> remove_last(1,[1,1])
    [1]
    >>> remove_last(1,[2,1])
    [2]
    >>> remove_last(1,[3,1,2])
    [3, 2]
    >>> remove_last(1,[3,1,2,1])
    [3, 1, 2]
    >>> remove_last(5, [3, 5, 2, 5, 11])
    [3, 5, 2, 11]
    """
    "*** YOUR CODE HERE ***"
    if len(lst) == 0: #base case
        return lst
    elif lst[-1] == x: #look at last number and delete if == x
        del lst[-1]
        return lst
    else:
        return remove_last(x, lst[ :len(lst)-1]) + [lst[-1]] #if not found, repeat with a shorter list


def map(f, seq):
    """
    Map a function f onto a sequence.

    >>> def double(x):
    ...     return x * 2
    >>> def square(x):
    ...     return x ** 2
    >>> def toLetter(x):
    ...     alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ...     return alpha[x%26]
    >>> map(double, [1,2,3,4])
    [2, 4, 6, 8]
    >>> map(square, [1, 2, 3, 4, 5, 10])
    [1, 4, 9, 16, 25, 100]
    >>> map(toLetter, [3, 0, 19, 0])
    ['d', 'a', 't', 'a']

    """
    "*** YOUR CODE HERE ***"
    if seq == []: #base case
        return []
    else:
        return [f(seq[0])] + map(f, seq[1:]) #apply function to first element, then move forward in the list


def hailstone_iterative(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone_iterative(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    count = 1
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n//2
            count +=1
        else:
            n = n*3 + 1
            count += 1
    print(n)
    return count
    

def hailstone_recursive(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone_recursive(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    if n == 1: #base case
        print(n)
        return 1
    elif n % 2 == 0: #recursive case 1
        print(n)
        return 1 + hailstone_recursive(n//2)
    else: #recursive case 2
        print(n)
        return 1 + hailstone_recursive(n*3+1)

def count_change(amount, coins):
    """Returns the number of ways to make change for amount.

    >>> coins = [50, 25, 10, 5, 1]
    >>> count_change(7, coins)
    2
    >>> count_change(100, coins)
    292
    >>> coins = [16, 8, 4, 2, 1]
    >>> count_change(7, coins)
    6
    >>> count_change(10, coins)
    14
    >>> count_change(20, coins)
    60
    """
    "*** YOUR CODE HERE ***"
    if amount == 0:
        return 1
    if amount <0 or not coins:
        return 0
    use_coin = count_change(amount - coins[0], coins)
    dont_use_coin = count_change(amount, coins[1:])
    return use_coin + dont_use_coin

