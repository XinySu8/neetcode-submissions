class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqS = {}
        freqT = {}

        for c in s:
            freqS[c] = freqS.get(c, 0) + 1
        
        for c in t:
            freqT[c] = freqT.get(c, 0) + 1

        for c in freqS:
            if freqS[c] != freqT.get(c, 0):
                return False
        return True