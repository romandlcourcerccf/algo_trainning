import sys


def compress(rows):
    ans = [rows[0]]
    for n in rows[1:]:
        if n != ans[-1]:
            ans.append(n)
    if len(ans) > 1 and set(ans[0]) == {"."}:
        ans.pop(0)
    if len(ans) > 1 and set(ans[-1]) == {"."}:
        ans.pop()

    return ans


def invert(rows):
    ans = []
    for i in range(len(rows[0])):
        ans.append([])

    for row in rows:
        for i in range(len(row)):
            ans[i].append(row[i])

    for i in range(len(ans)):
        ans[i] = "".join(ans[i])

    return ans


# n  = int(input())
# a = []
# for i in range(n):
#     a.append(input())

import os

dname = os.path.dirname(__file__)
filename = os.path.join(dname, "2.txt")

with open(filename, "r") as f:
    a = f.readlines()
    a = [r.rstrip() for r in a]

a.pop(0)
a = compress(a)
a = invert(a)
a = compress(a)
a = invert(a)

if a == ["#"]:
    print("I")
elif a == ["###", "#.#", "###"]:
    print("O")
elif a == ["##", "#.", "##"]:
    print("C")
elif a == ["#.", "##"]:
    print("L")
elif a == ["#.#", "###", "#.#"]:
    print("H")
elif a == ["###", "#.#", "###", "#.."]:
    print("P")
else:
    print("X")
