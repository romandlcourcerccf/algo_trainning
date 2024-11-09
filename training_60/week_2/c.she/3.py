import sys


def main():
   
    # rows = sys.stdin.readlines()

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '6.txt')
   
    with open(filename, 'r') as f:
        rows = f.readlines()
    
    _, dist = list(map(int, rows[0].split()))

    monuments = list(map(int, rows[1].split()))
    # print(monuments)

    l,r = 0,1
    count = 0
    intervals = []
   
    while l <= len(monuments)-1 and r <=  len(monuments)-1:
        _dist = monuments[r] - monuments[l]
        if r < len(monuments)-1:

            if _dist > dist:
                count+=1
                intervals.append((l, r))

                l+=1
                r+=1

            else:
                r+=1
        else:
            if _dist > dist:
                count+=1
                intervals.append((l, r))
            l+=1


    print(intervals)

    _intervals = set()

    for interval in intervals:
        # print('>>',interval)
        _intervals.add(interval)
        l = interval[0]
        r = interval[1]
        tmp = []
        for i in range(0, l):
            _intervals.add((i,r))
            tmp.append((i,r))
        tmp.append(interval)
        print(f'{interval} -> {tmp}')

    print(_intervals)
    print(len(_intervals))
  
    
   
if __name__ == '__main__':
    main()
