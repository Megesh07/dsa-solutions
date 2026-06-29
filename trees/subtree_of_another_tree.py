"""
Problem: Subtree of Another Tree
Difficulty: Easy
Link: https://leetcode.com/problems/subtree-of-another-tree/

Given the roots of two binary trees root and subRoot, return True if there is a subtree
of root with the same structure and node values as subRoot.

Example:
    Input:  root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: True

Approach: DFS + isSameTree — O(m * n) time, O(m + n) space
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from node import TreeNode, list_to_tree


def is_same_tree(s: TreeNode | None, t: TreeNode | None) -> bool:
    if not s and not t:
        return True
    if not s or not t or s.val != t.val:
        return False
    return is_same_tree(s.left, t.left) and is_same_tree(s.right, t.right)


def is_subtree(root: TreeNode | None, sub_root: TreeNode | None) -> bool:
    if not sub_root:
        return True
    if not root:
        return False

    if is_same_tree(root, sub_root):
        return True

    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)


if __name__ == "__main__":
    root = list_to_tree([3, 4, 5, 1, 2])
    sub = list_to_tree([4, 1, 2])
    print(is_subtree(root, sub))  # True

    root2 = list_to_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    print(is_subtree(root2, sub))  # False
