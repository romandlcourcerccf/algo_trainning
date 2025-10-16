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

    print(f"n {n}, p {p}")

    cs = list(map(int, rows[1].split()))

    min_dist = float("inf")
    p1 = -1
    p2 = -1

    enriched = []
    for idx, val in enumerate(cs):
        enriched.append((idx, val))

    enriched.sort(key=lambda x: x[1])

    print(enriched)

    enriched = [(e[0], e[1] / p) for e in enriched]

    print(enriched)

    for ci, c in enumerate(cs):
        dist, idx = float("inf"), -1
        left, right = 0, len(enriched) - 1

        count = 0
        while left < right:
            print(f"left {left} right {right}")
            if count > 10:
                print("count : ", count)
                break
            count += 1

            m = (left + right) // 2

            if abs(enriched[m][1] - c) <= dist and enriched[m][0] != ci:
                dist = enriched[m][1]
                idx = enriched[m][0]

            if enriched[m][1] <= c:
                left = m + 1
            else:
                right = m

        if dist < min_dist:
            p1 = ci
            p2 = idx

        print(f"c {c}, ci {ci}, dist {dist}, idx {idx}")

    print(p1, " ", p2)


if __name__ == "__main__":
    main()
