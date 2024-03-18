
from heapq import(heappop, heappush)

class Node():
    def __init__(self, val: int = 0):
        self.val = val


h = []
# heappush(h, (5, Node(5)))
# heappush(h, (7, Node(7)))
heappush(h, (1, 'write spec'))
heappush(h, (3, 'create tests'))
heappop(h)