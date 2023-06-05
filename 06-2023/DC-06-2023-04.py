"""
Date: 06/04/2023
Time: 25m
Question: Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
Algorithm Description: The algorithm slides a window of length k over the input array and finds the maximum value within each window. By iterating through the array and updating the sliding window, we obtain the maximum values of all subarrays of length k.

"""

def max_values_of_subarrays(arr, k):
    result = []

    for i in range(len(arr) - k + 1):
        subarray = arr[i:i+k]
        max_value = max(subarray)
        result.append(max_value)

    return result

# Test Cases
# Test Case 1
print(max_values_of_subarrays([1, 3, -1, -3, 5, 3, 6, 7], 3))
# Output: [3, 3, 5, 5, 6, 7]

# Test Case 2
print(max_values_of_subarrays([9, 11, 2, 1, 8, 7], 2))
# Output: [11, 11, 2, 8, 8]

# Test Case 3
print(max_values_of_subarrays([4, 5, 6, 7, 8], 1))
# Output: [4, 5, 6, 7, 8]
