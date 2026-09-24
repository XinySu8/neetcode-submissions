class Solution:
    def climbStairs(self, n: int) -> int:
        dfs = [0] * n
        if n <= 1:
            dfs[0] = 1
        elif n <= 2:
            dfs[0] = 1
            dfs[1] = 2
        else:
            dfs[0] = 1
            dfs[1] = 2
            for i in range(2, n):
                dfs[i] = dfs[i - 1] + dfs[i - 2]
        return dfs[n-1]