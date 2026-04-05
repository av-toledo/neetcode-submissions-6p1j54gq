class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        new = []

        neww = {}
        
        for word in strs:
            key = ''.join(sorted(word))

            if key not in neww:
                neww[key] = []

            neww[key].append(word)
            
        return list (neww.values())