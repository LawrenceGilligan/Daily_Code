"""
Date: 05/22/2023
Time: 45m
Question: cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
Algorithm Description: The cons function constructs a pair by taking two elements a and b and returning a function pair that can be used to access those elements. The car function takes a pair and returns the first element of the pair by calling pair with a function that only returns the first argument. Similarly, the cdr function takes a pair and returns the last element of the pair by calling pair with a function that only returns the second argument.

"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def get_first(a, b):
        return a
    return pair(get_first)

def cdr(pair):
    def get_last(a, b):
        return b
    return pair(get_last)

# Pair of cons
pair = cons(3, 4)


# Test case 1
pair1 = cons(3, 4)
first_element1 = car(pair1)
last_element1 = cdr(pair1)
print(first_element1)  # Output: 3
print(last_element1)   # Output: 4

# Test case 2
pair2 = cons(0, -1)
first_element2 = car(pair2)
last_element2 = cdr(pair2)
print(first_element2)  # Output: 0
print(last_element2)   # Output: -1

# Test case 3
pair3 = cons("Hello", "World")
first_element3 = car(pair3)
last_element3 = cdr(pair3)
print(first_element3)  # Output: "Hello"
print(last_element3)   # Output: "World"

# Test case 4
pair4 = cons([1, 2, 3], [4, 5, 6])
first_element4 = car(pair4)
last_element4 = cdr(pair4)
print(first_element4)  # Output: [1, 2, 3]
print(last_element4)   # Output: [4, 5, 6]
