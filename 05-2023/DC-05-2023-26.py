"""
Date: 05/26/2023
Time: 45m
Question: Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
Example: [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
Algorithm Description: The key idea of the algorithm is to keep track of the maximum sum at each step, considering whether to include the current number or skip it. By iteratively updating the maximum sum, the algorithm efficiently computes the largest sum of non-adjacent numbers in the given list.

"""

def max_sum_non_adjacent(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    prev_max = nums[0]
    curr_max = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        curr_max_incl = nums[i] + prev_max
        curr_max = max(curr_max, curr_max_incl)
        prev_max = curr_max

    return curr_max


# Test Cases

# Test Case 1:
nums1 = [1, 2, 3, 1]
print(max_sum_non_adjacent(nums1))  # Output: 5

# Test Case 2:
nums2 = [2, 7, 9, 3, 1]
print(max_sum_non_adjacent(nums2))  # Output: 15

# Test Case 3:
nums3 = [5, 1, 1, 5]
print(max_sum_non_adjacent(nums3))  # Output: 11

# Test Case 4:
nums4 = [-1, -2, -3, -4, -5]
print(max_sum_non_adjacent(nums4))  # Output: -1

# Test Case 5:
nums5 = [1, 2, 3, 4, 5]
print(max_sum_non_adjacent(nums5))  # Output: 13
