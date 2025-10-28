class Solution:
    def line_reflection(self, points) -> bool:
        xs = [p[0] for p in points]
        print(xs)

        p_set = set()
        for p in points:
            p_set.add((p[0], p[1]))

        max_x = max(xs)
        min_x = min(xs)

        x_mid = int((max_x + min_x) / 2)
        radius = abs(max_x - min_x)

        for p in points:
            if p[0] <= x_mid:
                if (p[0] + radius, p[1]) not in p_set:
                    return False

        return True


s = Solution()

assert s.line_reflection([[1, 1], [-1, 1]]) == True
assert s.line_reflection([[1, 1], [-1, -1]]) == False
