"""
Date: 5/18/2023
Time: 45m
Question: Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
Example: given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

"""

def sum(numbers, k):
    complements = set()

    for num in numbers:
        complement = k - num
        if complement in complements:
            return True
        complements.add(num)

    return False


# Test Cases
def test_sum():
    # Test case 1
    numbers = [1, 2, 3, 4, 5]
    k = 7
    assert sum(numbers, k) == True

    # Test case 2
    numbers = [1, 2, 3, 4, 5]
    k = 10
    assert sum(numbers, k) == False

    # Test case 3
    numbers = [3, 4, 1, 7, 9]
    k = 8
    assert sum(numbers, k) == True

    # Test case 4
    numbers = [2, 4, 6, 8, 10]
    k = 15
    assert sum(numbers, k) == False

    # Test case 5 (empty list)
    numbers = []
    k = 5
    assert sum(numbers, k) == False

    # Test case 6 (single element list)
    numbers = [5]
    k = 5
    assert sum(numbers, k) == False

    # Test case 7 (duplicate numbers)
    numbers = [1, 1, 2, 3, 4, 4, 5]
    k = 8
    assert sum(numbers, k) == True

    print("Test Cases Succesful")

test_sum()
