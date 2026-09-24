class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        la = {}
        for i in range (len(nums)):
            if nums[i] not in la:
                la[nums[i]] = 1
            else:
                return True
        return False
            
        