def main():
    _, curency_rate = tuple(map(int, input("").split()))
    plates = list(map(int, input("").split()))

    plates = [(plates[i] / curency_rate, plates[i], i) for i in range(len(plates))]
    plates.sort()

    min_dist = float("inf")
    min_idxs = (0, 0)
    for i in range(len(plates)):
        for j in range(len(plates)):
            if i != j:
                if abs(plates[i][0] - plates[j][1]) <= min_dist:
                    min_dist = abs(plates[i][0] - plates[j][1])
                    min_idxs = (j, i)

    print(min_idxs[0] + 1, " ", min_idxs[1] + 1)


if __name__ == "__main__":
    main()
