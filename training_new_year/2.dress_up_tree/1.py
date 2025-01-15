import sys
import os
from typing import List



def main():

    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '2.txt')
    # with open(filename, 'r') as f:
    #     layers = int(f.readline())

    layers = int(sys.stdin.readline())


    print(int((1.0 - 2.0**layers) / (1.0 - 2.0)))

    
if __name__ == '__main__':
    main()

