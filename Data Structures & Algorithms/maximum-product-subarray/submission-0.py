class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]

        n = len(nums)
        for i in range(1, n):
            num = nums[i]
            candidate = [
                num,
                curMax * num,
                curMin * num
            ]

            curMax = max(candidate)
            curMin = min(candidate)

            res = max(res, curMax)
            

        return res

