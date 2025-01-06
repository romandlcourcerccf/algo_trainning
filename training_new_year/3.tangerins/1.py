import sys
import os
from typing import List


def main():

    rows = sys.stdin.readlines()

    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '3.txt')
    # with open(filename, 'r') as f:
    #     rows =  f.readlines()

    n = int(rows[0])

    oranges = []
    tangerins = []

    sum_oranges = 0
    sum_tangerins = 0
    sums = []

    for r in rows[1:]:
        r = list(map(int,r.split()))
        # print(r)
        sum_oranges += r[0]
        sum_tangerins += r[1]

        oranges.append(r[0])
        tangerins.append(r[1])

        sums.append([[r[0],r[1]], r[0]+r[1]])

       
    # print('n : ',n)
    # print('oranges   : ',oranges)
    # print('tangerins : ',tangerins)

    # print('sum_oranges   :', sum_oranges)
    # print('sum_tangerins :', sum_tangerins)
    
    sums.sort(key= lambda x: x[1], reverse=True)

    sums = sums[:n]

    _o_sum = sum(s[0][0] for s in sums)
    _t_sum = sum(s[0][1] for s in sums)


    res = _o_sum > sum_oranges/2 and _t_sum > sum_tangerins/2

    print('Yes' if res else 'No')

    
if __name__ == '__main__':
    main()

