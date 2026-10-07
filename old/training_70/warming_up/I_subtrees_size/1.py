import sys
from collections import defaultdict

sys.setrecursionlimit(100000)


class Tree:
    def __init__(self, vertecis, tree):
        self._vertecis = vertecis
        self._tree = tree

    def dfs(self, root):
        self.__visited = set()
        self.__visited.add(root)
        self._dfs(root)

    def _dfs(self, root):

        nodes = 0

        for c in self._tree[root]:
            if c not in self.__visited:
                self.__visited.add(c)
                nodes += self._dfs(c)

        nodes += 1
        self._vertecis[root - 1] = nodes
        return nodes

    # def _dfs(self, root):
    #     self.__visited.add(root)

    #     if root not in self._tree:
    #         self._vertecis[root-1] = 1
    #         return 1
    #     else:
    #         nodes = 0
    #         for c in self._tree[root]:
    #             if c not in self.__visited:

    #                 nodes += self._dfs(c)

    #         self._vertecis[root-1] = nodes +1
    #         return nodes +1


def main():

    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '3.txt')

    # with open(filename, 'r') as f:
    #     rows = f.readlines()

    rows = sys.stdin.readlines()

    _vertecis = defaultdict(int)
    _vertecis = set()
    _tree = defaultdict(set)

    vert_num = int(rows[0])

    for r in rows[1:]:
        r = r.split()
        # print(r)
        r[0], r[1] = int(r[0]), int(r[1])
        # if r[1] not in _tree:
        #     _tree[r[0]].add(r[1])
        # else:
        _tree[r[1]].add(r[0])
        _tree[r[0]].add(r[1])

    # print(_tree)

    _vertecis = [0] * vert_num

    tree = Tree(vertecis=_vertecis, tree=_tree)
    tree.dfs(1)

    print(*tree._vertecis)


if __name__ == "__main__":
    main()
