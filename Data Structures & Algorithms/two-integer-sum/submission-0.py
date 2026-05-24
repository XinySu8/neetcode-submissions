class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasht = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in hasht:
                return [hasht[need], i]
            hasht[nums[i]] = i
        return
