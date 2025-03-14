import sys
from collections import defaultdict

import sys

sys.setrecursionlimit(100000)


def main():
    rows = sys.stdin.readlines()

    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '2.txt')

    # with open(filename, 'r') as f:
    #     rows = f.readlines()

    hierachy = defaultdict(list)
    nodes_set = set()

    for row in rows[1:]:
        row = row.split()
        nodes_set.add(row[0])
        nodes_set.add(row[1])
        hierachy[row[1]].append(row[0])

    depths = {}

    def dfs(root):
        depth = 1

        if root not in hierachy:
            return depth

        children = hierachy[root]
        for child in children:
            c_depth = dfs(child)

            if child not in depths:
                depths[child] = c_depth

            depth += c_depth
        return depth

    for node in nodes_set:
        if node in depths:
            continue

        depth = dfs(node)
        depths[node] = depth

    res = []
    for k, v in depths.items():
        res.append((k, v))

    res.sort(key=lambda x: x[0])

    for r in res:
        print(f"{r[0]} {r[1]-1}")


if __name__ == "__main__":
    main()
