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

    pairs_ansestors = defaultdict(list)
    pairs_sign_list = [0] * pairs_number
    for pair_number in range(pairs_number):
        pair = tuple(map(int, input("").split()))
        pairs_ansestors[pair[1]].append((pair[0], pair_number))

    def dfs(root, track):
        for pair in pairs_ansestors[root]:
            if pair[0] in track:
                pairs_sign_list[pair[1]] = 1

        track.append(root)

        for child in tree[root]:
            dfs(child, track)

    dfs(root[0], [])

    for sign in pairs_sign_list:
        print(sign)


if __name__ == "__main__":
    main()
