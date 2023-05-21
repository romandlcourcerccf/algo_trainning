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