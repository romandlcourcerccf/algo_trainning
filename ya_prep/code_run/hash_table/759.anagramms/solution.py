from collections import Counter


def load_data(path: str) -> list[str]:

    with open(path, "r") as reader:
        rows = reader.readlines()
        # res = [list(map(int, r.split())) for r in rows]
        return rows


if __name__ == "__main__":
    rows = load_data("input.txt")
    print(int(Counter(rows[0].strip()) == Counter(rows[1].strip())))
