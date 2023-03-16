class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        mem = []
        res = [0]* len(temperatures)

        for i, t in enumerate(temperatures):
            
            _mem = []
            while len(mem)>0:
                _i, _t = mem.pop()
                if _t < t:
                    res[_i] = i - _i
                else:
                    _mem.append((_i, _t))
            mem = _mem  
            mem.append((i, t))

        return res
