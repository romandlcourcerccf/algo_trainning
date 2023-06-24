from collections import defaultdict
from heapq import (heappush,
                     heappop,
                     nlargest)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        h = []
        for _k,_v in d.items():
            heappush(h, (-_v,_k))
        
        r = []
        for i in range(k):
            r.append(heappop(h))

        r = [i[1] for i in r]
        return r
