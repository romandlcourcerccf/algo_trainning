class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0]*26, [0]*26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')]+=1
            s2Count[ord(s2[i]) - ord('a')]+=1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l=0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r])-ord('a')
            s2Count[index] +=1
            if s1Count[index]  == s2Count[index]:
                matches +=1
            elif s1Count[index]+1  == s2Count[index]:
                matches -=1
             
            index = ord(s2[l])-ord('a')
            s2Count[index] -=1
            if s1Count[index]  == s2Count[index]:
                matches +=1
            elif s1Count[index]-1  == s2Count[index]:
                matches -=1
            
            l += 1

        return matches == 26
    


    from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        h1 = defaultdict(int)
        h2 = defaultdict(int)

        for i in range(len(s1)):
            h1[s1[i]]+=1
            h2[s2[i]]+=1
        
        if h1 == h2:
            return True
        
        for i in range(0, len(s2)-len(s1)+1):
            h2 = defaultdict(int)
            for _i in range(len(s1)):
                h2[s2[i+_i]] += 1
            
            if h1 == h2:
                return True

        return False
    
    