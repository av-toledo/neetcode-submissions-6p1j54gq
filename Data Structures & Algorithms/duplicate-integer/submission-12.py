class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = {}

        for i in range(len(nums)):
            if nums[i] not in track:
                track[nums[i]] = 1
            elif nums[i] in track:
                return True
        return False

