import os


def main():
    dname = os.path.dirname(__file__)

    # filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")

    rows = open(filename, "r").readlines()[1:]
    rows = [r.rstrip() for r in rows]

    print(rows)

    for r in rows:
        pos = 1
        cur_val = r[pos]
        ln = 1
        print("len(r) :", len(r))
        while pos < len(r):
            print("pos :", pos)

            if r[pos] == cur_val:
                ln += 1
            else:
                print("len :", ln)
                cur_val = r[pos]
                ln = 1
            pos += 1


if __name__ == "__main__":
    main()
