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


def main():
    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")
    # filename = os.path.join(dname, "4.txt")
    # filename = os.path.join(dname, "8.txt")
    filename = os.path.join(dname, "11.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    class ParentChecker:
        def __init__(self, rows):
            self.rows = rows
            self.tree = self._init_tree()
            self._paths = defaultdict(set)
            self._make_paths()

        def _init_tree(self):
            tree = defaultdict(set)

            nodes = map(int, rows[1].split())
            for i, v in enumerate(nodes):
                tree[v].add(i + 1)
            return tree

        @timer()
        def _make_paths(self):
            nodes = map(int, rows[1].split())
            for i, _ in enumerate(nodes):
                self.track = set()
                self.dfs(0, set(), i + 1)
                self._paths[i + 1] = self.track

        def dfs(self, root, track, target):
            track.add(root)

            if root == target:
                self.track = track
                return

            for child in self.tree[root]:
                self.dfs(child, track, target)

        def is_parent(self, a, b):
            return a in self._paths[b]

        @timer()
        def print_parents(self):
            for row in rows[3:]:
                a, b = tuple(map(int, row.split()))
                print(int(self.is_parent(a, b)))

    pc = ParentChecker(rows=rows)

    pc.print_parents()


if __name__ == "__main__":
    main()
