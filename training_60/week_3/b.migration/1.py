import sys


def main():
    rows = sys.stdin.readlines()

    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '1.txt')

    # with open(filename, 'r') as f:
    #     rows = f.readlines()

    populations = list(map(int, rows[1].split()))

    res = [-1] * len(populations)

    stack = []

    for i, p in enumerate(populations):
        while stack and p < stack[-1][1]:
            _i, _p = stack.pop()
            res[_i] = i

        stack.append((i, p))

    res = list(map(str, res))

    print(" ".join(res))


if __name__ == "__main__":
    main()
