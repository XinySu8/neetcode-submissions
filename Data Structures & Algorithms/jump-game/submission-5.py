class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [None] *n

        def dfs(i):
            if i >= n - 1:
                return True
            
            if dp[i] is not None:
                return dp[i]

            for j in range(1, nums[i] + 1):
                if dfs(i + j):
                    dp[i] = True
                    return True
            dp[i] = False
            return False

        return dfs(0)       