class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        union = []

        def _is_overlap(i1, i2):
            return not ((i1[0] <= i2[0] and i1[1] <= i2[0]) and (i2[0] <= i1[0] and i2[1] <= i1[0]))

        def _union(intervals):
            l = []
            r = []
            for i in intervals:
                l.append(i[0])
                r.append(i[1])
            
            return [min(l), max(r)]

        for i in range(len(intervals)):
            cur = intervals[i]
            if not _is_overlap(cur, union):
                res.append(union.copy())
                union = []
                union.append(cur)
            else:
                union = _union(union, cur)

        return res
    
    