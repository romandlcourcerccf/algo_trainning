import sys
from collections import Counter


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    with open("1.txt", "r") as reader:
        rows = reader.readlines()

    word = rows[1]

    counter = Counter(word)

    result = ""
    tail = ""

    for c in sorted(counter.keys()):
        if counter[c] == 1 and tail == "":
            tail = c
        elif counter[c] > 1:
            result += "".join([c] * (counter[c] // 2))
            if counter[c] % 2 != 0:
                tail = c

    result = result + tail + result[::-1]

    print(result)


if __name__ == "__main__":
    main()
