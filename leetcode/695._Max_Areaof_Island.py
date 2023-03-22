class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = float('-inf')
        area = 0

        cols = len(grid[0])
        rows = len(grid)

        def dfs(col, row):
            nonlocal area
            area +=1

            if col-1>= 0 and grid[row][col-1] == 1:
                grid[row][col-1] = 2
                dfs(col-1, row)
            
            if row-1>=0 and grid[row-1][col] == 1:
                grid[row-1][col] = 2
                dfs(col, row-1)

            if row+1 <= rows-1 and grid[row+1][col] == 1:
                grid[row+1][col] = 2
                dfs(col, row+1)

            if col+1 <= cols-1 and grid[row][col+1] == 1:
                grid[row][col+1] = 2
                dfs(col+1, row)

        
        for col in range(cols):
            for row in range(rows):
                if grid[row][col] == 1:
                    area = 0
                    dfs(col, row)
                max_area = max(max_area, area)

        return max_area