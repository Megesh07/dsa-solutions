"""
Problem: Lowest Common Ancestor of a Binary Search Tree
Difficulty: Medium
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a BST, find the Lowest Common Ancestor (LCA) of two given nodes p and q.
LCA is the lowest node that has both p and q as descendants.

Example:
    Input: root = [6,2,8,0,4,7,9], p = 2, q = 8
    Output: 6

Approach: BST property — O(h) time, O(1) space (h = height of tree)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from node import TreeNode, list_to_tree


def lowest_common_ancestor(
    root: TreeNode, p: TreeNode, q: TreeNode
) -> TreeNode:
    curr = root

    while curr:
        # Both nodes are in the right subtree
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        # Both nodes are in the left subtree
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        # Split point — this is the LCA
        else:
            return curr


if __name__ == "__main__":
    root = list_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p, q = TreeNode(2), TreeNode(8)
    print(lowest_common_ancestor(root, p, q).val)  # 6

    p2, q2 = TreeNode(2), TreeNode(4)
    print(lowest_common_ancestor(root, p2, q2).val)  # 2
