import sys
from collections import defaultdict, OrderedDict


def main():
    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '1.txt')

    # with open(filename, 'r') as f:
    #     rows = f.readlines()

    rows = sys.stdin.readlines()

    tree_map = defaultdict(str)

    for r in rows:
        r = r.split()
        if len(r) == 2:
            tree_map[r[0]] = r[1]

    res = defaultdict(str)

    names = set(tree_map.keys()) | set(tree_map.values())

    for name in names:
        level = 0
        cur = name
        while cur in tree_map:
            level += 1
            cur = tree_map[cur]
        res[name] = level

    res = OrderedDict(sorted(res.items()))

    for r in res.items():
        print(f"{r[0]} {r[1]}")


if __name__ == "__main__":
    main()
