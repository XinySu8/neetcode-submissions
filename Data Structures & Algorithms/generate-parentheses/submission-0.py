class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subs = []

        def dfs(l, r):
            if l == n and r == n:
                res.append("".join(subs))
                return 

            elif l > r:
                subs.append("(")
                if l + 1 <= n:
                    dfs(l + 1, r)

                subs.pop()
                subs.append(")")
                if r + 1 <= n:
                    dfs(l, r + 1)
                    subs.pop()
            elif l == r and (l + 1) <= n:
                subs.append("(")
                dfs(l + 1, r)
                subs.pop()
        dfs(0, 0)
        return res