#Recursive solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])

        res = []
        for p in perms:
            for i in range(len(p)+1):
                _p = p.copy()
                _p.insert(i, nums[0])
                res.append(_p)

        return res
    
#Non rec solutioin
    
    class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = [[]]

        for n in nums:
            new_perms = []
            for p in perms:
                
                for i in range(len(p)+1):
                    _p = p.copy()
                    _p.insert(i, n)
                    new_perms.append(_p)
            
            perms = new_perms

        return perms
    
    

