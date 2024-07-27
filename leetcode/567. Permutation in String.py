# My solution O(26N)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_h = defaultdict(int)
        s2_h = defaultdict(int)

        for c in s1:
            s1_h[c]+=1
        
        for r in range(0, len(s1)):
            s2_h[s2[r]]+=1

       
        if s1_h == s2_h:
            return True
        
        if len(s1) == len(s2) and s1_h != s2_h:
            return False

        
        for r in range(1,  len(s2)-len(s1)+1):
            s2_h[s2[r-1]]-=1
            if s2_h[s2[r-1]] == 0:
                del s2_h[s2[r-1]]

            s2_h[s2[r+len(s1)-1]]+=1

            if s1_h == s2_h:
                return True
        
        return False
    

    