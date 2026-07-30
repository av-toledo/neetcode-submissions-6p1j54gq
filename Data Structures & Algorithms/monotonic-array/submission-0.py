class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        s = sorted(nums)
        if nums == s or nums == s[::-1]:
            return True
        return False
        