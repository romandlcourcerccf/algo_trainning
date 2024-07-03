class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0:
            return True

        k = 0
        for i in range(len(t)):
            if t[i] == s[k]:
                k+=1
                
            if k > len(s)-1:
                break

        return k == len(s)