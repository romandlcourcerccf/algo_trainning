import os
from collections import defaultdict
def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]


    h = defaultdict(int)
    
    pains_num = int(rows[0])
    for i in range(1, pains_num+1):
        p = rows[i].split()
        h[p[0]] = p[1]
        h[p[1]] = p[0]

    word = rows[pains_num + 1]

    print(h[word])

if __name__ == '__main__':
    main()