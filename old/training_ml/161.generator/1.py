import sys
from random import uniform, choice
from math import cos, sin, pi
import numpy as np
import os


def generate1():
    a = uniform(0, 1)
    b = uniform(0, 1)
    return [a * cos(2 * pi * b), a * sin(2 * pi * b)]


def generate2():
    while True:
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if x**2 + y**2 > 1:
            continue
        return [x, y]


generators = {1: generate1, 2: generate2}
options = [1, 2]


def get_stats():
    arr1 = [generate1() for _ in range(1000)]
    arr2 = [generate2() for _ in range(1000)]

    arr1 = np.array(arr1).flatten()
    arr2 = np.array(arr2).flatten()

    res = [
        {"std": arr1.std(), "mean": arr1.mean(), "var": arr1.var()},
        {"std": arr2.std(), "mean": arr2.mean(), "var": arr2.var()},
    ]
    return res


def get_arr_stat(arr):
    arr = np.array(arr)
    return {"std": arr.std(), "mean": arr.mean(), "var": arr.var()}


def make_test_data():
    dname = os.path.dirname(__file__)
    filename_1 = os.path.join(dname, "1.txt")
    filename_2 = os.path.join(dname, "1_ans.txt")

    with open(filename_1, "w") as writer1:
        with open(filename_2, "w") as writer2:
            for _ in range(100):
                option = choice(options)
                arr = []
                gen = generators[option]
                for _ in range(2000):
                    arr.append(gen())

                arr = np.array(arr).flatten()
                arr = list(arr)
                arr = list(map(str, arr))
                arr = " ".join(arr)
                writer1.write(arr + "\n")
                writer2.write(str(option) + "\n")


def main():
    stats = get_stats()

    rows = sys.stdin.readlines()

    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '1.txt')

    # with open(filename, 'r') as f:
    #     rows = f.readlines()
    #     rows = [r.rstrip() for r in rows]

    res = []
    for row in rows:
        row = np.array(list(map(float, row.split())))
        arr_stat = get_arr_stat(row)

        diff_1 = abs(stats[0]["std"] - arr_stat["std"])
        diff_2 = abs(stats[1]["std"] - arr_stat["std"])

        res.append("1" if diff_1 <= diff_2 else "2")

    # print(get_stats())

    # make_test_data()

    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '1_ans.txt')

    # with open(filename, 'r') as f:
    #     answers = f.readlines()
    #     answers = [r.rstrip() for r in answers]

    # print(answers)
    # print(res)

    # cmp = []
    # for i in range(len(answers)):
    #     cmp.append(answers[i] == res[i])

    # print(all(cmp))

    for r in res:
        print(r)


if __name__ == "__main__":
    main()
