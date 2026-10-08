class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}

        def dfs(i, flag):
            if i == n - 1:
                dp[(i, flag)] = max(0, nums[i]) if flag else nums[i]

            if (i, flag) in dp:
                return dp[(i, flag)]   
            
            if flag:
                dp[(i, flag)] = max(0, nums[i] + dfs(i + 1, True))
                return dp[(i, flag)]
            
            dp[(i, flag)] = max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))
            return dp[(i, flag)]
        
        return dfs(0, False)
