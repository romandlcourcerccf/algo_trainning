class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        def bin_search(row, target):
            l, r = 0, len(row)-1
            while l <= r:
                m = (l+r) // 2
                if row[m] == target:
                    return True
                elif row[m] < target:
                    l = m+1
                else:
                    r = m-1

            return False

        u, d = 0, rows-1

        while u <= d:
            h = (u+d) // 2
            
            if matrix[h][0] <= target <= matrix[h][-1]:
                return bin_search(matrix[h], target)
            elif target > matrix[h][-1]:
                u = h+1
            elif target < matrix[h][0]:
                d = h-1

        
        return False
