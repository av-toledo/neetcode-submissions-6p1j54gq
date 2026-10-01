class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''
        
        for ch in s:
            if ch.isalnum():
                st += ch

        
        
        st = st.lower()

        rev = ''

        rev = st

        nev = rev[::-1]

        if st == nev:
            return True
        return False
        
        