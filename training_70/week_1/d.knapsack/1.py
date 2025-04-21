import sys


def main():
    # rows = sys.stdin.readlines()

    import os

    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, "0.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip().split() for r in rows]

        _rows = []
        for r in rows:
            _rows.append(list(map(int, r)))

    print(_rows)
    
# В первой строке вводится натуральное число N, не превышающее 100, и натуральное число M, не превышающее 10000.

# Во второй строке вводятся N натуральных чисел 

#   , не превышающих 100.


# 4 9
# 2 3 5 2

    N, M = _rows[0]
    items = _rows[1]

    print(f'N: {N} M: {M}')
    print(f'mi: {_rows[1]}')

    dp = [-1] * (M+1)
    dp[0] = 0
    print(dp)

    # for item in items:
    #     for i in range(len(dp)-1 - item, -1, -1):
    #         if dp[i] != -1:
    #              dp[i+item] = 1

    
    # for item in items:
    #     for i in range(len(dp)-1 - item, -1, -1):
    #         if dp[i] != -1:
    #              dp[i+item] = dp[i] + item

    for i_index in range(len(items)):
        print(f'i_index : {i_index} items[i_index]: {items[i_index]}')
        for i in range(len(dp)-1 - items[i_index], -1, -1):
            if dp[i] != -1:
                 if  dp[i+items[i_index]] == -1: 
                    dp[i+items[i_index]] =  i_index+1
                 
        
        print(dp)
    

    track = []
    pos = len(dp)-1
    while pos >= 0:
        track.append(dp[pos]-1)
        pos -= items[dp[pos]-1]
    
    print(track)

   







if __name__ == "__main__":
    main()
