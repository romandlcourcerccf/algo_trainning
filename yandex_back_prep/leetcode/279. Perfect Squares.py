import math


class SlowSolution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        squares = []

        for i in range(1, n + 1):
            if math.isqrt(i) ** 2 == i:
                dp[i] = 1
                squares.append(i)
            else:
                part_num = float("inf")

                for _i in range(i - 1, -1, -1):
                    if dp[_i] == 1:
                        if i - _i >= 1:
                            part_num = min(part_num, dp[_i] + dp[i - _i])
                        else:
                            continue

                dp[i] = part_num

        print("len dp: ", len(dp))
        print("len sq:", len(squares))
        return dp[-1]


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        squares = []

        for i in range(1, n + 1):
            if math.isqrt(i) ** 2 == i:
                dp[i] = 1
                squares.append(i)
            else:
                part_num = float("inf")

                for sq in squares[::-1]:
                    if i - sq >= 1:
                        part_num = min(part_num, 1 + dp[i - sq])
                    else:
                        continue

                # for _i in range(i - 1, -1, -1):
                #     if dp[_i] == 1:
                #         if i - _i >= 1:
                #             part_num = min(part_num, dp[_i] + dp[i - _i])
                #         else:
                #             continue

                dp[i] = part_num

        print("len dp: ", len(dp))
        print("len sq:", len(squares))
        return dp[-1]


assert SlowSolution().numSquares(12) == Solution().numSquares(12)
assert SlowSolution().numSquares(13) == Solution().numSquares(13)
assert SlowSolution().numSquares(8829) == Solution().numSquares(8829)
