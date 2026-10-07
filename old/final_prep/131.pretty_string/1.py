import sys
import os
from collections import defaultdict, Counter

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "3.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()


    # rows = sys.stdin.readlines()
    # rows = [r.rstrip() for r in rows]

    max_pstr_len = float('-inf')

    max_change = int(rows[0])
    string = rows[1]

    l,r = 0,0
    hash =  defaultdict(int)

    max_letter = None
    max_count = None

    for r in range(len(string)):

        hash[string[r]] += 1
        if not max_letter:
            max_letter = string[r]
            max_count = 1
        elif hash[string[r]] > max_count:
            max_letter = string[r]
            max_count = hash[string[r]] 

        if r-l+1 - max_count <= max_change:
            max_pstr_len = max(r-l+1, max_pstr_len)
        
        else:
            l+=1
            hash[string[l]] -= 1
            if string[l] == max_letter:
                max_count -=1 
    
    print(max_pstr_len)

if __name__ == '__main__':
    main()