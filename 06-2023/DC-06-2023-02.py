"""
Date: 06/02/2023
Time: 30m
Question: You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API.
API:    
record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
Algorithm Description: The algorithm ensures efficient time and space complexity, as it leverages the built-in functionality of the deque data structure to maintain the last N order IDs in a circular buffer.

"""

from collections import deque

class OrderLog:
    def __init__(self, N):
        self.log = deque(maxlen=N)

    def record(self, order_id):
        self.log.append(order_id)

    def get_last(self, i):
        if i <= len(self.log):
            return self.log[-i]
        else:
            return None


# Test Cases
# Test Case 1
log = OrderLog(5)
log.record(1001)
log.record(1002)
log.record(1003)
log.record(1004)
log.record(1005)
last_element = log.get_last(1)
print("Last element:", last_element) # Last element: 1005
# Test Case 2
log = OrderLog(5)
log.record(2001)
log.record(2002)
log.record(2003)
log.record(2004)
log.record(2005)
last_element = log.get_last(3)
print("Last element:", last_element) # Last element: 2003
# Test Case 3
log = OrderLog(3)
log.record(3001)
log.record(3002)
log.record(3003)
log.record(3004)
log.record(3005)
last_element = log.get_last(2)
print("Last element:", last_element) # Last element: 3004