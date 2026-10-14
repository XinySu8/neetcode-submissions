class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n)]
        dp[0] = True

        def dfs(i):
            for j in range(1, nums[i] + 1):
                next_i = i + j

                if next_i >= n:
                    break

                if dp[next_i] == True:
                    continue
                
                dp[next_i] = True
                dfs(next_i)
                
            
        dfs(0)
        return dp[n-1]
            