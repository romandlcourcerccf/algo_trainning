#slow solution
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        s1c = Counter(s1)
        s2c = Counter(s2[0:len(s1)])

        for i in range(0, len(s2)-len(s1)+1):
            if s1c == Counter(s2[i:i+len(s1)]):
                return True

        return False
    


    class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        h_s1 = Counter(s1)

        for r in range(0, len(s2)-len(s1)+1):
            if r == 0:
                h_s2 = Counter(s2[0:len(s1)])
            
            else:
                h_s2[s2[r-1]] -=1
                if h_s2[s2[r-1]] == 0:
                    h_s2.pop(s2[r-1])
                
                h_s2[s2[r + len(s1)-1]] +=1
            
            if h_s1 == h_s2:
                return True

        return False