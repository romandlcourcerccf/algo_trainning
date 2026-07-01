import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    lines = open("2.txt", "r").readlines()

    N, T = lines[0].split()[0], lines[0].split()[1]

    print(f"N {N} T {T}")

    intervals = []

    for i in range(int(T) + 1):
        intervals.append([])

    for i in range(1, len(lines)):
        r, l, a = lines[i].split()
        r, l, a = int(r), int(l), int(a)

        print(f"r {r}, l {l}, a {a}")
        intervals[r].append((("S", int(a))))
        intervals[l].append((("E", int(a))))

    print(intervals)

    max_sum = float("-inf")
    tmp_sum = 0
    for i in range(len(intervals)):
        for a in intervals[i]:
            if a[0] == "S":
                tmp_sum += a[1]
            elif a[0] == "E":
                tmp_sum -= a[1]

        max_sum = max(max_sum, tmp_sum)

    print(max_sum)


if __name__ == "__main__":
    main()
