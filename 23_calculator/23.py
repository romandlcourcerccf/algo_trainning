def calc(N):
    ops = 0

    track = []
    track.append(str(1))
    
    if N == 1:
        return ops, track

    _N = 1
    while _N <= N:

        mult_3 = _N * 3
        mult_2 = _N * 2
        plus_1 = _N+1

        res = [mult_3, mult_2, plus_1]
        res = [r for r in res if r <= N]
        res = max(res)
    
        ops += 1
        track.append(str(res))

        if res == N:
            return ops, track
        
        _N = res


N = int(open('input.txt', 'r').readline())

ops, track  = calc(N)


with open('output.txt', 'w') as w:
    w.write(str(ops))
    w.write('\n')
    w.write(' '.join(track))