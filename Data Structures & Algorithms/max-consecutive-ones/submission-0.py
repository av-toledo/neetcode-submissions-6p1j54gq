class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxCount = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                l = r + 1
            maxCount = max(maxCount, r - l + 1)
        return maxCount
            
        