def ones(N):
    if N == 0:
        return 0

    if N == 1:
        return 2

    s = set()
    s.add("0")
    s.add("1")

    for i in range(1, N):
        _s = set()
        for e in s:
            if len(e) == 1:
                _s.add(e + "0")
                _s.add(e + "1")
            else:
                _s.add(e + "0")
                e_1 = e + "1"
                if len(e_1[-3:]) != e_1[-3:].count("1"):
                    _s.add(e_1)
        s = _s

    # print(s)
    return len(s)


N = int(open("input.txt", "r").readline())

ans = ones(N)

open("output.txt", "w").write(str(ans))
