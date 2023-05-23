"""
Date: 05/21/2023
Time: 1h 15m
Question: Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
Example: For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
Algorithm Description: The algorithm efficiently handles the presence of non-positive numbers and finds the first missing positive integer using in-place modifications. It runs in linear time and uses constant space.

"""

def first_missing_positive(nums):
    n = len(nums)

    # Separate Positive and Non-positive numbers
    j = 0
    for i in range(n):
        if nums[i] <= 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    nums = nums[j:]

    # Mark positive numbers by changing indices to negative
    for num in nums:
        index = abs(num) - 1
        if index < len(nums) and nums[index] > 0:
            nums[index] = -nums[index]

    # Find the missing number
    for i in range(len(nums)):
        if nums[i] > 0:
            return i + 1

    # If no missing positive number found, return the next positive number
    return len(nums) + 1


# Test case 1
nums1 = [3, 4, -1, 1]
result1 = first_missing_positive(nums1)
print(result1)
# Output: 2

# Test case 2
nums2 = [1, 2, 0]
result2 = first_missing_positive(nums2)
print(result2)
# Output: 3

# Test case 3
nums3 = [7, 8, 9, 11, 12]
result3 = first_missing_positive(nums3)
print(result3)
# Output: 1

# Test case 4
nums4 = [-1, -2, -3]
result4 = first_missing_positive(nums4)
print(result4)
# Output: 1

# Test case 5
nums5 = [0, 0, 0]
result5 = first_missing_positive(nums5)
print(result5)
# Output: 1
