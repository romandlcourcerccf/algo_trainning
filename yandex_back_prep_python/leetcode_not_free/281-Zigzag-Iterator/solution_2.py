from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = []

        if v1:
            self.queue.append(v1)

        if v2:
            self.queue.append(v2)

    def next(self) -> int:
        print("len(self.queue) : ", len(self.queue))

        v = self.queue.pop(0)

        r = v.pop(0)

        if len(v) > 0:
            self.queue.append(v)

        return r

    def hasNext(self) -> bool:
        return len(self.queue) > 0


v1 = [1, 2, 3]
v2 = [4, 5, 6]

i, v = ZigzagIterator(v1, v2), []
while i.hasNext():
    v.append(i.next())

print(v)
