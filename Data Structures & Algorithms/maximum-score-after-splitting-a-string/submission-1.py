class Solution:
    def maxScore(self, s: str) -> int:
        r = s.count('1')
        l = 0
        max_sc = 0

        for i in range(len(s) -1):
            if s[i] == '0':
                l += 1
            elif s[i] == '1':
                r -= 1
            max_sc = max(max_sc, l + r)
        return max_sc