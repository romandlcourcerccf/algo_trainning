class Solution:
    def maxPower(self, s: str) -> int:
        
        res = ''
        le = -1

        if len(s) == 1:
            return 1

        pos = 0
        while pos < len(s)-1:
            res += s[pos]
            while  pos < len(s)-1 and s[pos] == s[pos+1]:
                pos +=1
                res += s[pos]
        
            le = max(le, len(res))
            res = ''
            pos +=1

        return le