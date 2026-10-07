import sys
from collections import defaultdict

def main():
    
                                      
    rows = sys.stdin.readlines()

    
    nums = int(rows[0])

    dp = [[0] * 4 for i in range(nums+3)]

    for i in range(1, len(rows)):

        row = list(map(int, rows[i].split()))
        row.append(0)

        dp[i+2] = row

    for i in range(3):
        for c in range(3):
            dp[i][c] = float('inf')

    for i in range(3, nums+3):
        dp[i][3] = min(dp[i-1][3]+dp[i][0], dp[i-2][3]+dp[i-1][1], dp[i-3][3]+dp[i-2][2])

    print(dp[-1][-1])

    

if __name__ == '_