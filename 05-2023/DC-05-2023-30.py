"""
Date: 05/30/2023
Time: 45m
Question: Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
Example: Given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
Algorithm Description: By iterating through the string once and updating the window and dictionary accordingly, the algorithm efficiently finds the length of the longest substring that contains at most k distinct characters

"""

def longest_substring_length(k, s):
    start = 0
    end = 0
    char_counts = {}
    max_length = 0
    distinct_chars = 0

    while end < len(s):
        char_counts[s[end]] = char_counts.get(s[end], 0) + 1
        if char_counts[s[end]] == 1:
            distinct_chars += 1

        while distinct_chars > k:
            char_counts[s[start]] -= 1
            if char_counts[s[start]] == 0:
                distinct_chars -= 1
                del char_counts[s[start]]
            start += 1

        max_length = max(max_length, end - start + 1)
        end += 1

    return max_length

# Test Cases
# Test Case 1
k = 2
s = "abcba"
print(longest_substring_length(k, s))  # Output: 3
# Test Case 2
k = 3
s = "aabacbebebeb"
print(longest_substring_length(k, s))  # Output: 8
# Test Case 3
k = 1
s = "aaaaaaa"
print(longest_substring_length(k, s))  # Output: 7
# Test Case 4
k = 4
s = "abcdabcdabcd"
print(longest_substring_length(k, s))  # Output: 12
# Test Case 5
k = 2
s = "aab"
print(longest_substring_length(k, s))  # Output: 3
