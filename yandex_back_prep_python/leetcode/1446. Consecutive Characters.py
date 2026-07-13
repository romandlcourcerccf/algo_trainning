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
    

    class Solution:
    def maxPower(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
            
        max_len = float('-inf')

        i = 0
        while i < len(s)-1:
            _max_len = 1
            while i < len(s)-1 and  s[i] == s[i+1]:
                i +=1
                _max_len +=1
            
            max_len = max(max_len, _max_len)
            i +=1

        return max_len
            
