class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countr = {}

        for i in range(len(nums)):
            if nums[i] not in countr:
                countr[nums[i]] = 1
            else:
                return True
        return False
            



