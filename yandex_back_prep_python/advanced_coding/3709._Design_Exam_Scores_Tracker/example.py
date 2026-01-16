python


class ExamTracker:
    def __init__(self):
        self.rs = 0
        self.times = [0]
        self.pf = [0]

    def record(self, time: int, score: int) -> None:
        self.rs += score
        self.pf.append(self.rs)
        self.times.append(time)

    def totalScore(self, startTime: int, endTime: int) -> int:
        # idx where time is less than or equal to start Time
        lower_idx = bisect_left(self.times, startTime)
        # idx where time is greater than end time
        upper_idx = bisect_right(self.times, endTime)

        # hence -1 to upper_idx to get time <= endTime
        # hence -1 to lower_idx to get time <= startTime
        return self.pf[upper_idx - 1] - self.pf[lower_idx - 1]


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)
