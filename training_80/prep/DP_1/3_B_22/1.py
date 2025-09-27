import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "2.txt")
    filename = os.path.join(dir_name, "3.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]


    n, k  = tuple(map(int, rows[0].split()))
   
    if n <= k:
        print(1)
        return

    dp = [0] * n

    for i in range(n):
        if i <=k:
            dp[i] = i
        else:
            dp[i] = sum(dp[i-k:i])

    print(dp[-1])  
    
if __name__ == '__main__':
    main()