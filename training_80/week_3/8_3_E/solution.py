def main():
    _, p = tuple(map(int, input("").split()))
    plates = list(map(int, input("").split()))

    plates = [(plates[i], i) for i in range(len(plates))]

    plates.sort()

    min_val = float("inf")
    min_pos = None

    for i in range(len(plates)):
        l, r = 0, len(plates) - 1

        while l <= r:
            m = (l + r) // 2
            if abs(plates[i][0] / plates[l][0] - p) <= abs(
                plates[i][0] / plates[m][0] - p
            ):
                r = m - 1
            else:
                l = m

        if min(min_val, abs(plates[i][0] / plates[m][0] - p)) <= min_val:
            min_val = abs(plates[i][0] / plates[m][0] - p)
            min_pos = (i, m)

    print(min_pos[1] + 1, "", min_pos[0] + 1)


if __name__ == "__main__":
    main()
