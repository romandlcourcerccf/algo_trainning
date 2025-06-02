from heapq import heappop, heappush, nsmallest


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

        closest = []
        points = [heappush(closest, (dist([0, 0], p), p)) for p in points]

        res = []
        for _ in range(k):
            res.append(heappop(closest)[1])

        return res

import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        l = []
        for point in points:
            l.append((sqrt((point[0])**2 + (point[1])**2), point))
        
        heapq.heapify(l)

        res = []
        while k > 0:
            k-=1
            res.append(heapq.heappop(l))

        res = [p[1] for p in res]

        return res