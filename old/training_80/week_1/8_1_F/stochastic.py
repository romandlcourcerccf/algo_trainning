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
        # print(coord)
        table[coord[0]][coord[1]] = random.choice([-1, 1])

    return table


def main():
    dir_name = os.path.dirname(__file__)
    file_mame = os.path.join(dir_name, "input.txt")

    rows = open(file_mame).readlines()
    table = []
    q_coords = list()
    for row in range(1, len(rows)):
        _r = []
        for col in range(len(rows[row])):
            if rows[row][col] == "+":
                _r.append(1)
            elif rows[row][col] == "-":
                _r.append(-1)
            elif rows[row][col] == "?":
                _r.append(1)
                q_coords.append((row - 1, col))
        table.append(_r)

    # print(table)
    # print(q_coords)

    max_dist = float("-inf")

    for coord in q_coords:
        # print(coord)
        table[coord[0]][coord[1]] = 1

    for _ in range(100):
        track = []

        for i in range(len(q_coords)):
            _c = q_coords[i]
            table[_c[0]][_c[1]] = -table[_c[0]][_c[1]]
            _dist = calc_dist(table)
            track.append((_c, _dist))
            table[_c[0]][_c[1]] = -table[_c[0]][_c[1]]

        _max_dist = float("-inf")
        _max_dist_coord = None

        for t in track:
            if t[1] >= _max_dist:
                _max_dist = t[1]
                _max_dist_coord = t[0]

        table[_max_dist_coord[0]][_max_dist_coord[1]] = -table[_max_dist_coord[0]][
            _max_dist_coord[1]
        ]

        max_dist = max(max_dist, _max_dist)

    print(max_dist)


if __name__ == "__main__":
    main()
