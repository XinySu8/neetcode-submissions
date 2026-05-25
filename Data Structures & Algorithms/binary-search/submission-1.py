class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(l: int, r: int):
            if l > r:
                return -1
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(l, mid-1)
            else:
                return binarySearch(mid+1, r)
        return binarySearch(0, len(nums)-1)


