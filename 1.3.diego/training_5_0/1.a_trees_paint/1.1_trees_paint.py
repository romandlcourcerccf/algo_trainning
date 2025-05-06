with open("input.txt") as reader:
    rows = reader.readlines()
    rows = [r.replace("\n", "") for r in rows]

    vs = rows[0].split(" ")
    p, v = int(vs[0]), int(vs[1])

    ms = rows[1].split(" ")
    q, m = int(ms[0]), int(ms[1])

    print(f"p {p}, v {v}")
    print(f"q {q}, m {m}")
