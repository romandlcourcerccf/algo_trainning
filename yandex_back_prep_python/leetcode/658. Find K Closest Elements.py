class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        heap = []

        for e in arr:
            heappush(heap, (abs(e - x), e))

        res = []

        while k > 0:
            res.append(heappop(heap)[1])
            k -= 1

        return sorted(res)
