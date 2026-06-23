class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, num)
            elif num > maxHeap[0]:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, num)
            
        return maxHeap[0]
            
