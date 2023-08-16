s = set([1,1,2,3])
print(s)

s1 = set([1, 2, 3, 4])
s2 = set([1, 2])

print(s2.issubset(s1))
print(s1.issubset(s2))