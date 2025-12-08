class ScoresTracker:
    def __init__(self):
        self._times = []
        self._scores = []

    def _get_closest_time(self, time: int, opt: str) -> int:
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

    def totalScore(self, startTime: int, endTime: int):
        left_border = self._get_closest_time(startTime, "l")
        right_border = self._get_closest_time(endTime, "r")

        print(f"startTime : {startTime} left_border : {left_border}")
        print(f"endTime : {endTime} right_border : {right_border}")

        return sum(self._scores[left_border : right_border + 1])
