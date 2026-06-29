"""
Problem: Same Tree
Difficulty: Easy
Link: https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check if they are the same.
Two trees are the same if they are structurally identical with the same node values.

Example:
    Input:  p = [1,2,3], q = [1,2,3]
    Output: True

Approach: Recursive DFS — O(n) time, O(h) space
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from node import TreeNode, list_to_tree


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    # Both None
    if not p and not q:
        return True
    # One is None but not the other, or values differ
    if not p or not q or p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == "__main__":
    p1, q1 = list_to_tree([1, 2, 3]), list_to_tree([1, 2, 3])
    print(is_same_tree(p1, q1))  # True

    p2, q2 = list_to_tree([1, 2]), list_to_tree([1, None, 2])
    print(is_same_tree(p2, q2))  # False

    p3, q3 = list_to_tree([1, 2, 1]), list_to_tree([1, 1, 2])
    print(is_same_tree(p3, q3))  # False
