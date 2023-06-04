"""
Date: 06/01/2023
Time: 35m
Question: Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
Algorithm Description: The algorithm works by maintaining a reservoir of size 1, initially empty, to hold the current randomly selected element. As each new element is encountered, the probability of it being selected as the random element is adjusted by dividing 1 by the current count of elements encountered. This ensures that each element has an equal chance of being selected at any given step.

"""

import random

def select_random_element(stream):
    result = None
    count = 0

    for i, element in enumerate(stream):
        count += 1

        # Update the selected element with probability 1/count
        if random.randint(1, count) == 1:
            result = element

    return result


# Test Cases
# Test Case 1
stream = [1, 2, 3, 4, 5]
random_element = select_random_element(stream)
print("Random element:", random_element)
# Test Case 2
stream = [10, 20, 30, 40, 50, 60]
random_element = select_random_element(stream)
print("Random element:", random_element)
# Test Case 3
stream = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
random_element = select_random_element(stream)
print("Random element:", random_element)