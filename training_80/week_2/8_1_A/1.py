import os


def main():

    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
 

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]
        
    N = int(rows[0])

    dp = [0]*N

    for i in range(N):
        if i == 0:
            dp[i] = 1
        elif i == 1:
            dp[i] = 2
        elif i == 2:
            dp[i] += dp[i-1] + dp[i-2] + 1
    
        else:
            dp[i] += dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[-1])
        

if __name__ == "__main__":
    main()

   


