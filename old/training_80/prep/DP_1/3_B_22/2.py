import os

def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "input.txt")
    # filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "3.txt")
    # filename = os.path.join(dir_name, "2.txt")
    # filename = os.path.join(dir_name, "3.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]


    n, k  = tuple(map(int, rows[0].split()))

    # print(f'n {n} k {k}')
   
    dp = [0] * (n+1)

    if n > k:
        for i in range(1, n+1):
            if i == 1:
                dp[i] = 1

            elif i < k:
                dp[i] = sum(dp[:i-1+1])
            else:
                dp[i] = sum(dp[i-k:i])
    elif n <= k:
        for i in range(1, n+1):
            if i == 1:
                dp[i] = 1
            else:
                dp[i] = sum(dp[:i])
    
    print(dp[-1])

if __name__ == '__main__':
    main()