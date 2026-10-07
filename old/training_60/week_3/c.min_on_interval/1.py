import sys
from collections import deque


def main():
    rows = sys.stdin.readlines()

    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '1.txt')

    # with open(filename, 'r') as f:
    #     rows = f.readlines()

    _, k = list(map(int, rows[0].split()))
    munbers = list(map(int, rows[1].split()))

    window = deque()
    for i, v in enumerate(munbers):
        while window and window[-1][0] >= munbers[i]:
            window.pop()

        window.append((v, i))

        while window[0][1] <= i - k:
            window.popleft()

        if i > k - 2:
            print(window[0][0])


if __name__ == "__main__":
    main()
