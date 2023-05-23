"""
Date: 05/19/2023
Time: 43m
Question: Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
Example: If our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Algorithm Description: The algorithm computes the products of the elements to the left and right of each index separately, avoiding the use of division. By traversing nums twice, it effectively computes the product of all numbers except the one at each index without using division.

"""

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Compute elements to the left of the index
    left_product = 1
    for i in range(n):
        result[i] *= left_product
        left_product *= nums[i]

    # Compute elements to the right of the index
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result


# Test case 1
nums1 = [1, 2, 3, 4, 5]
result1 = product_except_self(nums1)
print(result1)
# Output: [120, 60, 40, 30, 24]

# Test case 2
nums2 = [2, 4, 6, 8]
result2 = product_except_self(nums2)
print(result2)
# Output: [192, 96, 64, 48]

# Test case 3
nums3 = [1, 2, 3, 4, 5, 6]
result3 = product_except_self(nums3)
print(result3)
# Output: [720, 360, 240, 180, 144, 120]
