class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentMatch = {"]":"[", "}": "{", ")": "("}

        for c in s:
            if c in parentMatch:
                if stack and stack[-1] == parentMatch[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
