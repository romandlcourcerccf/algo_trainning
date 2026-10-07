from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


def main():
    _ = int(input(""))
    nodes = list(map(int, input("").split()))
    pairs_number = int(input(""))

    tree = defaultdict(list)
    root = []
    for i, v in enumerate(nodes):
        if v == 0:
            root.append(i + 1)

        tree[v].append(i + 1)

    stack = []
    stack.append(root[0])

    parent = {}

    while stack:
        s = stack.pop()

        if s not in tree:
            continue

        for child in tree[s]:
            stack.append(child)
            parent[child] = s

    for _ in range(pairs_number):
        pair = tuple(map(int, input("").split()))

        p = pair[1]
        g = pair[0]

        is_ansestor = False
        while p in parent.keys():
            if p == g:
                is_ansestor = True
                break
            p = parent[p]

        print(1 if is_ansestor else 0)


if __name__ == "__main__":
    main()
