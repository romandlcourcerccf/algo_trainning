class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        h = []

        for s in stones:
            heapq.heappush(h, -s)
        
        print(h)

        while len(h) > 0:
            if len(h) == 1:
                return -heapq.heappop(h)
            else:
                s1 = -heapq.heappop(h)
                s2 = -heapq.heappop(h)
                if s1 !=s2:
                    heapq.heappush(h, -abs(s1-s2))
        
        return 0
    

from heapq import (
    heappush,
    heappop
)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        _stones = []
        for s in stones:
            heappush(_stones, -s)

        while len(_stones) > 1:
            s1 = - heappop(_stones)
            s2 = - heappop(_stones)
            if s1 != s2:
                heappush(_stones, s2 - s1)


        return -_stones[0] if len(_stones) > 0 else 0