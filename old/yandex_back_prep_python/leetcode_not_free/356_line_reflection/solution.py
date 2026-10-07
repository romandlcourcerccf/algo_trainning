class Solution:
    def line_reflection(self, points) -> bool:
        p_xs = []

        for p in points:
            p_xs.append(p[0])

        x_max = max(p_xs)
        x_min = min(p_xs)

        x_med = (x_max + x_min) / 2

        p_set = set()

        for p in points:
            p_set.add((p[0], p[1]))

        for p in p_set:
            if p[0] > x_med and (x_max + x_min - p[0], p[1]) not in p_set:
                return False

        return True


s = Solution()

assert s.line_reflection([[1, 1], [-1, 1]]) is True
assert s.line_reflection([[1, 1], [-1, -1]]) is False
