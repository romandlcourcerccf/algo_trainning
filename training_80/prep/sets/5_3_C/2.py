import os

from collections import defaultdict

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "7.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    nums = list(map(int, rows[1].split()))

    h = defaultdict(set)

    for n1 in nums:
        for n2 in nums:
            print('n1 :', n1, 'n2 :', n2)
            h[abs(n1-n2)].add(n1)
            h[abs(n1-n2)].add(n2)

    print(h)
    

if __name__ == '__main__':
    main()