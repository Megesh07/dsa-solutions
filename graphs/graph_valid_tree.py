"""
Problem: Graph Valid Tree
Difficulty: Medium
Link: https://leetcode.com/problems/graph-valid-tree/

Given n nodes (0 to n-1) and edges, determine if they form a valid tree.
A valid tree has exactly n-1 edges and is fully connected (no cycles).

Example:
    Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: True

Approach: Union-Find — O(n * alpha(n)) time
"""


def valid_tree(n: int, edges: list[list[int]]) -> bool:
    # A tree with n nodes must have exactly n-1 edges
    if len(edges) != n - 1:
        return False

    parent = list(range(n))
    rank = [0] * n

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int) -> bool:
        px, py = find(x), find(y)
        if px == py:
            return False  # Cycle detected
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True

    for u, v in edges:
        if not union(u, v):
            return False  # Cycle found

    return True


if __name__ == "__main__":
    print(valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))  # True
    print(valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))  # False (cycle)
    print(valid_tree(1, []))  # True (single node)
