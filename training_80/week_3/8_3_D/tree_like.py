import os
from typing import Tuple


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, data: Tuple[int, int] = None):
        self.root = None

        for i in range(len(data)):
            if i == 0:
                self.root = TreeNode(val=data[i])
            else:
                self.fill_up(root=self.root, val=data[i])

    def fill_up(self, root, val: int):
        if val[1] < root.val[1]:
            if root.left:
                self.fill_up(root.left, val)
            else:
                root.left = TreeNode(val)
                return
        elif val[1] > root.val[1]:
            if root.right:
                self.fill_up(root.right, val)
            else:
                root.right = TreeNode(val)
                return

    def get_closest(self, data: Tuple[int, int]) -> Tuple[int, int]:
        self.min_dist = float("inf")
        self.closest = None

        def _get_closest(root, val):
            if not root:
                return

            _dist = val[1] - root.val[1]
            if abs(_dist) <= self.min_dist:
                self.min_dist = _dist
                self.closest = root

            if val[1] < root.val[1]:
                _get_closest(root.left, val)
            elif val[1] > root.val[1]:
                _get_closest(root.right, val)
            elif val[1] == root.val[1]:
                return

        _get_closest(self.root, data)

        return self.closest.val


def main():
    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")
    filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    n, p = tuple(map(int, rows[0].split()))

    print(f"n {n}, p {p}")

    cs = list(map(int, rows[1].split()))

    enriched = []
    for idx, val in enumerate(cs):
        enriched.append((idx, val))

    enriched = [(e[0], e[1] / p) for e in enriched]

    print(enriched)

    tree = Tree(enriched)
    print(tree)

    for idx, val in enumerate(cs):
        print(val, " ", tree.get_closest((idx, val)))


if __name__ == "__main__":
    main()
