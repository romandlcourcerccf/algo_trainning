import sys
import os

def main():

    # rows = sys.stdin.readlines()

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '2.txt')
   
    with open(filename, 'r') as f:
        rows = f.readlines()

    n,k = tuple(map(int, rows[0].split()))
    days = list(map(int, rows[1].split()))

    print(f'n : {n} k {k}')
    days.sort()
    print(f'days : {days}')

    groups_count = 0

    while len(days) > 0 and abs(days[0] - days[-1]) > k:
        l,r = 0, len(days)-1
        group = set()
        while l<r and abs(days[l] - days[r]) > k:
            group.add(days[l])
            group.add(days[r])
            _l, _r = l,r
            while abs(days[l]-days[_l]) and _l < _r  <= k:
                _l +=1
            while abs(days[r]-days[_r])  and _l < _r <= k:
                _r +=1
            
            l,r = _l, _r

        print(group)
        

    if len(days) > 0:
        groups_count +=1

    return groups_count


if __name__ == '__main__':
    main()

