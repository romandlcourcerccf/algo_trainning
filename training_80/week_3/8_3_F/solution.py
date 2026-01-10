from collections import defaultdict
import sys
from memory_profiler import profile

# sys.setrecursionlimit(100000)


# @profile
def main():
    tracks = defaultdict(set)

    _ = int(input(""))
    nodes = list(map(int, input("").split()))
    pairs_number = int(input(""))

    tree = defaultdict(list)
    root = []
    for i, v in enumerate(nodes):
        if v == 0:
            root.append(i + 1)

        tree[v].append(i + 1)

    pairs = []
    for _ in range(pairs_number):
        pairs.append(tuple(map(int, input("").split())))

    # print(tree)
    # print(pairs)

    def dfs(root, track):
        # tracks[root] = tracks[root] | set(track)
        tracks[root] = set(track)

        track.append(root)

        for child in tree[root]:
            dfs(child, track.copy())

    dfs(root[0], [])

    # print(tracks)

    tree.clear()

    for pair in pairs:
        print(1 if pair[0] in tracks[pair[1]] else 0)


if __name__ == "__main__":
    main()
