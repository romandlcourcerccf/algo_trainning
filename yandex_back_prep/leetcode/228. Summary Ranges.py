class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        nums.append(100)

        res = []
        pos = 0
        intreval = []
        while pos <= len(nums)-2:
            if nums[pos]+1 != nums[pos+1]:
                intreval.append(nums[pos])
                res.append(intreval.copy())
                intreval = []
            else:
                intreval.append(nums[pos])
            pos +=1

        print(res)

        _res = []
        for r in res:
            if len(r) == 1:
                _res.append(f"{r[0]}")
            else:
                _res.append(f"{r[0]}->{r[-1]}")
        
        return _res