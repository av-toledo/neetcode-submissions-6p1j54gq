class Solution:
    def firstUniqChar(self, s: str) -> int:
        tra = {}
        count = s[0]

        for i in range(len(s)):
            if s[i] not in tra:
                tra[s[i]] = 1
            elif s[i] in tra:
                tra[s[i]] += 1
        for i in range(len(s)):
            if tra[s[i]] == 1:
                return i
        return -1

            