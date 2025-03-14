from heapq import heappop, heappush


h = []


class Node:
    def __init__(self, val: int = 0):
        self.val = val


node1 = Node(0)
node2 = Node(1)

print(node1.val)
print(node2.val)

heappush(h, (node1.val, node1))
heappush(h, (node2.val, node2))

print(heappop(h)[0])
