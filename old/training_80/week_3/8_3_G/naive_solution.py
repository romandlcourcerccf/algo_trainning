def main():
    rows = []

    for _ in range(4):
        rows.append(list(map(int, input("").split())))

    A = list(map(int, rows[1]))
    B = list(map(int, rows[3]))

    res = 0
    for idx_a, a in enumerate(A):
        for idx_b, b in enumerate(B):
            # print((idx_a - idx_b) * abs(a - b))
            res += (idx_a - idx_b) * abs(a - b)

    print(res)


if __name__ == "__main__":
    main()
