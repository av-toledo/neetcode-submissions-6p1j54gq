class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hk = {}

        for num in nums:
            if num not in hk:
                hk[num] = 1
            elif num in hk:
                hk[num] += 1
        nums.sort(key = lambda x: (hk[x], -x))
        return nums
            
        