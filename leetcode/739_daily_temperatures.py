class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        mem = []
        res = [0]* len(temperatures)

        for i,t in enumerate(temperatures):
            while mem and t > mem[-1][0]:
                _t, _i = mem.pop()
                res[_i] = i-_i
            mem.append((t,i))

        return res