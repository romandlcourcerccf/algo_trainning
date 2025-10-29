#slow solution
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        s1c = Counter(s1)
        s2c = Counter(s2[0:len(s1)])

        for i in range(0, len(s2)-len(s1)+1):
            if s1c == Counter(s2[i:i+len(s1)]):
                return True

        return False