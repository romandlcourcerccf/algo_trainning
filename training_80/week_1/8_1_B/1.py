import os


def main():
    # dname = os.path.dirname(__file__)

    # filename = os.path.join(dname, "input.txt")
    # filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")
    # filename = os.path.join(dname, "4.txt")
    # filename = os.path.join(dname, "5.txt")
    # filename = os.path.join(dname, "65.txt")  # 1.717948717948718

    # with open(filename, "r") as f:
    #     rows = f.readlines()
    #     rows = [r.rstrip() for r in rows]

    # a, b, c, v0, v1, v2 = tuple(map(float, rows[0].split()))
    a, b, c, v0, v1, v2 = tuple(map(float, input().split()))

    min_time = min(
        (a / v0) + (a / v1) + (b / v0) + (b / v1),
        (b / v0) + (b / v1) + (a / v0) + (a / v1),
        (a / v0) + (a / v1) + (b / v1) + (b / v2),
        (b / v0) + (b / v1) + (a / v1) + (a / v2),
        (a / v0) + (c / v1) + (b / v2),
        (b / v0) + (c / v1) + (a / v2),
        (b / v0) + (c / v1) + (c / v2) + (b / v2),
        (b / v0) + (c / v0) + (c / v1) + (b / v2),
        (a / v0) + (c / v1) + (c / v2) + (a / v2),
        (a / v0) + (c / v0) + (c / v1) + (a / v2),
        (a / v0) + (c / v0) + (c / v1) + (a / v2),
        (b / v0) + (c / v0) + (c / v1) + (b / v1) + (b / v0) + (b / v1),
        (a / v0) + (c / v0) + (c / v1) + (a / v1) + (a / v0) + (a / v1),
    )

    print(min_time)


if __name__ == "__main__":
    main()
