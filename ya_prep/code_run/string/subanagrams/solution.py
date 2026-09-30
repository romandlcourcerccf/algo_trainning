from collections import Counter


def solution():
    rows = open("1.txt", "r").readlines()

    string = rows[0]
    pattern = Counter(rows[1])

    counter = 0

    for i in range(len(string)):
        k = i
        while i + k < len(string) and k < len(rows[1]):
            if string[i + k] in pattern:
                counter += 1
            else:
                break
            k += 1

    print(counter)


if __name__ == "__main__":
    solution()
