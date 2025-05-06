


def main():


    import os

    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, "input.txt")
    

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip().split() for r in rows]


    rows = [list(map(int, r)) for r in rows]

    N, M = rows[0]
    W = rows[1]
    C = rows[2]


    dp = [-1] * (M+1)    
    dp[0] = 0
    tr = [-1] * (M+1)
    
   
    for item_index in range(len(W)):
        for i in range(len(dp)-1 - W[item_index], -1, -1):
            if dp[i] != -1:
                dp[i+ W[item_index]] = max(dp[i] +  C[item_index], dp[i+ W[item_index]])

    print(max(dp))
    

if __name__ == "__main__":
    main()
