import sys
import os
from collections import Counter, defaultdict

def main():
    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "5.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()

    rows = [r.rstrip() for r in rows]

    # rows = sys.stdin.readlines()
    # rows = [r.rstrip() for r in rows]

    W = rows[1]
    S = rows[2]

  
    w_map = Counter(W)
    tmp_map = defaultdict(int)
    counter = 0

    print(f'w_map : {w_map}')

    l = 0
    for r in range(len(S)):

        
    
        if S[r] not in w_map:
            l = r+1
            tmp_map.clear()

        elif S[r] in w_map:
            tmp_map[S[r]] +=1

        print('w_map.keys() :', w_map.keys(), ' tmp_map.keys() :', tmp_map.keys())

        if w_map.keys() == tmp_map.keys() and sum(w_map.values()) == sum(tmp_map.values()):

            # print('w_map.keys() :', w_map.keys(), ' tmp_map.keys() :', tmp_map.keys())
           
            counter +=1

            tmp_map[S[l]] -=1
            if tmp_map[S[l]]  <= 0:
                del tmp_map[S[l]]

    print(counter)
        
        

if __name__ == '__main__':
    main()