import os


def main():

    import os

    def print_dp(dp, days, copouns):
        for d in range(days):
            r = []
            for c in range(copouns):
                r.append(str(dp[c][d]).rjust(5))
            print(*r)


    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, "1.txt")

    with open(filename, "r") as f:
        prises = f.readlines()
        prises = list(map(int, prises))
        days = prises[0]
        prises = prises[1:]

    print("days   :", days)
    print("prises :", prises)

    copouns = days

    dp = [[0] * (copouns+1) for _ in range(days + 1)]
    
   
    for copoun in range(1, copouns):
        dp[0][copoun] = float("inf")

 
    print_dp(dp, days, copouns)
    
    for day in range(1, days+1):
        for copoun in range(copouns):
        
    
            price = prises[day-1]

            if price > 100:
                dp[day][copoun] = min( dp[day-1][copoun + 1],
                                       dp[day-1][copoun - 1] + price)
            else:
                dp[day][copoun] = min(dp[day-1][copoun + 1],
                                       dp[day-1][copoun] + price )

           
    print_dp(dp, days, copouns)


if __name__ == "__main__":
    main()

