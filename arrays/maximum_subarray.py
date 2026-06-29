"""
Problem: Maximum Subarray (Kadane's Algorithm)
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example:
    Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6  (subarray [4, -1, 2, 1])

Approach: Kadane's Algorithm — O(n) time, O(1) space
"""


def max_subarray(nums: list[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_subarray([1]))                                 # 1
    print(max_subarray([5, 4, -1, 7, 8]))                   # 23
