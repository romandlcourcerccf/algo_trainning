from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        c = Counter(words)
       
        h = []
        for v, _k, in c.items():
            heapq.heappush(h, (-_k,v))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(h)[1])

        return res