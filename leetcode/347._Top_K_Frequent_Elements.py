from heapq import ( heappop,
                    heappush
                    )
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        fr = defaultdict(int)

        for e in nums:
            fr[e]+=1
           
        
        h = []
        for _k,_v in fr.items():
            heappush(h, (-_v,_k))
        

        res = [heappop(h)[1] for i in range(k)]
        return res