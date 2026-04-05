class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        herq = []
        for i in range(len(nums)):
            herq.append(nums[i] ** 2)
        herq.sort()
        return herq
        