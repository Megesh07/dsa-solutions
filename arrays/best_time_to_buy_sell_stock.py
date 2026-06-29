"""
Problem: Best Time to Buy and Sell Stock
Difficulty: Easy
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.
Return the maximum profit you can achieve. If you cannot achieve any profit, return 0.

Example:
    Input: prices = [7, 1, 5, 3, 6, 4]
    Output: 5  (buy at 1, sell at 6)

Approach: Sliding Window / One Pass — O(n) time, O(1) space
"""


def max_profit(prices: list[int]) -> int:
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(max_profit([7, 6, 4, 3, 1]))      # 0
    print(max_profit([1, 2]))               # 1
