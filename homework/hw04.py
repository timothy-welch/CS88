######################
# Required Questions #
######################

def operation_inator(operation_string):
    """
    >>> identity = operation_inator('self')
    >>> identity(5)
    5
    >>> identity(6)
    6
    >>> add_one = operation_inator('add one')
    >>> add_one(2)
    3
    >>> add_one(3)
    4
    >>> mul_together = operation_inator('multiply together')
    >>> mul_together(0, 1)
    0
    >>> mul_together(3, 2)
    6
    >>> zero_to_self = operation_inator('zero to self')
    >>> zero_to_self(3)
    [0, 1, 2]
    >>> zero_to_self(1)
    [0]
    """
    "*** YOUR CODE HERE ***"
    if operation_string == 'self':
        return lambda x:x
    elif operation_string == 'add one':
        return lambda x: x+1
    elif operation_string == 'multiply together':
        return lambda a,b: a * b
    elif operation_string == 'zero to self':
        return lambda x: list(range(x))
    else:
        return 'I dont know that one'


def higher_order_lambdas():
    """
    Return a lambda function that takes in a multiplier and returns a lambda function that given an input will 
    return the input multiplied by the multiplier
    >>> hol = higher_order_lambdas()
    >>> doubles = hol(2)
    >>> doubles(3)
    6
    >>> hol = higher_order_lambdas()
    >>> triples = hol(3)
    >>> triples(4)
    12
    """
    "*** YOUR CODE HERE ***"
    return lambda x: lambda y: x*y

def lambda_curry2(f2):
    """
    Returns a Curried version of a two argument function func.
    >>> from operator import add
    >>> x = lambda_curry2(add)
    >>> y = x(3)
    >>> y(5)
    8
    """
    "*** YOUR CODE HERE ***"
    return lambda x: lambda y: f2(x,y)
    


def replace_all(d, x, y):
    """
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> e = replace_all(d, 3, 'poof')
    >>> e == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"
    dict = {}
    for key,value in d.items():
        if value == x:
            dict.update({key : y})
        else:
            dict.update({key: value})
    return dict
    


def merge_dict(dict1, dict2):
    """Returns a dictionary that is the result of two dictionaries being merged together. 
    Dictionaries are merged by adding up their values. You can assume that the same keys 
    appear in both dictionaries.
    >>> data8 = {"midterms":1, "projects":3}
    >>> data100 = {"midterms":2, "projects":3}
    >>> combined_exams = merge_dict(data8, data100)
    >>> combined_exams
    {'midterms': 3, 'projects': 6}
    >>> sunday_orders = {"pizza": 3, "hot dogs": 2, "fries": 5}
    >>> monday_orders = {"pizza": 1, "hot dogs": 1, "fries": 8}
    >>> combined_orders = merge_dict(sunday_orders, monday_orders)
    >>> combined_orders
    {'pizza': 4, 'hot dogs': 3, 'fries': 13}
    """
    "*** YOUR CODE HERE ***"
    dict = {}
    for d in (dict1, dict2):
        for k,v in d.items():
            if k in dict.keys():
                dict[k] += v
            else:
                dict[k] = v
    return dict

