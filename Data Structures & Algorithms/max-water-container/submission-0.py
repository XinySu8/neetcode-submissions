class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxcontain = (r-l)*min(heights[l], heights[r])

        while l < r:
            if heights[l] <= heights[r]:
                l += 1
                maxcontain = max(maxcontain, (r-l)*min(heights[r],heights[l]))
            elif heights[l] > heights[r]:
                r -= 1
                maxcontain = max(maxcontain, (r-l)*min(heights[r],heights[l]))
        return maxcontain

        