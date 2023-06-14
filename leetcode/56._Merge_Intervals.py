class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []

        intervals.sort(key=lambda x: x[0])

        cur = None
        for i in range(len(intervals)):
            if i == 0:
                cur = intervals[i]
            else:
                if cur[1] < intervals[i][0]:
                   res.append(cur) 
                   cur = intervals[i]
                else:
                    cur = [min(cur[0], intervals[i][0]), max(cur[1], intervals[i][1])]
        

        # print('res :',res)
        # print('cur :',cur)

        res = res + [cur]
        
        return res