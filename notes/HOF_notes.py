#### -- Higher Order Funcitons Lecture 2/6/23: map(), filter(), reduce() -- takes in functions to act on a sequence -- ###

##map() transforms every item in the list. input = function, sequence. output = sequence.
numbers = range(0,10)
def square(n):
    return n * n

#we could square everything in numbers through list comprehnsion
[square(x) for x in numbers]

#OR use map instead. Note: it returns a "map" variable -> convert to list
lst = list(map(square, numbers))
q2 = list(map(square, range(5)))

cal = 'The University of California at Berkeley'
words = cal.split(' ')

def shout(word):
    return word.upper()

#this returns an error --  list(map(shout(words)))

def add_one(n):
    return n + 1

lst1 = list(map(add_one, range(10)))

##filter() returns a list with fewer items
def is_even(n):
    return n % 2 ==0 

#filters for all even numbers
list(filter(is_even, numbers))


def is_uppercase(word):
    return word[0].capitalize() == word[0]

#filters for all upper case words
list(filter(is_uppercase, words))

#How can we square all of the even numbers in our list? [0, 4, 16, ...]
#combining map and filter
list(map(square, filter(is_even, numbers)))

### -reduce() "Combines" items together - probably doesn't return a list. 
# input is: a 2 item function, sequence. output: an item
#have to load these functions to really use reduce
from operator import add, mul, concat
from functools import reduce

#returns 3
reduce(add, [1, 2])
#returns 6
reduce(add, [1,2,3])

#returns 24
reduce(mul, range(1,5))

#takes the text and shoves it together
reduce(concat, words)

def long_word(n):
    return len(n) > 3

def first_letter(n):
    return n[0]

def acronym(word):
    return list(map(first_letter, filter(long_word, word)))

#### -- Higher Order Funcitons Lecture 2/8/23 -- ####

def add_2(n):
    return n + 2

#adapting our code
def keep_words(word):
    specials = ['Los']
    return word in specials or long_word(word)

copycats = "University of California at Los Angeles"

### A function that returns(makes) a function :
def leq_maker(c):
    def leq(val):
        return val <= c
    return leq

less_3 = leq_maker(3)
less_3(4)

### Environment Diagrams
