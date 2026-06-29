"""
Problem: Serialize and Deserialize Binary Tree
Difficulty: Hard
Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Design an algorithm to serialize a binary tree to a string and deserialize it back.

Example:
    Input:  root = [1,2,3,null,null,4,5]
    Output: serialize then deserialize produces the same tree

Approach: BFS level-order encoding — O(n) serialize, O(n) deserialize
"""

import sys
import os
from collections import deque
sys.path.insert(0, os.path.dirname(__file__))
from node import TreeNode, list_to_tree, tree_to_list


SEPARATOR = ","
NULL = "null"


def serialize(root: TreeNode | None) -> str:
    """Encodes a tree to a single string."""
    if not root:
        return NULL

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(NULL)

    return SEPARATOR.join(result)


def deserialize(data: str) -> TreeNode | None:
    """Decodes encoded data to tree."""
    if data == NULL:
        return None

    values = data.split(SEPARATOR)
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if values[i] != NULL:
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] != NULL:
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    root = list_to_tree([1, 2, 3, None, None, 4, 5])
    encoded = serialize(root)
    print(f"Serialized: {encoded}")

    decoded = deserialize(encoded)
    print(f"Deserialized: {tree_to_list(decoded)}")  # [1, 2, 3, 4, 5]

    # Edge cases
    print(serialize(None))           # "null"
    print(tree_to_list(deserialize("null")))  # []
