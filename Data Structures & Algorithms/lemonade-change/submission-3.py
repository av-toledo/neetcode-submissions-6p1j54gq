class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        freq = {5:0, 10:0}
        
        for i in range(len(bills)):
            if bills[i] == 5:
                freq[5] += 1
            elif bills[i] == 10:
                if freq[5] == 0:
                    return False
                else:
                    freq[10] += 1
                    freq[5] -= 1
            elif bills[i] == 20:
                if freq[5] > 0 and freq[10] > 0:
                    freq[10] -= 1
                    freq[5] -= 1
                elif freq[5] >= 3:
                    freq[5] -= 3
                else:
                    return False
        return True