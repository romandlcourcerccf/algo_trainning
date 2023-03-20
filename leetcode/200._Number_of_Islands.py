class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        cols = len(grid)
        rows = len(grid[0])

        def _print():
            for row in range(rows-1): 
                print(grid[row])      
            print('\n')

        def valid(c, r):
            return c >= 0 and c <= cols-1 and r >= 0 and r <= rows-1 and grid[c][r] == '1'

        def dfs(col, row):
            # print('col :', col, 'row :', row)
            grid[col][row] = '2'

            left = (col-1, row)
            if valid(left[0], left[1]): dfs(left[0], left[1])
            right = col+1, row
            if valid(right[0], right[1]): dfs(right[0], right[1])
            up = col, row+1
            if valid(up[0], up[1]): dfs(up[0], up[1])
            down = col, row-1
            if valid(down[0], down[1]): dfs(down[0], down[1])

        # _print()
        islands = 0       
        for col in range(cols):
            for row in range(rows): 
                if grid[col][row] == '1':
                    islands +=1
                    dfs(col, row)
                    # _print()
        
        return islands