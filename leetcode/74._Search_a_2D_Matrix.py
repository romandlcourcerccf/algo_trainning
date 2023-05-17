class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])

        def bin_search(arr, target):
            left, right = 0, len(arr)-1

            while left <= right:
                pos = (left + right) // 2
                if arr[pos] == target:
                    return True 
                elif arr[pos] < target:
                    left = pos+1
                else:
                    right = pos-1
            
            return False

        if rows == 1: return bin_search(matrix[0], target)

        up, down = 0, rows-1
        # print('up :', up, 'down :', down)

        while up <= down:
            pos = (up + down) // 2
            if matrix[pos][0] <= target <= matrix[pos][cols-1]:
                return bin_search(matrix[pos], target)
            elif matrix[pos][0] >= target:
                down = pos-1
            elif matrix[pos][cols-1] <= target:
                up = pos+1

        return False