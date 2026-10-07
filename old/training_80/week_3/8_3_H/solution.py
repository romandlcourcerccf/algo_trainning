from collections import defaultdict
import sys

# sys.setrecursionlimit(100000)

edicts_count = 0


def main():
    vert_count = int(input(""))

    vert_parents = []
    for _ in range(vert_count - 1):
        vert_parents.append(int(input("")))

    verts_values = list(map(int, input("").split()))

    # print("vert_count :", vert_count)
    # print("vert_parents :", vert_parents)
    # print("verts_values :", verts_values)

    tree = defaultdict(set)

    for idx, vpr in enumerate(vert_parents):
        tree[vpr].add(idx + 1)

    # print(tree)

    def dfs(root, path):
        path.append(root)

        for child in tree[root]:
            # print("child :", child)
            dfs(child, path.copy())

        if verts_values[root] != 0:
            # print(f"before :root {root} verts_values: {verts_values} ")
            global edicts_count
            edicts_count += abs(verts_values[root])
            if verts_values[root] > 0:
                for p in path:
                    verts_values[p] -= abs(verts_values[root])
            else:
                for p in path:
                    verts_values[p] += abs(verts_values[root])

            # print(f"after :root {root} verts_values: {verts_values} ")

    dfs(0, [])

    # print(verts_values)
    print(edicts_count)


if __name__ == "__main__":
    main()
