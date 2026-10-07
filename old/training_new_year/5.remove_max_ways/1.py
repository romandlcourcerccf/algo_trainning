import sys
import os
from typing import List


def delit(a):
    res = []
    i = 2
    # цикл до квадратного корня из "а"
    # больше этого без остатка не делится, если только ...
    # (об этом ниже)
    while i * i < a + 1:
        # если при делении остаток = 0, то добавляем "i" в список
        if a % i == 0:
            res.append(i)
            # теперь делим исходное число на "i", пока не появится остаток
            while a % i == 0:
                a //= i
        # берем следующее "i"
        i += 1
    # если в конце "а" не равно единице, то значит остался один(!)
    # делитель, больший кв. корня из исходного "а"
    # добавляем в список
    if a != 1:
        res.append(a)
    return res


def main():
    import os

    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, "4.txt")
    with open(filename, "r") as f:
        row = f.readline()

    # row = sys.stdin.readline()

    n = int(row)

    # print('n :',n)
    res = 0
    x = 1
    while x < n:
        # print('>>>',x + len(delit(x)))
        if x + len(delit(x)) == n:
            # print('x :', x, 'del :', len(delit(x)), 'n - x :', n-x)

            res += 1
        x += 1

    print(res)


if __name__ == "__main__":
    main()
