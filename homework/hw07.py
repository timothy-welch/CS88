# 00P

class Person(object):
    """
    >>> steven = Person("Steven")
    >>> barb = Person("Barb")
    >>> steven.say("Hello")
    'Hello'
    >>> steven.repeat()
    'Hello'
    >>> steven.greet()
    'Hello, my name is Steven'
    >>> barb.ask("listen to me repeat myself")
    'Would you please listen to me repeat myself'
    >>> barb.repeat()
    'Would you please listen to me repeat myself'
    >>> steven.repeat()
    'Hello, my name is Steven'
    """
    def __init__(self, name):
        self.name = name
        "*** YOUR CODE HERE ***"

    def say(self, stuff):
        "*** YOUR CODE HERE ***"
        self.stuff = stuff
        return self.stuff

    def ask(self, stuff):
        self.stuff = self.say("Would you please " + stuff)
        return self.say("Would you please " + stuff)

    def greet(self):
        self.stuff = self.say("Hello, my name is " + self.name)
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        "*** YOUR CODE HERE ***"
        return self.stuff



class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> sophia_account = Account('Sophia')
    >>> sophia_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> sophia_account.transactions
    [('deposit', 1000000)]
    >>> sophia_account.withdraw(100)      # buying dinner
    999900
    >>> sophia_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02
    balance = 1000

    def __init__(self, account_holder, balance = 0):
        self.balance = balance
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        self.transactions.append(('deposit', amount))
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        self.transactions.append(('withdraw', amount))
        if amount > self.balance:
            return 'Insufficient funds'
        else:
            self.balance = self.balance - amount
            return self.balance


class VendingMachine(object):
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Sold out'
    >>> v.restock(2)
    'Stock: 2'
    >>> v.vend()
    'Need $10 more'
    >>> v.deposit(7)
    'Current Balance: $7'
    >>> v.vend()
    'Need $3 more'
    >>> v.deposit(5)
    'Current Balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change'
    >>> v.deposit(10)
    'Current Balance: $10'
    >>> v.vend()
    'Here is your candy'
    >>> v.deposit(15)
    'Sold out. Here is your $15'
    """
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.stock = 0
        self.balance = 0

    "*** YOUR CODE HERE ***"
    def restock(self, amount):
        self.stock = self.stock + amount
        return 'Stock: ' + str(self.stock)
    
    def deposit(self, amount): #add money to self.balance, return self.balance
        if self.stock == 0:
            return 'Sold out. Here is your $'+str(amount)
        else:
            self.balance = self.balance + amount
            return 'Current Balance: $' + str(self.balance)
    
    def vend(self):
        if self.stock == 0:
            return 'Sold out'
        if self.balance < self.price:
            return 'Need $'+ str(self.price-self.balance) +' more'
        elif self.balance > self.price:
            change = self.balance - self.price
            self.balance = 0 
            self.stock -= 1
            return 'Here is your ' + str(self.product) + ' and $' + str(change) + ' change'
        elif self.balance == self.price:
            self.balance = self.balance - self.price
            self.stock -= 1
            return 'Here is your candy'


class Arr88():
    """
    Arr88 is an object similar to Data 8 numpy arrays.
    Here the internel representation is a list
    """
    def __init__(self, values):
        # Check that all values are the same type, else it errors
        if len(values) > 1:
            assert all([type(values[0]) == type(values[i]) for i in range(len(values))]), "Arr88 must be of homogeneous type"
        self._values = values

    # DO NOT CHANGE THE __repr__
    # This displays the Arr88 nicely in the terminal
    def __repr__(self):
        return "Arr88(" + str(self._values) + ')'

    def __len__(self):
        """ Return the length of the Arr88

        >>> arr88 = Arr88([1, 2, 3])
        >>> len(arr88)
        3
        >>> arr88 = Arr88([1, 2, 3, 4])
        >>> len(arr88)
        4
        """
        "*** YOUR CODE HERE ***"
        return len(self._values)
        

    def item(self, i):
        """
        Get the item of the Arr88 at index i
        >>> arr88 = Arr88([1, 2, 3])
        >>> arr88.item(1)
        2
        >>> arr88.item(0)
        1
        """
        "*** YOUR CODE HERE ***"
        return self._values[i]
        

    def __add__(self, arr88):
        """ Add two Arr88s of the same length element by element

        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88b = Arr88([4, 5, 6])
        >>> arr88a + arr88b
        Arr88([5, 7, 9])
        >>> arr88a # We aren't mutating arr88a
        Arr88([1, 2, 3])
        >>> arr88a = Arr88(['He', 'Wor', '!'])
        >>> arr88b = Arr88(['llo', 'ld', ''])
        >>> arr88c = arr88a + arr88b
        >>> arr88c
        Arr88(['Hello', 'World', '!'])
        """
        # Checks that the lengths are the same
        assert len(self) == len(arr88), "Arr88's of different len"
        "*** YOUR CODE HERE ***"
        return Arr88([self._values[i] + arr88._values[i]for i in range(len(self._values))])
        

    def __mul__(self, arr88):
        """ Multiply two Arr88s of the same length componentwise

        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88b = Arr88([4, 5, 6])
        >>> arr88a * arr88b
        Arr88([4, 10, 18])
        >>> arr88a # We aren't mutating arr88a
        Arr88([1, 2, 3])
        >>> arr88a = Arr88(['Na', 'Batman', '!'])
        >>> arr88b = Arr88([10, 1, 5])
        >>> arr88c = arr88a * arr88b
        >>> arr88c
        Arr88(['NaNaNaNaNaNaNaNaNaNa', 'Batman', '!!!!!'])
        """
        # Checks that the lengths are the same
        assert len(self) == len(arr88), "Arr88's of different len"
        "*** YOUR CODE HERE ***"
        return Arr88([self._values[i] * arr88._values[i]for i in range(len(self._values))])
        

    def negate(self):
        """Negate an Arr88 with mutation

        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88b = Arr88([4.0, -5.5, 0.0])
        >>> arr88a.negate()
        >>> arr88a
        Arr88([-1, -2, -3])
        >>> arr88b.negate()
        >>> arr88b
        Arr88([-4.0, 5.5, -0.0])
        """
        "*** YOUR CODE HERE ***"
        for i in range(len(self._values)):
            self._values[i] = self._values[i]*-1
        


    def apply(self, func):
        """ Apply a function to an Arr88

        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88a.apply(lambda x : x * x)
        Arr88([1, 4, 9])
        >>> arr88a # We aren't mutating arr88a
        Arr88([1, 2, 3])
        >>> arr88b = Arr88([lambda x: x, lambda x: x + 1, lambda x: x + 2])
        >>> arr88c = arr88b.apply(lambda f: f(1))
        >>> arr88c
        Arr88([1, 2, 3])
        """
        "*** YOUR CODE HERE ***"
        lst = []
        for i in range(len(self._values)):
            lst.append( func(self._values[i]))
        return Arr88(lst)
        




