class Solution:
    def canJump(self, nums: List[int]) -> bool:

        indexJump = len(nums) - 1


        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= indexJump:
                indexJump = i
        if indexJump == 0:
            return True
        else:
            return False

                
                
            


        