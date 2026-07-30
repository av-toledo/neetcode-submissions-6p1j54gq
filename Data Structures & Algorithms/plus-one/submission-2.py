class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numberstr = ""
        

        for i in range(len(digits)):
            numberstr += str(digits[i])
        number = int(numberstr)
        number += 1
        return list(map(int, str(number)))