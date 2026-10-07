def _split(T):
    T = T.split(":")
    T = [int(t) for t in T]
    return T


def ops():
    lines = open("input.txt", "r").readlines()
    A, B, C = lines[0], lines[1], lines[2]

    A = _split(A)
    B = _split(B)
    C = _split(C)

    print(A)
    print(B)
    print(C)

    D = C[0] - A[0], C[1] - A[1], C[2] - A[2]

    print(D)

    real_time = B[0] - D[0], B[1] - D[1], B[2] - D[2]

    print(real_time)

    # open('output.txt', 'w').write(str(len(alive_sectors)))


ops()
