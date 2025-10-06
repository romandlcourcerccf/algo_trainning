import os

from collections import Counter
from math import factorial


def main():
    dname = os.path.dirname(__file__)

    # filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    filename = os.path.join(dname, "3.txt")
    # filename = os.path.join(dname, "4.txt")
    # filename = os.path.join(dname, "5.txt")
    # filename = os.path.join(dname, "6.txt")
    filename = os.path.join(dname, "7.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    password = rows[0]

    def trivial_solution(password):
        s = set()
        list_of_passwords = list(password)
        print(sorted(password))
        s.add(password)
        used = set()

        for i in range(len(list_of_passwords)):
            for j in range(len(list_of_passwords)):
                # print(i,' ', j)
                if (
                    i != j
                    and (i, j) not in used
                    and list_of_passwords[i] != list_of_passwords[j]
                ):
                    list_of_passwords[i], list_of_passwords[j] = (
                        list_of_passwords[j],
                        list_of_passwords[i],
                    )
                    # print(''.join(list_of_passwords))
                    s.add("".join(list_of_passwords))
                    list_of_passwords[j], list_of_passwords[i] = (
                        list_of_passwords[i],
                        list_of_passwords[j],
                    )
                    used.add((i, j))

        print(s)
        print(len(s))

    trivial_solution(password)


if __name__ == "__main__":
    main()
