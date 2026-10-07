import os


def main():
    rows = []

    # for _ in range(4):
    #     rows.append(list(map(int, input("").split())))

    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, "1.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    A = list(map(int, rows[1].split()))
    B = list(map(int, rows[3].split()))

    res = 0
    for idx_a, a in enumerate(A):
        for idx_b, b in enumerate(B):
            print(
                f"i A : {A[idx_a]}, B : {B[idx_b]} ({idx_a},{idx_b}) : {(idx_a - idx_b) * abs(a - b)}"
            )
            res += (idx_a - idx_b) * abs(a - b)

    print(res)


if __name__ == "__main__":
    main()
