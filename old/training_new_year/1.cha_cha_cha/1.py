import sys
import os
import math


def get_letters():
    letters = list(map(chr, range(ord("A"), ord("Z") + 1)))
    scores = {letters[i]: len(letters) - i for i in range(len(letters))}
    reversed_scores = {i[1]: i[0] for i in scores.items()}

    return scores, reversed_scores


def main():
    import os

    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, "8.txt")
    with open(filename, "r") as f:
        scores = f.readline()

    # scores = sys.stdin.readline()
    scores = scores.replace("\n", "")

    letters, reversed_letters = get_letters()

    # print(letters)

    scores = [letters[s] for s in scores]
    # print(scores)

    _min = min(scores)
    print("_min :", reversed_letters[_min])

    av = math.ceil(sum(scores) / len(scores))

    print("av  :", reversed_letters[av])

    if _min == int(av):
        print(reversed_letters[av])

    else:
        av = _min + 1
        print(reversed_letters[av])


if __name__ == "__main__":
    main()
