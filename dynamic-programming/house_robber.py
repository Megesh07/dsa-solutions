"""
Problem: House Robber
Difficulty: Medium
Link: https://leetcode.com/problems/house-robber/

You are a robber. Given an array of non-negative integers nums representing
the amount of money in each house, return the maximum amount you can rob
without robbing two adjacent houses.

Example:
    Input: nums = [2, 7, 9, 3, 1]
    Output: 12  (rob houses 0, 2, 4 → 2 + 9 + 1 = 12)

Approach: DP (two variables) — O(n) time, O(1) space
"""


def rob(nums: list[int]) -> int:
    prev1 = 0  # Max money if we skipped previous house
    prev2 = 0  # Max money if we robbed previous house

    for num in nums:
        curr = max(prev1 + num, prev2)
        prev1, prev2 = prev2, curr

    return prev2


# Tabulation approach for clarity
def rob_tabulation(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]


if __name__ == "__main__":
    print(rob([1, 2, 3, 1]))        # 4
    print(rob([2, 7, 9, 3, 1]))     # 12
    print(rob([2, 1, 1, 2]))        # 4
    print(rob_tabulation([2, 7, 9, 3, 1]))  # 12
