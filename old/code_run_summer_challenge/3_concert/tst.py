import heapq

l = [1, 2, 3, 4, 5]
heapq.heapify(l)

print(heapq.nsmallest(1, l))
heapq.heappop(l)
print(heapq.nsmallest(1, l))
