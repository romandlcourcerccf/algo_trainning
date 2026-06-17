class Solution:
    def reverse(self, x: int) -> int:
        def _reverce_positive(_x):
            res = []

            while _x:
                rem_part = _x % 10
                int_part = _x // 10
                res.append(str(rem_part))
                _x = int_part

            return int("".join(res))

        if x < 0:
            res = -_reverce_positive(-x)
        elif x > 0:
            res = _reverce_positive(x)
        else:
            res = 0

        if res > 2**31 - 1 or res < -(2**31):
            # if res > 2**31 - 1 or res < -(2**31):
            return 0

        return res


s = Solution()
print(s.reverse(9646324351))
