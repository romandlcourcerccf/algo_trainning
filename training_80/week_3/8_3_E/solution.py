from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


def main():
    vert_count = int(input(""))

    vert_parents = []
    for _ in range(vert_count - 1):
        vert_parents.append(int(input("")))

    verts_values = list(map(int, input("").split()))

    print("vert_count :", vert_count)
    print("vert_parents :", vert_parents)
    print("verts_values :", verts_values)

    tree = defaultdict(set)

    for idx, vpr in enumerate(vert_parents):
        tree[vpr].add(idx + 1)

    print(tree)

    paths = defaultdict(list)

    def dfs(root, path):
        print("root :", verts_values[root])

        path.append(root)

        if root not in tree:
            paths[root] = path

        for child in tree[root]:
            print("child :", child)
            dfs(child, path.copy())

    dfs(0, [])

    print(paths)


if __name__ == "__main__":
    main()
