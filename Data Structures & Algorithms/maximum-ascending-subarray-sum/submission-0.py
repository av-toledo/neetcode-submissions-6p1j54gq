class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        new = 0
        for i in range(len(nums)):
            CurSum = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] <= nums[j - 1]:
                    break
                CurSum += nums[j]
            new = max(new, CurSum) 
        return new