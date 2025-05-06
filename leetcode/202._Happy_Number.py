class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self._sum_of_squares(n)

            if n == 1:
                return True

        return False

    def _sum_of_squares(self, n: int) -> int:
        out = 0
        while n:
            digit = n % 10
            digit = digit**2
            out += digit
            n //= 10
        return out
