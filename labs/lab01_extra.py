"""Optional questions for Lab 1"""

# While Loops

def triangular_sum(n):
    """
    >>> t_sum = triangular_sum(5)
    1
    3
    6
    10
    15
    >>> t_sum
    35
    """
    "*** YOUR CODE HERE ***"
    a = 1
    d = 1
    total = 0
    while a <= n:
        d = (a + 1) * a/2
        print(int(d))
        total = total + d
        a += 1
    return int(total)

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    state = False
    while n > 0:
        if n % 10 == 8:
            if state: 
                return True
            else:
                state = True
        else:
            state = False
        n = n // 10
    return False



# Boolean Operators

def right_triangle(a, b, c):
    """Determine whether a, b, and c can be sides of a right triangle
    >>> right_triangle(1, 1, 1)
    False
    >>> right_triangle(5, 3, 4)
    True
    >>> right_triangle(8, 10, 6)
    True
    """
    "*** YOUR CODE HERE ***"

