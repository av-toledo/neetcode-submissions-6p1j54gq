class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        tra = {}

        for i in range(len(nums)):
            if nums[i] not in tra:
                tra[nums[i]] = 1
            elif nums[i] in tra:
                tra[nums[i]] += 1

        filtr = []

        for key in tra:
            if tra[key] == 1:
                filtr.append(key)
        if len(filtr) == 0:
            return -1
        return max(filtr)


        
        
        
        