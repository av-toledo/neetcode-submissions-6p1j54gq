class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new = []
        for i in range(len(heights)):
            new.append(heights[i])
        new.sort()
        count = 0

        for i in range(len(heights)):
            if heights[i] != new[i]:
                count += 1
        return count