import sys
from collections import defaultdict

import sys

sys.setrecursionlimit(100000)


def main():
    # rows = sys.stdin.readlines()

    import os

    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, "35.txt")

    with open(filename, "r") as f:
        rows = f.readlines()

    hierachy = defaultdict(set)

    emp_num = int(rows[0])

    bosses = list(map(int, rows[1].split()))
    bonuses = [0] * (emp_num)

    for i in range(2, emp_num + 1):
        hierachy[int(bosses[i - 2])].add(i)

    def dfs(root):
        price = 1

        if root not in hierachy or len(hierachy[root]) == 0:
            for k in hierachy:
                if root in hierachy[k]:
                    hierachy[k].remove(root)

        else:
            price = 1 + dfs(min(hierachy[root]))

        bonuses[root - 1] += price

        return price

    while hierachy[1]:
        bonuses[0] += dfs(1)

    bonuses[0] += 1

    print(" ".join(list(map(str, bonuses))))


if __name__ == "__main__":
    main()
