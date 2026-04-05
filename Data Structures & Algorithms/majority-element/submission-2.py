class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tracker = {}
        for num in nums:
            if num not in tracker:
                tracker[num] = 1
            else:
                tracker[num] += 1

        return max(tracker,key = tracker.get)
            



        