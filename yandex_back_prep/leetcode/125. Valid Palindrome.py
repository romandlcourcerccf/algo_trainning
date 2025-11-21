class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned_up = []

        for c in s:
            if c.isdigit() or c.isalpha():
                cleaned_up.append(c.lower())

        cleaned_up = ''.join(cleaned_up)

        return cleaned_up == cleaned_up[::-1]
    

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = list(s)
        _s = []
        
        for c in s:
            if c.lower() != ' ' and  c.isalnum():
                _s.append(c.lower())

        return _s == _s[::-1]
    
    class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join([c.lower() for c in s if c.isalnum() ])
        return s == s[::-1]