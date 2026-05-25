class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(index, height)
        maxrec = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                stacki, height = stack.pop()
                maxrec = max(maxrec, height * (i - stacki))
                start = stacki
            stack.append([start, h])
        
        for i, h in stack:
            maxrec = max(maxrec, h * (len(heights) - i))
        return maxrec
