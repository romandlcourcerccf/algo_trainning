import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
<<<<<<< HEAD
    tort_num = int(input(""))

    fair_torts_counter = 0

    for t in range(tort_num):
        t_sp = list(map(int, input("").split()))
        if sum(t_sp) <= tort_num - 1:
            fair_torts_counter += 1

    print(fair_torts_counter)


if __name__ == "__main__":
    main()
=======

    _ = int(input(""))
    vagons = list(map(int, input("").split()))

    end = []
    res = []

    for idx, val in enumerate(vagons):
        if idx < len(vagons) - 1:
            if val <= min(vagons[idx + 1 :]):
                res.append(val)
            elif not end or val <= end[-1]:
                end.append(val)
            else:
                print("NO")
                return
        else:
            res.append(val)

    res += end[::-1]
    print("YES")
>>>>>>> 9c6a377a9cb9661be124a2a1b9c7eaaeeccd1f98
