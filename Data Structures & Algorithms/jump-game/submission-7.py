class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        def dfs(i):
            for j in range(1, nums[i]+1):
                if i + j >= n:
                    break

                if dp[i+j] == True:
                    continue
                dp[i+j] = True
                dfs(i+j)

        dfs(0)
        return dp[n-1]       