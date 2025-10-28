import os
from collections import defaultdict


def main():
    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    # filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")
    # filename = os.path.join(dname, "7.txt")
    # filename = os.path.join(dname, "8.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    n = int(rows[0])
    results = list(map(int, rows[1].split()))

    max_idx = results.index(max(results))

    best_res = 0

    for i in range(max_idx + 1, n): 
        if results[i] % 10 == 5 and i + 1 < n and results[i] > results[i + 1]:
            best_res = max(best_res, results[i])

    if best_res == 0:
        print(best_res)

    else:
        print(sum([1 for r in results if r > best_res]) + 1)


if __name__ == "__main__":
    main()
