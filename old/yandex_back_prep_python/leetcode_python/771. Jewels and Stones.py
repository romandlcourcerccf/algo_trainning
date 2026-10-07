class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        js = set(jewels)

        c = 0
        for s in stones:
            if s in js:
                c +=1

        return c
