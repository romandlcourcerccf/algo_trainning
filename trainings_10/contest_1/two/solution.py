from collections import Counter


def solution(s: str, t: str):

    print(f"s : {s}")

    cnt = 0
    for i in range(1, len(t) + 1):
        print(f"_t {t[:i]}")
        _t = set(t[:i])
        _ct = Counter(_t)
        _l = len(t[:i])

        for _i in range(len(s) - _l):
            _s = s[_i : _i + _l]
            print(f">> {_s}")

            print(":<<<<<")
            print(Counter(_s))
            print("---")
            print(_ct)
            print(":>>>>>")

            if Counter(_s) == _ct:
                cnt += 1

    print(cnt)


if __name__ == "__main__":
    lines = open("1.txt").readlines()

    solution(lines[0], lines[1])
