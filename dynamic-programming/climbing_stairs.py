"""
Problem: Climbing Stairs
Difficulty: Easy
Link: https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can climb 1 or 2 steps. Return how many distinct ways to reach the top.

Example:
    Input: n = 5
    Output: 8

Approach: Dynamic Programming (Fibonacci variant) — O(n) time, O(1) space
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    prev1, prev2 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr

    return prev2


# Memoized recursive approach
from functools import lru_cache

@lru_cache(maxsize=None)
def climb_stairs_memo(n: int) -> int:
    if n <= 2:
        return n
    return climb_stairs_memo(n - 1) + climb_stairs_memo(n - 2)


if __name__ == "__main__":
    print(climb_stairs(2))  # 2
    print(climb_stairs(3))  # 3
    print(climb_stairs(5))  # 8
    print(climb_stairs(10)) # 89
