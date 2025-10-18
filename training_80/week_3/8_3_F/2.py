import os
from collections import defaultdict


import functools
import time
from typing import Callable, Any


def timer():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Any:
            print(f"Start func {func} ")
            start = time.time()
            try:
                return func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"Finish func {func} {total} ")

        return wrapped

    return wrapper


@timer()
def main():
    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")
    filename = os.path.join(dname, "4.txt")
    # filename = os.path.join(dname, "8.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    class ParentChecker:
        def __init__(self, rows):
            self.rows = rows
            self.tree = self._init_tree()
            # print(self.tree)
            self.is_parent

        def _init_tree(self):
            tree = defaultdict(set)

            nodes = map(int, rows[1].split())
            for i, v in enumerate(nodes):
                tree[v].add(i + 1)
            return tree

        def dfs(self, root, track, parent, target):
            track.append(root)

            if root == target and parent in track:
                # print(f"parent {parent}, target {target} track {track}")
                self._is_parent = True
                return

            for child in self.tree[root]:
                _track = track.copy()
                self.dfs(child, _track, parent, target)

        def is_parent(self, a, b):
            self._is_parent = False
            self.dfs(0, list(), a, b)
            return self._is_parent

    pc = ParentChecker(rows=rows)

    hash = defaultdict(int)

    for row in rows[3:]:
        a, b = tuple(map(int, row.split()))
        if (a, b) in hash:
            print(hash[(a, b)])
        elif (b, a) in hash and hash[(b, a)] == 1:
            print(0)
        else:
            is_parent = int(pc.is_parent(a, b))
            hash[(a, b)] = is_parent
            print(is_parent)

    # rows = ["4 2"]
    # for row in rows:
    #     a, b = tuple(map(int, row.split()))
    #     print(f"a {a}, b {b}, -> {int(pc.is_parent(a, b))}")


if __name__ == "__main__":
    main()
