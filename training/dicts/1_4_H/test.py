from collections import defaultdict

a = defaultdict(int)
b = defaultdict(int)

a['a'] +=1
a['b'] +=1

b['a'] +=1
# b['b'] +=1


print(a == b)


