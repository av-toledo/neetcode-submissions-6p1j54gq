class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        res1 = []

        for i in range(len(nums1)):
            if nums1[i] in res:
                continue
            if nums1[i] not in nums2:
                 res.append(nums1[i])
        for j in range(len(nums2)):
            if nums2[j] in res1:
                continue
            if nums2[j] not in nums1:
                res1.append(nums2[j])
        ress = [res, res1]
        return ress