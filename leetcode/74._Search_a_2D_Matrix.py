class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def birary_search(arr, l, r):
            while l<=r:
                mid = (l+r) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        
        def search_in_matrix(matrix, up, down):

            while up <= down:
                mid = (up+down) // 2
                if  matrix[mid][0] <=target <= matrix[mid][cols-1]:
                    return birary_search(matrix[mid], 0, cols-1)
                elif matrix[mid][0] > target:
                    down = mid-1
                else :
                    up = mid+1
            
            return False
                
        return search_in_matrix(matrix, 0, rows-1)