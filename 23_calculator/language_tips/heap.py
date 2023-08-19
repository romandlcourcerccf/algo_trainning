from heapq import (heapify,
                    heappop,
                      heappush)


arr = [3,3,4,3,4,3,5,4,5,4,3]
print(arr)
heapify(arr)
print(arr)

print(heappop(arr))