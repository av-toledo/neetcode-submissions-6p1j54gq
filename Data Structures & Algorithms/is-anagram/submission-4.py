class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        compr = {}
        compr1 = {}

        for c in s:
            if c not in compr:
                compr[c] = 1
            else:
                compr[c] += 1
        for ch in t:
            if ch not in compr1:
                compr1[ch] = 1
            else:
                compr1[ch] += 1
        if compr == compr1:
            return True
        return False
        