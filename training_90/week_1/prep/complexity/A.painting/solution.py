from collections import defaultdict


def main():
    p, v = tuple(map(int, input("").split()))
    q, m = tuple(map(int, input("").split()))

    if p == q:
        print(2 * max(v, m))

    elif p < q:
        if p + v <= q + m:
            print(2 * v + 2 * m + 1)
        elif q - m < p + v < q + m:
            print(abs(q + m - (p - q)))
        elif p + v > q + m:
            print(abs(p + v - (p - v)))

    elif q < p:
        if q + m < p + v:
            print(2 * v + 2 * m + 1)
        elif p - v < q + m < p + v:
            print(abs(p + v - (q - m)))
        elif q + m > p + v:
            print(abs(q + m - (q - m)))


if __name__ == "__main__":
    main()
