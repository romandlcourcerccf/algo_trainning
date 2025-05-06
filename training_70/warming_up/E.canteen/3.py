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

    dp = [[0] * (copouns) for _ in range(days + 1)]
    
    for copoun in range(1, copouns):
        dp[0][copoun] = float("inf")

 
    print_dp(dp, days, copouns)
   
    for day in range(1, days):
        day_prise = prises[day-1]
        print(day_prise)
        for copoun in range(copouns):
            if day_prise > 100:
                if copoun == 0:
                    dp[day][copoun] = dp[day-1][copoun+1]
                else:
                    if copoun == copouns-1:

                        dp[day][copoun] = dp[day-1][copoun-1] + day_prise
                    else:
                        dp[day][copoun] = min(dp[day-1][copoun-1] + day_prise, dp[day-1][copoun+1])
            else:
                if copoun == copouns-1:
                    dp[day][copoun] = dp[day-1][copoun] + day_prise
                else:
                    dp[day][copoun] = min(dp[day-1][copoun] + day_prise, dp[day-1][copoun+1])
    
           
    print_dp(dp, days, copouns)


if __name__ == "__main__":
    main()

