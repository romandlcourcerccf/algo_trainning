import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)
        print(c)

        h = []

        for _k, _v in c.items():
            heapq.heappush(h, (-_v, _k))

        res = [heapq.heappop(h)[1] for e in range(k)]

        return res