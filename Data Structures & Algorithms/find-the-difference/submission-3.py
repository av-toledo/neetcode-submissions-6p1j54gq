class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        track_s = {}
        track_t = {}

        for c in s:
            if c not in track_s:
                track_s[c] = 1
            else:
                track_s[c] += 1
        for c in t:
            if c not in track_t:
                track_t[c] = 1
            else:
                track_t[c] += 1
        for c in track_t:
            if c not in track_s or track_t[c] > track_s[c]:
                return c