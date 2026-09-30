class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''
        

        for ch in s:
            if ch.isalnum():
                cleaned += ch

        cleaned = cleaned.lower()
        new = cleaned

        new2 = new[::-1]

        if cleaned == new2:
            return True
        return False


        