import sys
from collections import defaultdict

import sys

sys.setrecursionlimit(100000)


def main():
    # rows = sys.stdin.readlines()

    import os

    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, "1.txt")

    with open(filename, "r") as f:
        rows = f.readlines()

    hierachy = defaultdict(list)
    nodes_set = set()

    for row in rows[1:]:
        row = row.split()
        nodes_set.add(row[0])
        nodes_set.add(row[1])
        hierachy[row[1]].append(row[0])

    # for k,v in hierachy.items():
    #     print(f'{k}')
    #     print(f'{v}')
    res = []

    print(">>", len(nodes_set))

    def dfs(root, collected_ansestors):
        if root not in hierachy:
            return

        _ansestors = hierachy[root]

        collected_ansestors.extend(_ansestors)
        for a in _ansestors:
            dfs(a, collected_ansestors)

    for node in nodes_set:
        # print('>>',node)
        # ansestors = set()
        # cur = node
        # __ansestors = set()
        # ansestors.update(hierachy[cur])
        # __ansestors.update(ansestors)
        # while ansestors:
        #     _ansestors = set()
        #     for a in ansestors:
        #         if a in hierachy:
        #             _ansestors.update(hierachy[a])
        #     __ansestors.update(_ansestors)
        #     ansestors = _ansestors

        collected_ansestors = []
        dfs(node, collected_ansestors)

        res.append((node, len(collected_ansestors)))

    res.sort(key=lambda x: x[0])

    for r in res:
        print(f"{r[0]} {r[1]}")


if __name__ == "__main__":
    main()
