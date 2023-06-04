"""
Date: 05/31/2023
Time: 40m
Question: The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
Algorithm Description: The algorithm leverages the random generation of points within a square and the relationship between the area of the quarter circle and the area of the square to estimate the value of π. By increasing the number of random points, the algorithm converges towards a more accurate estimation of π.

"""

import random
from math import sqrt

def estimate_pi():
    total_points = 0
    points_inside_circle = 0

    for _ in range(1000000):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = sqrt(x**2 + y**2)

        if distance <= 1:
            points_inside_circle += 1

        total_points += 1

    pi_estimate = 4 * (points_inside_circle / total_points)

    pi_estimate = round(pi_estimate, 3)

    return pi_estimate


# Test Cases
# Test Case 1
pi_estimate = estimate_pi()
print("Estimated value of π:", pi_estimate)
# Test Case 2
pi_estimate = estimate_pi()
print("Estimated value of π:", pi_estimate)
# Test Case 3
pi_estimate = estimate_pi()
print("Estimated value of π:", pi_estimate)


