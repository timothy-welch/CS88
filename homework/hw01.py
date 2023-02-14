"""Homework 1."""

def odd(number):
    """Return whether the number is odd.

    >>> odd(2)
    False
    >>> odd(5)
    True
    """
    "*** YOUR CODE HERE ***"
    if number % 2 == 0 :
        return False
    else :
        return True


from math import sqrt

def distance(x1, y1, x2, y2):
    """Calculates the Euclidian distance between two points (x1, y1) and (x2, y2)

    >>> distance(1, 1, 1, 2)
    1.0
    >>> distance(1, 3, 1, 1)
    2.0
    >>> distance(1, 2, 3, 4)
    2.8284271247461903
    """
    "*** YOUR CODE HERE ***"
    c = (x1 - x2) * (x1 - x2)
    d = (y1 - y2) * (y1 - y2)
    return sqrt(c + d)

def distance3d(x1, y1, z1, x2, y2, z2):
    """Calculates the 3D Euclidian distance between two points (x1, y1, z1) and
    (x2, y2, z2).

    >>> distance3d(1, 1, 1, 1, 2, 1)
    1.0
    >>> distance3d(2, 3, 5, 5, 8, 3)
    6.164414002968976
    """
    "*** YOUR CODE HERE ***"
    c = (x1 - x2) * (x1 - x2)
    d = (y1 - y2) * (y1 - y2)
    e = (z1 - z2) * (z1 - z2)
    return sqrt(c + d + e)

from operator import add, sub
def absol(n) :
    if n < 0 :
        n = n * -1
    return n

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-5, -1)
    -4
    """
    if b < 0:
        f = a + absol(b)
    else:
        f = a + b
    return f


from math import sqrt

def quadratic(a, b, c):
    """
    >>> quadratic(1, 0, -1)
    (1.0, -1.0)
    >>> quadratic(1, 2, 1)
    (-1.0, -1.0)
    >>> quadratic(1, 3, -4)
    (1.0, -4.0)
    """
    "*** YOUR CODE HERE ***"
    e = 4 * a * c
    b2 = b * b
    b = b * -1
    s = sqrt(b2 - e)
    x1 = (b + s) / (2 * a)
    x2 = (b - s) / (2 * a)
    return x1, x2


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    total = 1
    if k == 0 :
        return 1
    else :
        while k > 0 :
            total = total * n 
            n -= 1
            k -= 1
        return total 




def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
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
    b = 1
    print(int(n)) 
    while n > 1:
        if n % 2 == 0 :
            n = n/2
            print(int(n))
            b += 1
        else:
            n = (n*3) + 1
            print(int(n))
            b += 1
    return b

    

