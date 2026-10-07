# You are given n points on a 2D plane. Your task is to determine if
# there exists a vertical line (parallel to the y-axis) such that when all points are reflected across this line,
# the resulting set of points is identical to the original set.


class Solution:
    def line_reflection(self, points) -> bool:
        xs = [p[0] for p in points]
        ps = {(p[0], p[1]) for p in points}

        l_bound = min(xs)
        r_bound = max(xs)

        middle = (l_bound + r_bound) / 2  # key fact

        for p in ps:
            if p[0] < middle:
                if (p[0] + abs(p[0] - middle) * 2, p[1]) not in ps:
                    return False
            if p[0] > middle:
                if (p[0] - abs(p[0] - middle) * 2, p[1]) not in ps:
                    return False

        return True


s = Solution()

assert s.line_reflection([[1, 1], [-1, 1]]) is True
assert s.line_reflection([[1, 1], [-1, -1]]) is False
