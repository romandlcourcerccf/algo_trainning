import os
from collections import defaultdict


def main():
    # n = int(input())

    # rows = []
    # for _ in range(n - 1):
    #     rows.append(input())

    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")
    filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")
    # filename = os.path.join(dname, "4.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    tree = defaultdict(set)

    used = set()
    orphans = defaultdict(set)

    for r in rows[1:]:
        r = tuple(map(int, r.split()))
        if len(r) < 2:
            continue

        if r[0] == 1:
            tree[r[0]].add(r[1])
            used.add(r[0])
            used.add(r[1])
        elif r[0] in used or r[1] in used:
            if r[0] in used:
                tree[r[0]].add(r[1])
                # search for the orphan
                if r[1] in orphans:
                    tree[r[1]] = orphans[r[1]]
            elif r[1] in used:
                tree[r[1]].add(r[0])

                tree[r[1]].add(r[0])
                # search for the orphan
                if r[0] in orphans:
                    tree[r[0]] = orphans[r[0]]

            used.add(r[0])
            used.add(r[1])

        elif r[0] not in used and r[1] not in used:
            orphans[r[0]].add(r[1])
            orphans[r[1]].add(r[0])

    print(tree)

    class PathFinder:
        def __init__(self, tree):
            self.min_path = float("inf")
            self.tree = tree

        def dfs(self, root):
            if root not in tree:
                return 1

            print(">>", root)

            p_lens = []
            for c in tree[root]:
                p_lens.append(self.dfs(c))

            if len(p_lens) > 1:
                self.min_path = min(self.min_path, sum(p_lens))

            return min(p_lens) + 1
            # elif len(p_lens) == 1:
            #     # self.min_path = p_lens[0]
            #     return p_lens[0] + 1

    pf = PathFinder(tree)
    pf.dfs(1)

    print(pf.min_path)


if __name__ == "__main__":
    main()
