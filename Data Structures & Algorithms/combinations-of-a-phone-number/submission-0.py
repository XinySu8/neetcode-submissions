class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        subs = ""
        res = []

        def dfs(i, subs):
            if len(subs) == len(digits):
                res.append(subs)
                return
            for c in dic[digits[i]]:
                dfs(i + 1, subs+c)
            
        if digits:
            dfs(0, "")
            
        return res
            

            