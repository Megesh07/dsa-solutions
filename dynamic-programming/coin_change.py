"""
Problem: Coin Change
Difficulty: Medium
Link: https://leetcode.com/problems/coin-change/

Given an array of coin denominations and a total amount,
return the fewest number of coins needed to make up that amount.
Return -1 if no combination is possible.

Example:
    Input: coins = [1, 5, 6, 9], amount = 11
    Output: 2  (5 + 6)

Approach: Bottom-up DP — O(amount * n) time, O(amount) space
"""


def coin_change(coins: list[int], amount: int) -> int:
    # dp[i] = min coins needed to make amount i
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins to make amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    print(coin_change([1, 5, 6, 9], 11))   # 2
    print(coin_change([1, 2, 5], 11))       # 3 (5+5+1)
    print(coin_change([2], 3))              # -1
    print(coin_change([1], 0))              # 0
