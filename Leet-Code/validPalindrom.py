import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = s.lower()
        word = re.sub(r'[\W_]', '', word)
        def palindrom(s):
            n = len(s)
            if n == 0 or n == 1:
                return True
            else:
                if s[0] == s[n-1]:
                    return palindrom(s[1:n-1])
                else:
                    return False 
        return palindrom(word)