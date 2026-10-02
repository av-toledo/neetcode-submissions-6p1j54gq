class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            freq = {}
            for ch in word:
                if ch not in freq:
                    freq[ch] = 1
                else:
                    freq[ch] += 1
            key = tuple(sorted(freq.items()))

            if key not in group:
                group[key] = []

            group[key].append(word)

        return list(group.values())
        

            
        
        