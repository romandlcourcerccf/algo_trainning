import os

        
def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "2.txt")
    filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "4.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]
 
    
    N, M = tuple(map(int, rows[0].split()))

    # print(f'N {N} M {M}')
    
    dp = [ [0 for m in range(M)] for n in range(N) ]
    dp[0][0] = 1

    for row in range(N):
        for col in range(M):
             
            if row >= 2 and col >=1:
                dp[row][col] += dp[row-2][col-1]

            if row >= 1 and col >=2:
                dp[row][col] += dp[row-1][col-2]
            

    for r in range(len(dp)):
        print(dp[r])
    
    print(dp[-1][-1])



if __name__ == '__main__':
    main()