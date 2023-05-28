"""
Date: 05/28/2023
Time: 55m
Question: Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
Example: Given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
Algorithm Description:

"""


def autocomplete(s, strings):
    results = []
    for string in strings:
        if string.startswith(s):
            results.append(string)
    return results


# Test Cases

# Test Case 1:
query1 = "s"
strings1 = ["strawberry", "apple", "apricot", "avocado"]
print(autocomplete(query1, strings1))
# Output: ['strawberry']

# Test Case 2:
query2 = "c"
strings2 = ["cat", "car", "cab", "dog", "cake"]
print(autocomplete(query2, strings2))
# Output: ['cat', 'car', 'cab']

# Test Case 3:
query3 = "fi"
strings3 = ["file", "folder", "finance", "fish", "find"]
print(autocomplete(query3, strings3))
# Output: ['file', 'finance', 'find']

# Test Case 4:
query4 = "zoo"
strings4 = ["cat", "dog", "fish", "bird"]
print(autocomplete(query4, strings4))
# Output: []

# Test Case 5:
query5 = "ab"
strings5 = ["abc", "abacus", "abide", "able", "above"]
print(autocomplete(query5, strings5))
# Output: ['abc', 'abacus', 'abide', 'able']
