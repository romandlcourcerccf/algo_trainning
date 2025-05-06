with open("input.txt") as reader:
    rows = reader.readlines()
    rows = [r.replace("\n", "") for r in rows]

    board = []

    figures = []

    for r in range(len(rows)):
        cols = rows[r].split(" ")
        for c in range(len(cols)):
            if cols[c] == "B":
                figures.append(["B", (r, c)])
            elif cols[c] == "R":
                figures.append(["R", (r, c)])

    print(figures)
