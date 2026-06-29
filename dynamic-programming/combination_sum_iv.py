"""
Problem: Combination Sum IV
Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum-iv/

Given an array of distinct integers nums and a target integer, return the number
of possible combinations that add up to target. Order matters (permutations).

Example:
    Input: nums = [1, 2, 3], target = 4
    Output: 7
    Explanation: (1+1+1+1), (1+1+2), (1+2+1), (1+3), (2+1+1), (2+2), (3+1)

Approach: Bottom-up DP — O(target * n) time, O(target) space
"""


def combination_sum4(nums: list[int], target: int) -> int:
    # dp[i] = number of combinations that sum to i
    dp = [0] * (target + 1)
    dp[0] = 1  # One way to reach 0: choose nothing

    for i in range(1, target + 1):
        for num in nums:
            if num <= i:
                dp[i] += dp[i - num]

    return dp[target]


if __name__ == "__main__":
    print(combination_sum4([1, 2, 3], 4))   # 7
    print(combination_sum4([9], 3))          # 0
    print(combination_sum4([1, 2, 3], 0))   # 1
