"""
Date: 05/27/2023
Time: 1h 15m
Question: Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
Algorithm Description: The key idea of the algorithm is to utilize the time.sleep function to introduce the desired delay and then call the provided function f. This way, the algorithm provides a way to schedule the execution of a function after a certain time delay, as specified by the input n in milliseconds.

"""

import time

def job_scheduler(f, n):
    time.sleep(n / 1000)  
    f()  

def print_hello():
    print("Hello, world!")

job_scheduler(print_hello, 2000)


# Test Cases

# Test Case 1:
def print_message():
    print("Scheduled message!")

job_scheduler(print_message, 1000)  # Calls print_message() after a 1000-millisecond delay
# Output: "Scheduled message!" will be printed after a 1-second delay

# Test Case 2:
def greet(name):
    print("Hello, " + name + "!")

job_scheduler(lambda: greet("Alice"), 500)  # Calls greet("Alice") after a 500-millisecond delay
# Output: "Hello, Alice!" will be printed after a 0.5-second delay

# Test Case 3:
def calculate_square(num):
    print("Square of", num, "is", num ** 2)

job_scheduler(lambda: calculate_square(5), 2000)  # Calls calculate_square(5) after a 2000-millisecond delay
# Output: "Square of 5 is 25" will be printed after a 2-second delay

