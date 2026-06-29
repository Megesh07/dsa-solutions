"""
Problem: Validate Binary Search Tree
Difficulty: Medium
Link: https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST: left subtree < node < right subtree (strictly), for all nodes.

Example:
    Input:  [2, 1, 3]
    Output: True

Approach: DFS with valid range [min, max] — O(n) time, O(h) space
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from node import TreeNode, list_to_tree


def is_valid_bst(root: TreeNode | None) -> bool:
    def validate(node: TreeNode | None, min_val: float, max_val: float) -> bool:
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (
            validate(node.left, min_val, node.val) and
            validate(node.right, node.val, max_val)
        )

    return validate(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    root = list_to_tree([2, 1, 3])
    print(is_valid_bst(root))  # True

    root2 = list_to_tree([5, 1, 4, None, None, 3, 6])
    print(is_valid_bst(root2))  # False (4 < 5 but is right child)

    root3 = list_to_tree([5, 4, 6, None, None, 3, 7])
    print(is_valid_bst(root3))  # False (3 < 5 but in right subtree)
