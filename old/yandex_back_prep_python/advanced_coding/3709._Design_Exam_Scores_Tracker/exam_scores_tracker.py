class ExamTracker:
    def __init__(self):
        self._times = []
        self._scores = []
        self._prefix_sum = [0]

    def _get_closest_index(self, time: int, opt: str) -> int:
        l, r = 0, len(self._times) - 1

        while l <= r:
            m = (l + r) // 2
            if self._times[m] == time:
                return m
            elif self._times[m] > time:
                r = m - 1
            else:
                l = m + 1

        if opt == "l":
            return max(l, r)
        else:
            return min(l, r)

    def record(self, time: int, score: int) -> None:
        self._times.append(time)
        self._scores.append(score)
        self._prefix_sum.append(self._prefix_sum[-1] + score)

    def totalScore(self, startTime: int, endTime: int):
        left_border = self._get_closest_index(startTime, "l")
        right_border = self._get_closest_index(endTime, "r")

        return self._prefix_sum[right_border + 1] - self._prefix_sum[left_border]
