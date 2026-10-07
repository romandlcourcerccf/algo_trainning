from collections import Counter, defaultdict


def solution():
    rows = open("1.txt", "r").readlines()

    string = rows[0]
    pattern = Counter(rows[1])

    counter = 0
    pos = 0

    while pos < len(string):
        c = pos
        local_counter = defaultdict(int)
        while c + pos < len(string):
            if string[c + pos] in pattern and (
                string[c + pos] not in local_counter
                or local_counter[string[c + pos]] < pattern[string[c + pos]]
            ):
                counter += 1
                local_counter[string[c + pos]] += 1
            else:
                break
            c += 1
        pos += c

    print(counter)


if __name__ == "__main__":
    solution()
