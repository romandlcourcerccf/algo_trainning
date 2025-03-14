import sys
from collections import defaultdict, OrderedDict


class Heap:
    def __init__(self):
        self._heap = []

    def push(self, x):
        self._heap.append(x)
        pos = len(self._heap) - 1
        while pos > 0 and self._heap[pos] > self._heap[(pos - 1) // 2]:
            self._heap[pos], self._heap[(pos - 1) // 2] = (
                self._heap[(pos - 1) // 2],
                self._heap[pos],
            )
            pos = (pos - 1) // 2

    def pop(self):
        res = self._heap[0]
        self._heap[0] = self._heap[-1]
        pos = 0
        while pos*2+1 < len(self._heap)-1:
            min_son_index = pos * 2 + 1
            if self._heap[pos * 2 + 2] > self._heap[min_son_index]:
                min_son_index = pos * 2 + 2
            if self._heap[pos] < self._heap[min_son_index]:
                self._heap[pos], self._heap[min_son_index] = (
                    self._heap[min_son_index],
                    self._heap[pos],
                )
                pos = min_son_index
            else:
                break

        self._heap.pop()

        return res


def main():
    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '1.txt')

    with open(filename, 'r') as f:
        rows = f.readlines()

   
    heap = Heap()

    for r in rows:
        r = r.split()
        if len(r) == 1 and int(r[0]) == 1:
            print(heap.pop())
        elif len(r) == 2 and int(r[0]) == 0:
            heap.push(int(int(r[1])))


if __name__ == "__main__":
    main()
