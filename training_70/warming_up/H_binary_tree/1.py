import sys


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self._val = val
        self._left = left
        self._right = right


class Tree:
    def __init__(self):
        self._root = None

    def add(self, val: int) -> str:
        if not self._root:
            self._root = TreeNode(val)
            return "DONE"

        return self._add(self._root, val)

    def _add(self, root: TreeNode, val: int):
        if val == root._val:
            return "ALREADY"
        elif val > root._val:
            if not root._left:
                root._left = TreeNode(val)
                return "DONE"
            else:
                return self._add(root._left, val)
        else:
            if not root._right:
                root._right = TreeNode(val)
                return "DONE"
            else:
                return self._add(root._right, val)

    def search(self, val: int):
        if not self._root:
            return "NO"

        return self._search(self._root, val)

    def _search(self, root: TreeNode, val: int):
        if val == root._val:
            return "YES"
        elif val > root._val:
            if not root._left:
                return "NO"
            else:
                return self._search(root._left, val)
        else:
            if not root._right:
                return "NO"
            else:
                return self._search(root._right, val)

    def print_tree(self):
        self._print_tree(root=self._root, level=0)

    def _print_tree(self, root, level):
        if not root:
            return

        self._print_tree(root._right, level=level + 1)
        print(f"{''.join(['.']*level)}{root._val}")
        self._print_tree(root._left, level=level + 1)


def main():
    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '1.txt')

    # with open(filename, 'r') as f:
    #     rows = f.readlines()

    rows = sys.stdin.readlines()

    tree = Tree()

    for r in rows:
        r = r.split()
        command = r[0]

        match command:
            case "ADD":
                print(tree.add(val=int(r[1])))
            case "SEARCH":
                print(tree.search(val=int(r[1])))
            case "PRINTTREE":
                tree.print_tree()


if __name__ == "__main__":
    main()
