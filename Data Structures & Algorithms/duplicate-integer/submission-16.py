class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = set()
        for i in range(len(nums)):
            if nums[i] not in track:
                track.add(nums[i])
            elif nums[i] in track:
                return True
        return False


        