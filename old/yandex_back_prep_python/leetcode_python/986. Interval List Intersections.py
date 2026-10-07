class Solution:
    def intersection(self, i1, i2):
        if i1[1] < i2[0] or i2[1] < i1[0]:
            return []
        else:
            il = max(i1[0], i2[0])
            ir = min(i1[1], i2[1])

            return [il, ir]

    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        res = []

        pos_first = pos_second = 0

        while pos_first < len(firstList) and pos_second < len(secondList):
            i = self.intersection(firstList[pos_first], secondList[pos_second])

            if len(i) > 0:
                res.append(i)

            if firstList[pos_first][1] >= secondList[pos_second][1]:
                pos_second += 1
            else:
                pos_first += 1

        return res
