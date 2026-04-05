class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums3 = nums1 + nums2

        nums3.sort()

        total = len(nums3)

        if total % 2 == 0:
            return (nums3[total // 2 - 1] + nums3[total // 2]) / 2.0
        else:
            return nums3[total // 2]
        

        