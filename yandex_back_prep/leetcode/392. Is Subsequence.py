class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        p1, p2 = 0, 0

        if len(s) == 0:
            return True

        if len(t) == 0:
            return False

        if len(t) < len(s):
            return False  
        
        if len(t) == len(s) == 1:
            return t[0] == s[0]

        while p1 <= len(s)-1:
            while p2 < len(t)-1 and t[p2] != s[p1] :
                p2 +=1
           
            if p1 < len(s)-1 and t[p2] == s[p1]:
                p1 +=1

            elif p2 == len(t)-1:
                break

        return p1 == len(s)-1 
                