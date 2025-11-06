class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        return reduce(lambda i, j: int(i) ^ int(j), nums)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        s = set()

        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)

        return list(s)[0]