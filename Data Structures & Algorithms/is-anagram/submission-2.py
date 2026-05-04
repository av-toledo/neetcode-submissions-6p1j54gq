class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        trac = {}

        for c in s:
            trac[c] = trac.get(c, 0) + 1

        for c in t:
            if c not in trac:
                return False
            trac[c] -= 1
            if trac[c] < 0:
                return False
        return True
        



        
        