class Calendar:
    def __init__(self):
        self._intervels = []

    def _is_intersect(self, i1, i2):
        return not (i1[1] < i2[0] or i2[1] < i1[0])

    def book(self, startTime: int, endTime: int) -> bool:
        for i in range(len(self._intervels)):
            if self._is_intersect(self._intervels[i], [startTime, endTime]):
                return False

        self._intervels.append([startTime, endTime])
        self._intervels.sort(key=lambda x: x[0])

        return True
