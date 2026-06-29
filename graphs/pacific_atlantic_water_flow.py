"""
Problem: Pacific Atlantic Water Flow
Difficulty: Medium
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

Given an m x n matrix of heights, return a list of grid coordinates where water
can flow to both the Pacific (top/left) and Atlantic (bottom/right) oceans.
Water flows from high to equal/lower cells.

Example:
    Input:  heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Approach: Reverse BFS from each ocean boundary — O(m * n) time
"""

from collections import deque


def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    rows, cols = len(heights), len(heights[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(starts: list[tuple]) -> set:
        visited = set(starts)
        queue = deque(starts)
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]
                ):
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return visited

    # Pacific touches top row and left column
    pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(1, rows)]
    # Atlantic touches bottom row and right column
    atlantic_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows - 1)]

    pacific = bfs(pacific_starts)
    atlantic = bfs(atlantic_starts)

    return [[r, c] for r, c in pacific & atlantic]


if __name__ == "__main__":
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    print(sorted(pacific_atlantic(heights)))
    # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
