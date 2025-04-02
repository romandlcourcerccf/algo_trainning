import os


def main():

    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    # filename = os.path.join(dname, "3.txt")

    with open(filename, "r") as f:
        money = int(f.readline())
        

    print("money   :", money)
    
    dp = [float('inf')] * (money)
    dp[0] = 0

    for m in range(1,money):
        for c in [1,3,4]:
            if c <= m:
                dp[m] = min(dp[m], 1 + dp[m-c])

    # print(dp)
    print(dp[-1])
    

if __name__ == "__main__":
    main()

