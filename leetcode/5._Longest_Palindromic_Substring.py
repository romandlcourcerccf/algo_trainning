class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        if len(s) == 1:
            return s

        max_l = float('-inf')
        max_s = None

        for i in range(len(s)):

            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if (r-l+1) > max_l:
                    max_l = r-l+1
                    max_s = s[l:r+1]

                l -=1
                r +=1

            l,r = i,i+1 
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if (r-l+1) > max_l:
                    max_l = r-l+1
                    max_s = s[l:r+1]

                l -=1
                r +=1
        return max_s