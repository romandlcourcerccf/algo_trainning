import os
from collections import defaultdict


def main():
    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    # filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")
    # filename = os.path.join(dname, "7.txt")
    filename = os.path.join(dname, "8.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    nums = list(map(int, rows[1].split()))

    

  

if __name__ == "__main__":
    main()
