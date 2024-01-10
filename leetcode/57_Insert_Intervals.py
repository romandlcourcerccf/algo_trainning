class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)

        return res


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        def overlaps(i1, i2):
            return max(i1[0], i2[0]) < min(i1[1], i2[1])
    
        def merge(l):
            l1 = [i[0] for i in l]
            l2 = [i[1] for i in l]

            _l = l1 + l2

            return [min(_l), max(_l)]

        i = 0
        while i <= len(intervals)-1:

            print('>>',i)
            if not overlaps(intervals[i], newInterval):
                res.append(intervals[i])
            else:
                tmp = []
                tmp.append(newInterval)
                while i<=len(intervals)-1 and overlaps(intervals[i], newInterval):
                    tmp.append(intervals[i])
                    i+=1
                    
                print('Overlap :', tmp)
                res.append(merge(tmp))

            i+=1

        return res