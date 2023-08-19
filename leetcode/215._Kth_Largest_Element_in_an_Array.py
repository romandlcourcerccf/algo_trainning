from heapq import(
            heappush, 
            heappop)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        h = []
        for n in nums:
            heappush(h, -n)
        
        for i in range(k):
            e = heappop(h)

        return -e
    

    from heapq import (
    heappush,
    heappop
)
