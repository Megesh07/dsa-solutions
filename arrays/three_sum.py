"""
Problem: 3Sum
Difficulty: Medium
Link: https://leetcode.com/problems/3sum/

Given an integer array nums, return all triplets [nums[i], nums[j], nums[k]] such that
i != j != k and nums[i] + nums[j] + nums[k] == 0. The solution set must not contain duplicates.

Example:
    Input: nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

Approach: Sort + Two Pointers — O(n^2) time, O(1) extra space
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
    print(three_sum([0, 1, 1]))               # []
    print(three_sum([0, 0, 0]))               # [[0,0,0]]
