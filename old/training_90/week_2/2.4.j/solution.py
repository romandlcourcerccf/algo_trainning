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
        rows = [r.strip() for r in rows]

    word = rows[1]
    string = rows[2]

    # print(f"word : {word}")
    # print(f"string : {string}")

    w_counter = Counter(word)
    t_counter = None

    res_counter = 0

    for i in range(0, len(string) - len(word) + 1):
        # print(string[i : i + len(word)])

        if i == 0:
            t_counter = Counter(string[i : i + len(word)])
        else:
            t_counter[string[i - 1]] -= 1
            if t_counter[string[i - 1]] == 0:
                del t_counter[string[i - 1]]
            t_counter[string[i + len(word) - 1]] += 1

        if t_counter == w_counter:
            res_counter += 1

    print(res_counter)


if __name__ == "__main__":
    main()
