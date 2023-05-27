"""
Date: 05/25/2023
Time: 35m
Question: A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Algorithm Description: The algorithm uses recursion to traverse the binary tree and checks if each subtree is a unival subtree based on the values of its nodes. By recursively counting unival subtrees in each subtree, it provides the total count of unival subtrees in the binary tree.

"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_unival(node):
    if node is None:
        return True, None

    left_unival, left_val = is_unival(node.left)
    right_unival, right_val = is_unival(node.right)

    if (left_unival and right_unival and
            (left_val is None or left_val == node.val) and
            (right_val is None or right_val == node.val)):
        return True, node.val
    else:
        return False, node.val


def count_unival_subtrees(root):
    if root is None:
        return 0

    is_root_unival, _ = is_unival(root)
    count_left = count_unival_subtrees(root.left)
    count_right = count_unival_subtrees(root.right)

    return count_left + count_right + (1 if is_root_unival else 0)


# Test Cases
# Test Case 1:
#     1
#    / \
#   1   1
#  / \   \
# 1   1   1
root1 = TreeNode(1)
root1.left = TreeNode(1)
root1.right = TreeNode(1)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(1)
root1.right.right = TreeNode(1)
print(count_unival_subtrees(root1))  # Output: 6

# Test Case 2:
#     2
#    / \
#   2   2
#  / \   \
# 2   3   2
root2 = TreeNode(2)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(2)
print(count_unival_subtrees(root2))  # Output: 4

# Test Case 3:
#     5
#    / \
#   5   5
#  / \   \
# 1   5   5
root3 = TreeNode(5)
root3.left = TreeNode(5)
root3.right = TreeNode(5)
root3.left.left = TreeNode(1)
root3.left.right = TreeNode(5)
root3.right.right = TreeNode(5)
print(count_unival_subtrees(root3))  # Output: 4
