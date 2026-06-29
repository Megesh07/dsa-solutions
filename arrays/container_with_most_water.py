"""
Problem: Container With Most Water
Difficulty: Medium
Link: https://leetcode.com/problems/container-with-most-water/

Given n vertical lines at positions i with height[i], find two lines that together
with the x-axis form a container that holds the most water.

Example:
    Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49

Approach: Two Pointers — O(n) time, O(1) space
"""


def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        water = min(height[left], height[right]) * width
        max_water = max(max_water, water)

        # Move the pointer with the shorter height inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(max_area([1, 1]))                          # 1
