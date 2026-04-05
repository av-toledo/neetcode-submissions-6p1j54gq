class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}

        for m in magazine:
            if m not in freq:
                freq[m] = 1
            else:
                freq[m] += 1

        for r in ransomNote:
            if r not in freq or freq[r] == 0:
                return False
            freq[r] -=1
        return True
            



        


                


        
        