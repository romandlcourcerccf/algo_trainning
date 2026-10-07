import os

from collections import Counter


def main():
    password = input()

    def nontrivial_solution(password):
        c = Counter(password)
        v = list(c.values())
        res = 0
        for i in range(len(v)):
            if i == len(v) - 1:
                _res = 1
            else:
                _res = v[i] * sum(v[i + 1 :])

            res += _res

        return res

    print(nontrivial_solution(password))


if __name__ == "__main__":
    main()
