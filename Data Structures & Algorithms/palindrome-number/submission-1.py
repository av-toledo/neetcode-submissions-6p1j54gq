class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = str(x)[::-1]
        r = int(rev)

        if x == r:
            return True
        else:
            return False
        