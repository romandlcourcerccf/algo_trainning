import sys
from collections import defaultdict

import sys

sys.setrecursionlimit(100000)


def main():
    # rows = sys.stdin.readlines()

    import os

    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, "3.txt")

    with open(filename, "r") as f:
        rows = f.readlines()

    hierachy = defaultdict(list)

    for row in rows[1:]:
        row = row.split()
        print("row :", row)

        if int(row[1]) in hierachy:
            hierachy[int(row[1])].append(int(row[0]))
        else:
            hierachy[int(row[0])].append(int(row[1]))

    # print(hierachy)

    res = {}

    def dfs(root):
        print(f"-->{root}")

        if root not in hierachy:
            res[root] = 1
            return 1

        # print(f'-->{root}')

        _vert_sum = sum([dfs(c) for c in hierachy[root]]) + 1

        res[root] = _vert_sum

        return _vert_sum

    dfs(1)

    vertices = sorted(list(res.keys()))
    depth = [str(res[v]) for v in vertices]

    print(" ".join(depth))


if __name__ == "__main__":
    main()
