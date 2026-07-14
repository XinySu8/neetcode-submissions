class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subs = []

        def dfs(i):
            if i >= len(nums):
                res.append(subs.copy())
                return

            # include the nums[i]
            subs.append(nums[i])
            dfs(i + 1)
            

            # do not include the nums[i]
            subs.pop()
            t = nums[i]
            while i < len(nums) and nums[i] == t:
                i += 1
            dfs(i)

        dfs(0)
        return res