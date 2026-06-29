"""
Problem: Binary Tree Level Order Traversal
Difficulty: Medium
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values
(i.e., from left to right, level by level).

Example:
    Input:  [3, 9, 20, null, null, 15, 7]
    Output: [[3], [9, 20], [15, 7]]

Approach: BFS with a queue — O(n) time, O(n) space
"""

import sys
import os
from collections import deque
sys.path.insert(0, os.path.dirname(__file__))
from node import TreeNode, list_to_tree


def level_order(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


if __name__ == "__main__":
    root = list_to_tree([3, 9, 20, None, None, 15, 7])
    print(level_order(root))  # [[3], [9, 20], [15, 7]]

    root2 = list_to_tree([1])
    print(level_order(root2))  # [[1]]

    print(level_order(None))   # []
