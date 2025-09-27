import os

from collections import Counter

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "2.txt")
    # filename = os.path.join(dir_name, "7.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    nums = list(map(int, rows[1].split()))

    c = Counter(nums)

    res = 0

    for k in c.keys():
        _res = c[k] + max( c.get(k-1, 0), c.get(k+1, 0))
        res = max(_res, res)

    print(len(nums) - res)
     



    
        
    

if __name__ == '__main__':
    main()