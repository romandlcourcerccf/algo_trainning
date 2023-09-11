class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        ss = []

        def dfs(i):

            if i >= len(nums):
                res.append(ss.copy())
                return

            ss.append(nums[i])
            dfs(i+1)
            ss.pop()
            dfs(i+1)


        dfs(0)

        return res
