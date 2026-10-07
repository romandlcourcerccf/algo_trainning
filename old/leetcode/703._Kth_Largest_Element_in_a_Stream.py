class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self._heap = nums
        self._k = k

        heapq.heapify(self._heap)

    def add(self, val: int) -> int:
        heapq.heappush(self._heap, val)
        while len(self._heap) > self._k:
            heapq.heappop(self._heap)

        return self._heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
