"""
Date: 05/24/2023
Time: 30m
Question: Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
Example: The message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'. You can assume that the messages are decodable. For example, '001' is not allowed.
Algorithm Description: The algorithm utilizes dynamic programming to build up the number of ways to decode the message by considering the possibilities of single-digit and two-digit decodings at each step. By efficiently updating the dp array, it avoids redundant computations and provides the count of the number of ways the encoded message can be decoded.

"""

def num_decodings(s):
    n = len(s)
    if n == 0 or s[0] == '0':
        return 0

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        if s[i - 1] != '0':
            dp[i] = dp[i - 1]

        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]

# Test Cases
print(num_decodings("12"))  # Output: 2
print(num_decodings("226"))  # Output: 3
print(num_decodings("0"))  # Output: 0
print(num_decodings("06"))  # Output: 0
print(num_decodings("10"))  # Output: 1
print(num_decodings("27"))  # Output: 1
print(num_decodings("111"))  # Output: 3
