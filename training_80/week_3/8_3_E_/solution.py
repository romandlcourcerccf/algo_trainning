from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


def main():
    ls_num = int(input(""))
    pairs = []
    while True:
        nodes_pair = ""
        try:
            nodes_pair = input("")
        except:
            pass

        if not nodes_pair:
            break

        pairs.append(tuple(map(int, nodes_pair.split())))

    tree = defaultdict(set)
    dist = defaultdict(int)

    for pair in pairs:
        tree[pair[0]].add(pair[1])
        tree[pair[1]].add(pair[0])

    # print(tree)

    class MINPathAlgo:
        def __init__(self, tree, dist):
            self.tree = tree
            self.dist = dist
            self.min_path_len = float("inf")
            self.used = set()

        def dfs(self, root):
            self.used = set()
            self._dfs(root)

        def _dfs(self, root):
            self.used.add(root)

            if not (self.tree[root] - self.used):
                return 1

            else:
                child_distanses = []
                for child in self.tree[root] - self.used:
                    child_distanses.append(self._dfs(child))

                child_distanses.sort()

                if len(child_distanses) > 1:
                    self.min_path_len = min(
                        self.min_path_len, child_distanses[0] + child_distanses[1]
                    )
                else:
                    if root == 1:
                        self.min_path_len = min(self.min_path_len, child_distanses[0])

                return 1 + child_distanses[0]

    min_path_algo = MINPathAlgo(tree=tree, dist=dist)

    min_path_algo.dfs(1)

    print(min_path_algo.min_path_len)


if __name__ == "__main__":
    main()
