class Solution:
    def reverseWords(self, s: str) -> str:
        
        res = []

        l, r = 0,0

        while r < len(s):

            while s[l] == s[r] == ' ':
                l+=1
                r+=1
                res.append(' ')

            while r < len(s) and  s[r] != ' ':
                r +=1
            
            res.append(s[l:r][::-1])
            l = r
        
        print(''.join(res))
            
        return ''.join(res)
