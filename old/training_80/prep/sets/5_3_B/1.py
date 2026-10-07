import os
from collections import Counter


def main():
    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "2.txt")

    with open(filename, "r") as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    row1 = rows[0]
    row2 = rows[1]

    counter1 = Counter(row1)
    counter2 = Counter(row2)

    for k in counter1:
        if k not in counter2 or counter1[k] != counter2[k]:
            print("NO")
            return

    for k in counter2:
        if k not in counter1 or counter1[k] != counter2[k]:
            print("NO")
            return

    print("YES")


if __name__ == "__main__":
    main()
