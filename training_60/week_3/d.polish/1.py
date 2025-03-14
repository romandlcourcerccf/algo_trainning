import sys
from collections import deque


operations = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y}


def main():
    rows = sys.stdin.readlines()

    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '1.txt')

    # with open(filename, 'r') as f:
    #     rows = f.readlines()

    tokens = rows[0].split()

    s = []
    for t in tokens:
        if t not in operations.keys():
            s.append(t)
        else:
            op1 = s.pop()
            op2 = s.pop()
            s.append(operations[t](int(op2), int(op1)))

    print(s[0])


if __name__ == "__main__":
    main()
