import os
from collections import defaultdict


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    salers = defaultdict(set)
    sales = defaultdict(int)

    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, "2.txt")

    with open(filename, "r") as reader:
        lines = reader.readlines()

    for line in lines:
        line = line.split()
        salers[line[0]].add(line[1])
        sales[line[0] + "_" + line[1]] += int(line[2])

    salers_lex = sorted(list(salers.keys()))

    for saler in salers_lex:
        print(f"{saler}:")
        for product in sorted(list(salers[saler])):
            print(f"{product} {sales[saler + '_' + product]}")


if __name__ == "__main__":
    main()
