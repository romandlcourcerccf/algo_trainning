from bisect import bisect_left

l = [1, 50, 100]
x = 1000


pos = bisect_left(l, x)
print("pos :", pos)
