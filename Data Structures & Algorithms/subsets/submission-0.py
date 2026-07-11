class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subs = []
        def dfs(i):
            if i >= len(nums):
                res.append(subs.copy())
                return
            
            # include the index i nums
            subs.append(nums[i])
            dfs(i + 1)

            # do not include the index i nums
            subs.pop()
            dfs(i + 1)
        dfs(0)
        return res

