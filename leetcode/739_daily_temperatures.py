class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        s = []

        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while s and t > s[-1][1]:
                _i, _t = s.pop()
                res[_i] = i - _i
            s.append((i,t)) 

            
        return res
