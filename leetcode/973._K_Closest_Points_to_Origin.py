class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        h = []

        def distanse(p1, p2):
            return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        

        for p in points:
            heapq.heappush(h, (distanse((0,0), (p[0],p[1])), p))

        res = []

        for _ in range(k):
            res.append(heapq.heappop(h)[1])

        return res
