class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}

        for m in magazine:
            if m not in freq:
                freq[m] = 1
            else:
                freq[m] += 1

        for ch in ransomNote:
            if ch not in freq or freq[ch] == 0:
                return False
            freq[ch] -= 1
        return True


        


                


        
        