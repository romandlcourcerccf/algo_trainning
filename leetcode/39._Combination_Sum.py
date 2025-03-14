class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        arr = []

        def dfs(i, arr):
            if i > len(candidates) - 1 or sum(arr) > target:
                return

            if sum(arr) == target:
                res.append(arr.copy())
                return

            arr.append(candidates[i])
            dfs(i, arr)
            arr.pop()
            dfs(i + 1, arr)

        dfs(0, arr)

        return res
