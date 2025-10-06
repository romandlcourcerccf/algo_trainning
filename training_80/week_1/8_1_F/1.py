import os
import itertools
import numpy as np


def main():
    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")
    # filename = os.path.join(dname, "4.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    q_smb_count = 0
    for r in rows[1:]:
        q_smb_count += r.count("?")
        print(list(r))

    print(f"q_smb_count : {q_smb_count}")

    lst = list(itertools.product([-1, 1], repeat=q_smb_count))

    max_diff = float("-inf")
    max_diff_arr = None

    for l in lst:
        # print(l)

        arr = []
        pos = 0
        for r in rows[1:]:
            r = list(r)
            _r = []
            for c in r:
                if c == "+":
                    _r.append(1)
                elif c == "-":
                    _r.append(-1)
                else:
                    _r.append(l[pos])
                    pos += 1

            arr.append(_r)

        arr = np.array(arr)

        # print(arr)
        # print(np.sum(arr, axis=0))

        diff = abs(np.max(np.sum(arr, axis=1)) - np.min(np.sum(arr, axis=0)))
        print(diff)

        if diff > max_diff:
            max_diff = diff
            max_diff_arr = arr

        if diff == 0:
            print(arr)

        # print('\n')

    print(f"max_diff {max_diff}")

    print("max_diff")
    print(max_diff_arr)

    # for r in rows[1:]:
    #     arr.append(list(r))

    # for r in arr:
    #     print(r)


if __name__ == "__main__":
    main()
