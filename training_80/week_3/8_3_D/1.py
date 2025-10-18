import os


def main():
    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")
    filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    n, p = tuple(map(int, rows[0].split()))

    cs = list(map(int, rows[1].split()))


if __name__ == "__main__":
    main()
