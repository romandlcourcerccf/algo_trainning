import os

def is_reachable(r, c, rows):
    return r >=0 and r <= len(rows)-1 and c >=0 and c < 3 and rows[r][c] != 'W' and rows[r][c] != 'U'

def get_if_valid(r, c, rows):
    if r >=0 and r <= len(rows)-1 and  c >=0 and c < 3 and rows[r][c] != 'W' and rows[r][c] != 'U':
        return rows[r][c] 
    return 0

def process(rows, r, c, dp):

    if rows[r][c] != 'W':
        max_val = max([get_if_valid(r-1, c+1, dp),
                            get_if_valid(r-1, c, dp),
                                get_if_valid(r-1, c-1, dp) ])


        max_val = max_val+1 if rows[r][c] == 'C' else max_val
        is_reach = is_reachable(r-1, c+1, rows) | is_reachable(r-1, c, rows) | is_reachable(r-1, c-1, rows)

        # print(f'r {r}, {c} is_reach : {is_reach}')
        # print(f'r: {r-1} c: {c+1}  {is_reachable(r-1, c+1, rows)}')
        # print(f'r: {r-1} c: {c}  {is_reachable(r-1, c, rows)}')
        # print(f'r: {r-1} c: {c-1}  {is_reachable(r-1, c-1, rows)}')
        if not is_reach and r != 0:
            rows[r][c] = 'U'

        if not is_reach:
            max_val = 0

        dp[r][c] = max_val

def main():

    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    # filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")
    # filename = os.path.join(dname, "6.txt")
    filename = os.path.join(dname, "7.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    r_num = int(rows[0])
    rows = [list(r) for r in rows[1:]]

    # for r in rows:
    #     print(r)

    dp = [[0 for _ in range(3)] for r in range(r_num)]
   
    max_coins = float('-inf')

    for i in range(3):
        _max_coins_for_i = float('-inf')

        if rows[0][i] == 'W':
            _max_coins_for_i = 0
            continue

        for r in range(r_num):
            if r == 0:
                for c in range(i,3):
                    process(rows, r, c, dp)
                    
            else:
                for c in range(3):
                    if rows[r][c] != 'W':
                        process(rows, r, c, dp)
                        _max_coins_for_i = max(_max_coins_for_i, dp[r][c])
                    
        
        max_coins = max(_max_coins_for_i, max_coins)
        # for r in dp:
        #     print(r)

    max_coins = 0 if max_coins == float('-inf') else max_coins
    
    print(max_coins)

    for r in rows:
        print(r)
        

if __name__ == "__main__":
    main()

   


