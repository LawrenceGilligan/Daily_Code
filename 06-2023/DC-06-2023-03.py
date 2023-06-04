"""
Date: 06/03/2023
Time: 1h 30m
Question: Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
Algorithm Description: The algorithm utilizes a stack to keep track of the lengths of directories at each level. It simulates traversing the file system hierarchy and updates the stack as it encounters new directories and removes directories when going back to parent directories. The length of each directory or file is calculated by subtracting the depth from the length of the element. The maximum length is updated whenever a file is encountered. Finally, the algorithm returns the length of the longest absolute path to a file, or 0 if no file is found.

"""

def length_longest_path(file_system):
    elements = file_system.split('\n')
    stack = []
    max_length = 0

    for element in elements:
        depth = element.count('\t')
        while len(stack) > depth:
            stack.pop()

        length = len(element) - depth

        if '.' in element:
            max_length = max(max_length, len(stack) + length)
        else:
            stack.append(length + 1)  # Add 1 for the directory separator '/'

    if max_length == 0:
        return 0
    else:
        return max_length


# Test Cases
# Test Case 1 (Basic test case)
file_system = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
length = length_longest_path(file_system)
print(length)  # Output: 10

# Test Case 2 (File system with multiple files)
file_system = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tfile2.ext\n\tsubdir2\n\t\tsubsubdir\n\t\t\tfile3.ext"
length = length_longest_path(file_system)
print(length)  # Output: 12

# Test Case 3 (File system with no files)
file_system = "dir\n\tsubdir1\n\tsubdir2\n\t\tsubsubdir"
length = length_longest_path(file_system)
print(length)  # Output: 0

# Test Case 4 (File system with single-character directory names)
file_system = "a\n\tb\n\t\tc\n\t\t\td.ext"
length = length_longest_path(file_system)
print(length)  # Output: 8

# Test Case 5 (File system with empty directories)
file_system = "dir\n\tsubdir1\n\t\t\n\tsubdir2\n\t\t\n\t\t\tfile.ext"
length = length_longest_path(file_system)
print(length)  # Output: 11
