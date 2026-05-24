class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k = len(s1)
        l, r = 0, k-1
        substr1 = {}
        substr2 = {}

        for i in range(k):
            substr1[s1[i]] = substr1.get(s1[i], 0) + 1
            substr2[s2[i]] = substr2.get(s2[i], 0) + 1

        
        while r < len(s2)-1:
            if substr1 == substr2:
                return True
            substr2[s2[l]] = substr2.get(s2[l], 0) - 1
            if substr2[s2[l]] == 0:
                del substr2[s2[l]]
            l += 1
            r += 1
            substr2[s2[r]] = substr2.get(s2[r], 0) + 1
        return substr1 == substr2

