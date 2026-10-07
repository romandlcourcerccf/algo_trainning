from collections import defaultdict

orders = defaultdict(defaultdict(int))

orders["ff"] = "ssa"
orders["ff"] = "ssb"

print(orders["ff"])
