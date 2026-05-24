class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxleft = [0]*n
        maxright = [0]*n
        maxl = height[0]
        maxr = height[n-1]
        total = 0


        for i in range(1, n-1):
            maxleft[i] = maxl
            maxright[n-1-i] = maxr
            # if height[i] > maxl:
            #     maxl = height[i]
            # if height[n-1-i] > maxr:
            #     maxr = height[n-1-i]
            maxl = max(height[i], maxl)
            maxr = max(height[n-1-i], maxr)

        for i in range(1, n-1):
            total += max(0, min(maxleft[i], maxright[i]) - height[i])

        return total

            