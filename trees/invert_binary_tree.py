"""
Problem: Invert Binary Tree
Difficulty: Easy
Link: https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

Example:
    Input:
          4
         / \
        2   7
       / \ / \
      1  3 6  9
    Output:
          4
         / \
        7   2
       / \ / \
      9  6 3  1

Approach: Recursive DFS — O(n) time, O(h) space where h = tree height
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from node import TreeNode, list_to_tree, tree_to_list


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    if not root:
        return None

    # Swap left and right children
    root.left, root.right = root.right, root.left

    # Recursively invert both subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root


if __name__ == "__main__":
    root = list_to_tree([4, 2, 7, 1, 3, 6, 9])
    print(tree_to_list(invert_tree(root)))  # [4, 7, 2, 9, 6, 3, 1]

    root2 = list_to_tree([2, 1, 3])
    print(tree_to_list(invert_tree(root2)))  # [2, 3, 1]
