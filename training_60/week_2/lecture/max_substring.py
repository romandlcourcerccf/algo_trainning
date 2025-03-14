from collections import defaultdict

# n, k = map(int, input().split())
# s = input()

n, k = 10, 3
s = "ababababcc"

d = defaultdict(int)

l = r = bestl = bestr = 0

while r < n:
    if d[s[r]] < k:
        if r - l >= bestr - bestl:
            bestr, bestl = r, l
        d[s[r]] += 1
        r += 1
    else:
        while l < n and d[s[r]] >= k:
            d[s[l]] -= 1
            l += 1

print(bestr - bestl + 1, bestl + 1)
