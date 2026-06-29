"""
Problem: Longest Increasing Subsequence
Difficulty: Medium
Link: https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example:
    Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
    Output: 4  (2, 3, 7, 101)

Approach 1: DP — O(n^2) time, O(n) space
Approach 2: Binary Search (Patience Sorting) — O(n log n) time, O(n) space
"""

import bisect


def length_of_lis_dp(nums: list[int]) -> int:
    """O(n^2) DP approach."""
    n = len(nums)
    dp = [1] * n  # dp[i] = LIS ending at index i

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def length_of_lis(nums: list[int]) -> int:
    """O(n log n) Binary Search approach (Patience Sorting)."""
    tails = []  # tails[i] = smallest tail of IS with length i+1

    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num  # Replace to keep tails as small as possible

    return len(tails)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(length_of_lis_dp(nums))  # 4
    print(length_of_lis(nums))     # 4

    print(length_of_lis([0, 1, 0, 3, 2, 3]))  # 4
    print(length_of_lis([7, 7, 7, 7, 7]))     # 1
