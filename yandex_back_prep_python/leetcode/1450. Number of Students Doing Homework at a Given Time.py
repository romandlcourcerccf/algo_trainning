class Solution:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:
        busy_counter = 0

        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                busy_counter += 1

        return busy_counter
