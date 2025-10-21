class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned_up = []

        for c in s:
            if c.isdigit() or c.isalpha():
                cleaned_up.append(c.lower())

        cleaned_up = ''.join(cleaned_up)

        return cleaned_up == cleaned_up[::-1]