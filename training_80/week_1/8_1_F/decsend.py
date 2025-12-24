import os
import random


def calc_dist(table):
    row_maxs = []
    col_mins = []

    for r in table:
        row_maxs.append(sum(r))

    for c in range(len(table[0])):
        col = []
        for r in range(len(table)):
            col.append(table[r][c])

        col_mins.append(sum(col))

    return abs(max(row_maxs) - min(col_mins))


def fill_random(coords, table):
    for coord in coords:
        print(coord)
        table[coord[0]][coord[1]] = random.choice([-1, 1])

    return table


def main():
    dir_name = os.path.dirname(__file__)
    file_mame = os.path.join(dir_name, "2.txt")

    rows = open(file_mame).readlines()
    table = []
    q_coordis = list()
    for row in range(1, len(rows)):
        _r = []
        for col in range(len(rows[row])):
            if rows[row][col] == "+":
                _r.append(1)
            elif rows[row][col] == "-":
                _r.append(-1)
            elif rows[row][col] == "?":
                _r.append(1)
                q_coordis.append((row - 1, col))
        table.append(_r)

    print(table)
    print(q_coordis)

    max_dist = float("-inf")

    for _ in range(100):
        rnd_table = fill_random(coords=q_coordis, table=table)
        dist = calc_dist(rnd_table)
        max_dist = max(max_dist, dist)

    print(max_dist)


if __name__ == "__main__":
    main()
