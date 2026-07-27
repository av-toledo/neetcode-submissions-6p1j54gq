class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heightName = {}
        for h, n in zip(heights, names):
            heightName[h] = n
        

        res = []

        for h in reversed(sorted(heights)):
            res.append(heightName[h])
        
        return res
        