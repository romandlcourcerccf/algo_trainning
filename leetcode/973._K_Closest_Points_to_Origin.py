from heapq import (
    heappop, 
    heappush,
    nsmallest
)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(x, y):
            return sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

        closest = []
        points = [heappush(closest, (dist([0,0], p), p))   for p in points]
 
        res = []
        for _ in range(k):
           res.append(heappop(closest)[1]) 

    
        return res
        