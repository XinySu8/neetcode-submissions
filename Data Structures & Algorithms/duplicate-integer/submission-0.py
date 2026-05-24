class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashT = set()

        for i in nums:
            if i in hashT:
                return True
            hashT.add(i)
        return False