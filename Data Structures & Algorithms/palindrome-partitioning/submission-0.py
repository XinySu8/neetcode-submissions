class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        path = []

        def dfs(c):
            if c == n:
                res.append(path.copy())
                return

            # subs 只是用来构造当前 substring
            subs = []

            for i in range(c, n):
                subs.append(s[i])

                # 检查当前 subs 是否是 palindrome
                m = len(subs)
                left, right = 0, m - 1
                is_palindrome = True

                while left < right:
                    if subs[left] != subs[right]:
                        is_palindrome = False
                        break

                    left += 1
                    right -= 1

                # 如果当前 substring 是 palindrome
                if is_palindrome:
                    path.append("".join(subs))

                    # 从下一个位置继续切
                    dfs(i + 1)

                    # backtracking
                    path.pop()

        dfs(0)
        return res