import os

        
def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "2.txt")
    # filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "4.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]
 
    
    fields = []
    N, M = tuple(map(int, rows[0].split()))
    for row in rows[1:]:
        fields.append(list(map(int, row.split())))

    # print(fields)

    dp = [ [0 for n in range(M)] for m in range(N)]
    path = []

    for n in range(N):
        for m in range(M):
            if n==0:
                dp[n][m] += dp[n][m-1] + fields[n][m]
            elif m==0:
                dp[n][m] += dp[n-1][m] + fields[n][m]
            else:
                dp[n][m] += max(dp[n][m-1] , dp[n-1][m]) + fields[n][m]
 
    print(dp[-1][-1])

    n,m = N-1, M-1
    while n !=0 and m !=0:
        if dp[n][m-1] >= dp[n-1][m]:
            path.append('R')
            m-=1
        else:
            path.append('D')
            n -=1

    if n > 0:
        while n !=0:
            path.append('D')
            n -=1
    else:
        while m !=0:
            path.append('R')
            m-=1

    print(*path[::-1])

    


if __name__ == '__main__':
    main()