class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

            if len(count) <= 2:
                continue
            
            newcount = defaultdict(int)
            for _n, _k in count.items():
                if _k > 1:
                    newcount[_n] = _k-1

            count = newcount

        res = []

        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        
        return res
            