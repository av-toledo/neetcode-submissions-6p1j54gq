class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        mine = (nums[0] * nums[1])

        maxe = (nums[-1] * nums[-2])

        res = maxe - mine

        return res
        