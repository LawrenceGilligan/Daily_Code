"""
Date: 05/29/2023
Time: 1h 15m
Question: (Step 1) There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters. (Step 2) What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
Algorithm Description:  By storing the results of subproblems in an array (dp), they avoid redundant calculations and efficiently compute the final count of unique ways to climb the staircase.

"""

# Step 1
def count_steps(N):
    if N == 0 or N == 1:
        return 1

    dp = [0] * (N + 1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N]

# Step 1 Test Cases
print(count_steps(2))  # Output: 2
print(count_steps(3))  # Output: 3
print(count_steps(4))  # Output: 5
print(count_steps(5))  # Output: 8
 
# Step 2
def count_steps2(N, X):

    dp = [0] * (N + 1)

    dp[0] = 1

    for i in range(1, N + 1):
        for x in X:
            if i >= x:
                dp[i] += dp[i - x]

    return dp[N]

# Step 2 Test Cases
X = {1, 3, 5}
print(count_steps2(4, X))  # Output: 3
print(count_steps2(5, X))  # Output: 5
print(count_steps2(6, X))  # Output: 8

