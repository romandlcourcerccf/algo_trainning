class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_val = float('-inf')
        res = [0] * len(arr)
        for i in range(len(arr)-2, -1, -1):
            max_val = max(arr[i+1], max_val)
            res[i] = max_val
        
        res[-1] = -1

        return res 