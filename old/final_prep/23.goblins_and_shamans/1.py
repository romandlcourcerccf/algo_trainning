import sys
import os
from collections import defaultdict, Counter


def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "2.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    # rows = sys.stdin.readlines()
    # rows = [r.rstrip() for r in rows]

    queue = []

    for r in rows[1:]:
        r = r.split()
        if r[0] == '+':
            queue.append(int(r[1]))
        elif r[0] == '-':
            print(queue.pop(0))
        elif r[0] == '*':

            if len(queue) % 2 == 0:
                queue.insert(len(queue)//2, int(r[1]))
            else:
                queue.insert((len(queue)+1)//2-1, int(r[1]))



if __name__ == '__main__':
    main()