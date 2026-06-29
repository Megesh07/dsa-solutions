"""
Problem: Clone Graph
Difficulty: Medium
Link: https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Example:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: Deep copy of the same graph

Approach: DFS + Hash Map (old node -> cloned node) — O(V + E) time, O(V) space
"""


class GraphNode:
    def __init__(self, val: int = 0, neighbors: list["GraphNode"] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: GraphNode | None) -> GraphNode | None:
    if not node:
        return None

    cloned = {}  # Maps original node -> its clone

    def dfs(curr: GraphNode) -> GraphNode:
        if curr in cloned:
            return cloned[curr]

        clone = GraphNode(curr.val)
        cloned[curr] = clone

        for neighbor in curr.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)


def build_graph(adj_list: list[list[int]]) -> GraphNode | None:
    """Helper: Build graph from adjacency list (1-indexed)."""
    if not adj_list:
        return None

    nodes = {i + 1: GraphNode(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


if __name__ == "__main__":
    original = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
    cloned_root = clone_graph(original)
    print(f"Original node 1 val: {original.val}")
    print(f"Cloned node 1 val:   {cloned_root.val}")
    print(f"Are they different objects? {original is not cloned_root}")
