import sys
import os
from collections import Counter, defaultdict

def main():
    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "2.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()

    rows = [r.rstrip() for r in rows]

    # rows = sys.stdin.readlines()
    # rows = [r.rstrip() for r in rows]

    W = rows[1]
    S = rows[2]

  
    w_map = Counter(W)
    t_map = defaultdict(int)
    counter = 0

    # print(f'w_map : {w_map}')

    l = 0
    for r in range(len(S)):

    
        if S[r] not in w_map:
            l = r+1
            t_map.clear()

        elif S[r] in w_map and S[r] not in t_map or  t_map[S[r]] < w_map[S[r]]:
            t_map[S[r]] +=1

        # print('w_map.keys() :', w_map.keys(), ' tmp_map.keys() :', t_map.keys())

        if w_map.keys() == t_map.keys() and sum(w_map.values()) == sum(t_map.values()):

            counter +=1

            t_map[S[l]] -=1
            if t_map[S[l]]  <= 0:
                del t_map[S[l]]
            
            l +=1

    print(counter)
        
        

if __name__ == '__main__':
    main()