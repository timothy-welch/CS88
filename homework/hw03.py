######################
# Required Questions #
######################

def add_matrices(x, y):
    """
    >>> matrix1 = [[1, 3],
    ...            [2, 0]]
    >>> matrix2 = [[-3, 0],
    ...            [1, 2]]
    >>> add_matrices(matrix1, matrix2)
    [[-2, 3], [3, 2]]
    >>> matrix4 = [[ 1, -2,  3],
    ...            [-4,  5, -6]]
    >>> matrix5 = [[-1,  2, -3],
    ...            [ 4, -5,  6]]
    >>> add_matrices(matrix4, matrix5)
    [[0, 0, 0], [0, 0, 0]]
    """
    "*** YOUR CODE HERE ***"
    return [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]


def mul_by_num(factor):
    """
    Returns a function that takes one argument and
    returns the product of factor and that argument.
    >>> x = mul_by_num(5)
    >>> y = mul_by_num(2)
    >>> x(3)
    15
    >>> y(-4)
    -8
    """
    "*** YOUR CODE HERE ***"
    def multiple(x):
        return x * factor
    return multiple 
    


def make_derivative(f):
    """Returns a function that approximates the derivative of f.

    Recall that f'(a) = (f(a + h) - f(a)) / h as h approaches 0. We will
    approximate the derivative by choosing a very small value for h.

    >>> def square(x): 
    ...     # equivalent to: square = lambda x: x*x
    ...     return x*x
    >>> derivative = make_derivative(square)
    >>> result = derivative(3)
    >>> round(result, 3) # approximately 2*3
    6.0
    """
    h=0.00001
    "*** YOUR CODE HERE ***"
    def deriv(a):
        return (f(a + h) - f(a))/h
    return deriv


def count_cond(mystery_function, n):
    """
    >>> def divisible(n, i):
    ...     return n % i == 0
    >>> count_cond(divisible, 2) # 1, 2
    2
    >>> count_cond(divisible, 4) # 1, 2, 4
    3
    >>> count_cond(divisible, 12) # 1, 2, 3, 4, 6, 12
    6

    >>> def is_prime(n, i):
    ...     return count_cond(divisible, i) == 2
    >>> count_cond(is_prime, 2) # 2
    1
    >>> count_cond(is_prime, 3) # 2, 3
    2
    >>> count_cond(is_prime, 4) # 2, 3
    2
    >>> count_cond(is_prime, 5) # 2, 3, 5
    3
    >>> count_cond(is_prime, 20) # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    def func(n):
        i, count = 1,0
        while i <= n:
            if mystery_function(n, i):
                count +=1
            i += 1
        return count
    return func(n)
    


def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function
    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def again(n):
        def func(k):
            count = 0
            for i in range(n):
                if count == 0:
                    count += 1
                    k = f1(k)
                elif count == 1:
                    count += 1
                    k = f2(k)
                elif count == 2:
                    count = 0
                    k = f3(k)
            return k
        return func
    return again




def store_word(secret):
    """
    >>> word_len, guess_word = store_word("cake")
    >>> word_len
    4
    >>> guess_word("corn")
    [True, False, False, False]
    >>> guess_word("come")
    [True, False, False, True]
    >>> guess_word("cake")
    [True, True, True, True]
    >>> word_len, guess_word = store_word("pop")
    >>> word_len
    3
    >>> guess_word("ate")
    [False, False, False]
    >>> guess_word("top")
    [False, True, True]
    >>> guess_word("pop")
    [True, True, True]
    """
    "*** YOUR CODE HERE ***"
    def guess_word(guess):
        result = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                result.append(True)
            else:
                result.append(False)
        return result
    return len(secret), guess_word
