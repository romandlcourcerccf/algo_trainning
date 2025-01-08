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

    counter = 0
    _c = 0
    while len(days) > 0: 
        print('days :', days)
        _c +=1
        if _c > 10:
             break
        l,r = 0, len(days)-1
        
        if abs(days[l]-days[r]) < k:
            counter +=1
            break
        
        jobs_done = set()
        __c = 0
        while abs(days[l]-days[r]) >= k:
           
            __c +=1
            if __c > 10:
                 break
            jobs_done.add(days[l])
            jobs_done.add(days[r])

            _l, _r = l, r

            print(f'1:  _l, _r {_l},{_r}')

            while abs(days[_l] - days[l]) < k and _l >= len(days)-1:
                   _l +=1
            
            while abs(days[_r] - days[r]) < k and _r <= 0:
                   _r -=1

            if l > r:
                 break
            
        
            print(f'2:  _l, _r {_l},{_r}')
            l, r = _l, _r 

        print('jobs_done :', jobs_done)
        if not jobs_done:
             break
        
        days  = set(days) - jobs_done
        days = list(days)
        counter +=1

    print('>>', counter)

if __name__ == '__main__':
    main()

