class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        anw = []
        ane = []
        ans =[]

        for i in range(len(nums)):
            anw.append(nums[i])
            ane.append(nums[i])
        for i in range (len(anw)):
            ans.append(anw[i])
        for i in range(len(ane)):
            ans.append(ane[i])
        return ans
            
        
            
        
                