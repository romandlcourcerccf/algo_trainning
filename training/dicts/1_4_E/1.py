import os
from collections import defaultdict
def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

   
    h = defaultdict(int)

    for r in rows[1:]:
        width, height = tuple(map(int, r.split()))
        if width not in h or h[width] < height:
            h[width] = height

    # print(h)    

    keys = sorted(list(h.keys()), reverse=True)
    # print(keys)

    res = 0

    for k in keys:
        res += h[k]

    print(res)
    
        
    

if __name__ == '__main__':
    main()