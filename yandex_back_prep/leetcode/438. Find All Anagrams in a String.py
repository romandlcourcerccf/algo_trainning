class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        pc = Counter(p)
        ps = None
        res = []

        print(f's : {s}')
        print(f'p : {p}')

    
        for i in range(0, len(s)-len(p)+1):
            print(f'i {i} s[{i}] {s[i]}')
            if i == 0:
                ps = Counter(s[i:len(p)])
                
            else:
                ps[s[i-1]]-=1
                if ps[s[i-1]] == 0:
                    ps.pop(s[i-1])
                ps[s[i+len(p)-1]]+=1

            if ps == pc:
                    res.append(i)
        
        return res






        