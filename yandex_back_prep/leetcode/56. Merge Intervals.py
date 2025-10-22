class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []
        pos = 0

        def is_overlaped(i1, i2):
            return not i1[1] < i2[0] or i1[0] > i2[1]

        def merge_intervals(i1, i2):
            return [min(i1[0], i2[0]), max(i1[1], i2[1])]

        while pos <= len(intervals) - 2:
            if not is_overlaped(intervals[pos], intervals[pos + 1]):
                res.append(intervals[pos])
            else:
                intervals[pos + 1] = merge_intervals(intervals[pos], intervals[pos + 1])
            pos += 1

        while pos < len(intervals):
            res.append(intervals[pos])
            pos += 1

        return res
    
    class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key= lambda x: x[0])

        res = []

        def is_intersected(i1, i2):
            return not i1[1] < i2[0] 
        
        def merge(i1, i2):
            return [min(i1[0], i2[0]), max(i1[1], i2[1])]

        for i in range(len(intervals)-1):
            if not is_intersected(intervals[i], intervals[i+1]):
                res.append(intervals[i])
            else:
                intervals[i+1] = merge(intervals[i], intervals[i+1])

        res.append(intervals[-1])

        return res

        
