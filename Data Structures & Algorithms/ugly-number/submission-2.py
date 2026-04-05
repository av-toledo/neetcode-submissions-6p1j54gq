class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for d in [2, 3, 5]:
            while n % d == 0:
                n //= d
        if n == 1:
            return True
        else:
            return False