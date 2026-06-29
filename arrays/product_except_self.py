"""
Problem: Product of Array Except Self
Difficulty: Medium
Link: https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to
the product of all the elements of nums except nums[i].
Must run in O(n) time WITHOUT using division.

Example:
    Input: nums = [1, 2, 3, 4]
    Output: [24, 12, 8, 6]

Approach: Prefix & Suffix Products — O(n) time, O(1) extra space
"""


def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n

    # Build prefix products (left pass)
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Multiply with suffix products (right pass)
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))   # [24, 12, 8, 6]
    print(product_except_self([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
