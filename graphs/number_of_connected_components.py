"""
Problem: Number of Connected Components in an Undirected Graph
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

Given n nodes (0 to n-1) and edges, return the number of connected components.

Example:
    Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2

Approach: Union-Find (Disjoint Set Union) — O(n * alpha(n)) nearly O(n)
"""


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already in same component

        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        self.components -= 1
        return True


def count_components(n: int, edges: list[list[int]]) -> int:
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.components


if __name__ == "__main__":
    print(count_components(5, [[0, 1], [1, 2], [3, 4]]))          # 2
    print(count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))  # 1
    print(count_components(3, []))                                   # 3
