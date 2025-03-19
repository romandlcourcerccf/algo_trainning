import os


def main():

    import os

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

    dp = [[0] * copouns for i in range(days + 1)]

    for copoun in range(1, copouns):
        dp[0][copoun] = float("inf")

    for day in range(1, days + 1):
        for copoun in range(copouns - 1):

            if prises[day - 1] > 100:
                dp[day][copoun] = min(
                    dp[day - 1][copoun + 1], dp[day - 1][copoun - 1] + prises[day - 1]
                )
            else:
                dp[day][copoun] = min(dp[day - 1][copoun + 1], prises[day - 1])

    print(dp)


if __name__ == "__main__":
    main()
