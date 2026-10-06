class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for x in range(amount + 1):
            for coin in coins:
                if x - coin >= 0:
                    dp[x] = min(dp[x], dp[x-coin] + 1)
        return -1 if dp[amount] >= 1e9 else dp[amount]