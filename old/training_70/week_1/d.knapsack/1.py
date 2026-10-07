


def main():

    # import sys
    # rows = sys.stdin.readlines()

    import os

    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, "input.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip().split() for r in rows]


    rows = [list(map(int, r)) for r in rows]

    N, M = rows[0]
    items = rows[1]


    dp = [-1] * (M+1)
    dp[0] = 0
    
    items.sort(reverse=True)
    
    for item in items:
        for i in range(len(dp)-1 - item, -1, -1):
            if dp[i] != -1:
                 dp[i+item] = dp[i] + item


    print(max(dp))
    

if __name__ == "__main__":
    main()
