class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}

        def dfs(i, Has):
            if i >= n:
                return 0
            
            if (i, Has) in dp:
                return dp[(i, Has)]

            hold = dfs(i + 1, Has)

            if Has:
                buy = dfs(i + 2, not Has) + prices[i]
                dp[(i, Has)] = max(buy, hold)
            else:
                sell = dfs(i + 1, not Has) - prices[i]
                dp[(i, Has)] = max(sell, hold)
            return dp[(i, Has)]
            
        return dfs(0, False)