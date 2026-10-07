from typing import List


class HitCounter:
    def __init__(self):
        self.queue = []

    def hit(self, secs: int) -> None:
        print(f"hit() args: {secs}")
        while self.queue and secs - self.queue[0] >= 300:
            self.queue.pop(0)

        self.queue.append(secs)

        print("queue :", self.queue)

    def getHits(self, secs: int) -> int:
        print(f"hit() getHits: {secs}")

        print(self.queue)

        res = [s for s in self.queue if secs - s < 300]

        return len(res)
