"""
Date: 05/20/2023
Time: 1h
Question: Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
Example: class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
Algorithm Description: The serialize function converts each node into a comma-separated string. The deserialize function reconstructs the binary tree by splitting the serialized string.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root:
        return "None,"

    serialized = str(root.val) + ","
    serialized += serialize(root.left)
    serialized += serialize(root.right)
    return serialized

def deserialize(s):
    def helper(values):
        if values[0] == "None":
            values.pop(0)
            return None

        root = TreeNode(int(values[0]))
        values.pop(0)
        root.left = helper(values)
        root.right = helper(values)
        return root

    values = s.split(",")
    return helper(values[:-1])


# Test case 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(5)

serialized_tree1 = serialize(root1)
print(serialized_tree1)
# Output: "1,2,None,None,3,4,None,None,5,None,None,"

deserialized_tree1 = deserialize(serialized_tree1)
print(deserialized_tree1.val)
# Output: 1
print(deserialized_tree1.left.val)
# Output: 2
print(deserialized_tree1.right.val)
# Output: 3
print(deserialized_tree1.right.left.val)
# Output: 4
print(deserialized_tree1.right.right.val)
# Output: 5


# Test case 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

serialized_tree2 = serialize(root2)
print(serialized_tree2)
# Output: "1,2,None,None,3,None,None,"

deserialized_tree2 = deserialize(serialized_tree2)
print(deserialized_tree2.val)
# Output: 1
print(deserialized_tree2.left.val)
# Output: 2
print(deserialized_tree2.right.val)
# Output: 3


# Test case 3
root3 = None

serialized_tree3 = serialize(root3)
print(serialized_tree3)
# Output: "None,"

deserialized_tree3 = deserialize(serialized_tree3)
print(deserialized_tree3)
# Output: None