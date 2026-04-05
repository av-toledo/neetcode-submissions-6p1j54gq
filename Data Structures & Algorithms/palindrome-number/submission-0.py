class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev = str(x)[::-1]
        fa = int(rev)

        if x == fa:
            return True
        else:
            return False
        