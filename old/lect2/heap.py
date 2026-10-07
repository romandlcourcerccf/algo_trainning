class Heap:
    def __init__(self) -> None:
        self._heap = []

    def push_heap(self, x):
        self._heap.append(x)
        pos = len(self._heap) - 1
        while pos > 0 and self._heap[pos] < self._heap[(pos - 1) // 2]:
            self._heap[pos], self._heap[(pos - 1) // 2] = (
                self._heap[(pos - 1) // 2],
                self._heap[pos],
            )
            pos = (pos - 1) // 2

    def pop_heap(self):
        ans = self._heap[0]
        self._heap[0] = self._heap[-1]
        pos = 0
        while pos * 2 + 1 < len(self._heap) - 1:
            min_son_index = pos * 2 + 1
            if self._heap[pos * 2 + 2] < self._heap[min_son_index]:
                min_son_index = pos * 2 + 2
            if self._heap[pos] > self._heap[min_son_index]:
                self._heap[pos], self._heap[min_son_index] = (
                    self._heap[pos],
                    self._heap[min_son_index],
                )
                pos = min_son_index
            else:
                break
        self._heap.pop()
        return ans


if __name__ == "__main__":
    h = Heap()

    h.push_heap(4)
    h.push_heap(3)
    h.push_heap(2)
    h.push_heap(1)

    print(h._heap)

    print(h.pop_heap())
    print(h.pop_heap())

    print(h._heap)
