class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def v_search(matrix, target):
            cols = len(matrix[0])
            up, down = 0, len(matrix)-1
            while up <= down:
                m = (up + down) // 2
                if matrix[m][0] <= target <= matrix[m][cols-1]:
                    return  h_search(matrix[m], target)
                elif target > matrix[m][cols-1]:
                    up = m+1
                else:
                    down = m-1
            
            return False

        def h_search(row, target):
            l, r = 0,  len(row)-1
            while l <= r:
                m = (l+r) // 2
                if row[m] == target:
                    return True
                elif row[m] > target:
                    r = m-1
                else:
                    l = m+1
            return False

        return v_search(matrix, target)
        
                




