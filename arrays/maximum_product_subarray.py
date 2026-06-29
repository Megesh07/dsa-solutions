"""
Problem: Maximum Product Subarray
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a subarray that has the largest product, and return the product.

Example:
    Input: nums = [2, 3, -2, 4]
    Output: 6  (subarray [2, 3])

Approach: Track both max and min products (negatives flip sign) — O(n) time, O(1) space
"""


def max_product(nums: list[int]) -> int:
    result = max(nums)
    cur_min = cur_max = 1

    for num in nums:
        if num == 0:
            cur_min = cur_max = 1
            continue
        candidates = (num, cur_max * num, cur_min * num)
        cur_max = max(candidates)
        cur_min = min(candidates)
        result = max(result, cur_max)

    return result


if __name__ == "__main__":
    print(max_product([2, 3, -2, 4]))   # 6
    print(max_product([-2, 0, -1]))     # 0
    print(max_product([-2, 3, -4]))     # 24
