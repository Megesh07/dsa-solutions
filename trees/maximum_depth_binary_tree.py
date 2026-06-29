"""
Problem: Maximum Depth of Binary Tree
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.
Maximum depth is the number of nodes along the longest path from root to leaf.

Example:
    Input:  [3, 9, 20, null, null, 15, 7]
    Output: 3

Approach: Recursive DFS — O(n) time, O(h) space
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from node import TreeNode, list_to_tree


def max_depth(root: TreeNode | None) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# Iterative BFS approach
from collections import deque

def max_depth_bfs(root: TreeNode | None) -> int:
    if not root:
        return 0

    depth = 0
    queue = deque([root])

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth


if __name__ == "__main__":
    root = list_to_tree([3, 9, 20, None, None, 15, 7])
    print(max_depth(root))      # 3
    print(max_depth_bfs(root))  # 3

    root2 = list_to_tree([1, None, 2])
    print(max_depth(root2))     # 2
