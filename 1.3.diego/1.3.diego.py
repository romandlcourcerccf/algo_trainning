from bisect import bisect_left


def diego():
    with open("input.txt") as reader:
        rows = reader.readlines()
        rows = [r.replace("\n", "") for r in rows]

        collection_size = int(rows[0][0])

        collection = sorted(list(set([int(i) for i in rows[1].split(" ")])))

        collectors_num = rows[2][0]
        collectors_sizes = [int(cs) for cs in rows[3].split(" ")]

        res = []
        for cs in collectors_sizes:
            pos = bisect_left(collection, cs)
            res.append(pos)

        with open("output.txt", "w") as w:
            for r in res:
                w.write(str(r) + "\n")


if __name__ == "__main__":
    diego()
