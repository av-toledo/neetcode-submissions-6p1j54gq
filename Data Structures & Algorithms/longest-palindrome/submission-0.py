class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        coun = 0

        for c in s:
            if c not in seen:
                seen.add(c)
            elif c in seen:
                seen.remove(c)
                coun += 2
        if seen:
            return coun + 1
        else:
            return coun
        